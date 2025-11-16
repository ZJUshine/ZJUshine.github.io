from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

# Setup proxy
pg = ProxyGenerator()
# pg.FreeProxies()  # Use free rotating proxies
pg.SingleProxy(http="http://user-usslab2013:db2013@pr.roxlabs.cn:4600", https="https://user-usslab2013:db2013@pr.roxlabs.cn:4600")
# pg.ScraperAPI("43019212068df4f4851b40f33cf238fe")

scholarly.use_proxy(pg)
os.environ['GOOGLE_SCHOLAR_ID'] = 'cz6jVd0AAAAJ'
author = None

# 多次尝试获取作者信息
max_retries = 5
retry_delay = 2  # 秒
for attempt in range(max_retries):
    try:
        author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        break  # 成功则退出循环
    except Exception as e:
        if attempt < max_retries - 1:
            print(f"尝试 {attempt + 1}/{max_retries} 失败: {e}，{retry_delay}秒后重试...")
            time.sleep(retry_delay)
        else:
            print(f"所有 {max_retries} 次尝试均失败: {e}")
            raise

if author is not None:
    name = author.get('name', '')
    updated_time = str(datetime.now())
    publications = author.get('publications', [])
    publications_dict = {v.get('author_pub_id', f'pub_{i}'): v for i, v in enumerate(publications)} if isinstance(publications, list) else {}
    print(json.dumps(author, indent=2))
    os.makedirs('results', exist_ok=True)
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump({**author, 'updated': updated_time, 'publications': publications_dict}, outfile, ensure_ascii=False)

    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{author.get('citedby', 0)}",
    }
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
