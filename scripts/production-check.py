"""Verify actual public HTTPS, route/asset bytes, SEO and old-host behaviour."""
import argparse,json,subprocess,hashlib,ssl,socket,re
from urllib.request import Request,urlopen,build_opener,HTTPRedirectHandler
from urllib.error import HTTPError
from urllib.parse import urlsplit
from pathlib import Path
from datetime import datetime,timezone
from verify_static import Scan
import xml.etree.ElementTree as ET
parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['staging','production'],default='production');parser.add_argument('--sha',required=True);args=parser.parse_args()
origin='https://kilatmoto.ismailstudio.my';routes=['/','/about/','/services/','/projects/','/contact/']
out={'time':datetime.now(timezone.utc).isoformat(),'origin':origin,'mode':args.mode,'expected_sha':args.sha,'routes':[],'assets':[],'checks':[]};issues=[];targets=set()
def check(name,ok):
 out['checks'].append({'name':name,'pass':bool(ok)})
 if not ok:issues.append(name)
def get(url):
 with urlopen(Request(url,headers={'User-Agent':'KILAT-release-verification/1.0','Accept-Encoding':'identity'}),timeout=40) as r:return r.status,dict(r.headers.items()),r.read(),r.geturl()
def eqgit(path,data):
 expected=subprocess.check_output(['git','show',args.sha+':'+path]);return hashlib.sha256(expected).hexdigest()==hashlib.sha256(data).hexdigest()
try:
 for route in routes:
  status,headers,data,final=get(origin+route);scan=Scan();scan.feed(data.decode('utf8'));low={k.lower():v for k,v in headers.items()};source=data.decode('utf8')
  out['routes'].append({'route':route,'status':status,'final_url':final,'headers':headers,'title':scan.title,'robots':scan.metadata.get('robots'),'body_sha256':hashlib.sha256(data).hexdigest()})
  check(route+' direct 200',status==200 and final==origin+route);check(route+' content matches committed source',eqgit(('index.html' if route=='/' else route.strip('/')+'/index.html'),data));check(route+' release header',low.get('x-release-sha')==args.sha)
  check(route+' only local application script',[a.get('src') for t,a in scan.tags if t=='script']==['/assets/js/main.js'])
  check(route+' brand and fictional disclosure','KILAT MOTORWORKS' in source and 'fictional' in source.lower());check(route+' security policies',"connect-src 'none'" in low.get('content-security-policy','') and "form-action 'none'" in low.get('content-security-policy','') and low.get('x-frame-options')=='DENY')
  if args.mode=='production':
   check(route+' indexable',scan.metadata.get('robots')==['index, follow'] and 'noindex' not in low.get('x-robots-tag','').lower());check(route+' canonical',any(t=='link' and a.get('rel')=='canonical' and a.get('href')==origin+route for t,a in scan.tags));check(route+' social',scan.metadata.get('og:url')==[origin+route] and scan.metadata.get('og:image')==[origin+'/og-image.webp'] and scan.metadata.get('twitter:image')==[origin+'/og-image.webp'])
  else:check(route+' staging noindex',scan.metadata.get('robots')==['noindex, follow'] and 'noindex' in low.get('x-robots-tag',''))
  for ref in scan.references:
   p=urlsplit(ref)
   if p.path.startswith('/assets/') or p.path in ['/favicon.svg','/og-image.webp']:targets.add(p.path)
 for path in sorted(targets|{'/assets/fonts/space-grotesk.ttf'}):
  status,headers,data,final=get(origin+path);out['assets'].append({'path':path,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()});check(path+' asset matches committed source',status==200 and eqgit(path.lstrip('/'),data))
 status,headers,data,final=get(origin+'/release.json');out['release']=json.loads(data);check('Hosted release manifest clean matching SHA',out['release']['git_sha']==args.sha and not out['release']['dirty'])
 for path in ['/robots.txt','/sitemap.xml']:
  status,headers,data,final=get(origin+path);out[path]=data.decode();check(path+' matches committed source',status==200 and eqgit(path.lstrip('/'),data))
 if args.mode=='production':
  check('Five sitemap URLs',[e.text for e in ET.fromstring(out['/sitemap.xml']).iter() if e.tag.endswith('loc')]==[origin+r for r in routes]);check('Robots permits crawl with sitemap','Allow: /' in out['/robots.txt'] and 'Disallow: /' not in out['/robots.txt'] and 'Sitemap: '+origin+'/sitemap.xml' in out['/robots.txt'])
 class NoRedirect(HTTPRedirectHandler):
  def redirect_request(self,*a,**k):return None
 opener=build_opener(NoRedirect)
 try:
  with opener.open('https://rapimotion.ismailstudio.my/',timeout=40) as r: old={'status':r.status,'headers':dict(r.headers.items()),'body':r.read().decode()}
 except HTTPError as e:old={'status':e.code,'headers':dict(e.headers.items()),'body':e.read().decode()}
 out['old_host_http']={'status':old['status'],'headers':old['headers']}
 # The old host returns 403 to urllib but 200 to a normal browser. Preserve both observations.
 old_browser=json.loads(subprocess.check_output(['node','scripts/old-host-check.cjs'],text=True))
 out['old_host_browser']=old_browser
 check('Old host no redirect to new host',old_browser['status']==200 and old_browser['final_url']=='https://rapimotion.ismailstudio.my/' and old_browser['request_chain']==['https://rapimotion.ismailstudio.my/'])
 check('Old host remains original noindex site','RAPI MOTION' in old_browser['title'] and 'noindex' in old_browser['robots'])
 for path in ['/.git/config','/README.md','/kilatmoto-Codex-Handoff/00-START-HERE.md','/scripts/build.mjs','/node_modules/','/not-a-route/']:
  try:s,h,d,u=get(origin+path)
  except HTTPError as e:s=e.code
  check(path+' not published',s==404)
 out['dns_addresses']=sorted({r[4][0] for r in socket.getaddrinfo('kilatmoto.ismailstudio.my',443)})
 with socket.create_connection(('kilatmoto.ismailstudio.my',443),timeout=20) as sock:
  with ssl.create_default_context().wrap_socket(sock,server_hostname='kilatmoto.ismailstudio.my') as conn:out['tls']={'version':conn.version(),'certificate':conn.getpeercert()}
 check('TLS hostname and trust chain verified',bool(out['tls']['certificate']))
except Exception as error:
 issues.append(type(error).__name__+': '+str(error))
 raise
finally:
 out['issues']=issues;Path('qa-artifacts').mkdir(exist_ok=True);Path('qa-artifacts/'+args.mode+'-http-evidence.json').write_text(json.dumps(out,indent=2));print(json.dumps({'mode':args.mode,'checks':len(out['checks']),'issues':issues}))
if issues:raise SystemExit(1)
