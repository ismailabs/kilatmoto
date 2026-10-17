"""Fail-closed review of explicitly staged files. This is not Gitleaks."""
import subprocess,re
names=subprocess.check_output(['git','diff','--cached','--name-only','-z']).decode().split('\0')
problems=[];total=0
for name in filter(None,names):
 if re.search(r'(^|/)(\.env[^/]*|\.dev\.vars[^/]*|node_modules|dist|\.wrangler|tmp|\.git)(/|$)',name):problems.append('Forbidden path: '+name)
 content=subprocess.check_output(['git','show',':'+name]);total+=len(content)
 if b'\x00' in content[:4096]:continue
 text=content.decode('utf8',errors='ignore')
 patterns=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'\bgh[pousr]_[A-Za-z0-9]{30,}',r'\bgithub_pat_[A-Za-z0-9_]{40,}',r'\bsk-(?:proj-)?[A-Za-z0-9_-]{30,}',r'\bAKIA[A-Z0-9]{16}\b']
 if any(re.search(p,text) for p in patterns):problems.append('Potential secret: '+name)
subprocess.run(['git','diff','--cached','--check'],check=True)
if problems:raise SystemExit('\n'.join(problems))
print(f'PASS: {len([n for n in names if n])} staged files / {total} bytes; forbidden-path, custom secret-pattern and whitespace checks. Not a Gitleaks audit.')
