from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

# Setup proxy
pg = ProxyGenerator()
# pg.FreeProxies()  # Use free rotating proxies
pg.SingleProxy(http="http://user-usslab2013:db2013@pr.roxlabs.cn:4600", https="https://user-usslab2013:db2013@pr.roxlabs.cn:4600")
# pg.ScraperAPI("43019212068df4f4851b40f33cf238fe")

scholarly.use_proxy(pg)
os.environ['GOOGLE_SCHOLAR_ID'] = 'cz6jVd0AAAAJ'
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
