from pathlib import Path
from PIL import Image
import json, xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
services=json.loads((R/'data/six-service-contract.json').read_text())['services']
assert len(services)==6
assert len({s['id'] for s in services})==6
assert len({s['name'] for s in services})==6
routes=json.loads((R/'data/routes.json').read_text())
assert routes['github']=='ismailabs/kilatmoto'
assert routes['worker']=='kilatmoto'
assert routes['production_origin']=='https://kilatmoto.ismailstudio.my'
assert routes['display_brand']=='KILAT MOTORWORKS'
assert routes['old_host_redirect'] is False
for p in (R/'assets/brand').glob('*.svg'): ET.parse(p)
for p in list((R/'assets/photos').glob('*.webp'))+list((R/'design').rglob('*.png')):
 with Image.open(p) as im: im.verify()
assert len(list((R/'design/concept-boards').glob('*.png')))==4
assert len(list((R/'design/implementation-mockups').glob('*.png')))==4
print('OK: handoff assets, six protected services, technical slugs, no old-host redirect, 4 boards, 4 precise mockups')
