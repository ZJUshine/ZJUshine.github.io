from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

# Setup proxy using ScraperAPI
scraper_api_key = os.environ.get('SCRAPER_API_KEY','43019212068df4f4851b40f33cf238fe')
if scraper_api_key:
    pg = ProxyGenerator()
    success = pg.ScraperAPI(scraper_api_key)
    if success:
        scholarly.use_proxy(pg)
        print("ScraperAPI proxy configured successfully")
    else:
        print("Warning: Failed to configure ScraperAPI proxy")
else:
    print("Warning: SCRAPER_API_KEY not set, running without proxy (may be rate limited)")

# 从环境变量获取 Scholar ID，如果未设置则使用默认值
scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'cz6jVd0AAAAJ')
author = None

# 多次尝试获取作者信息
max_retries = 5
retry_delay = 2  # 秒
for attempt in range(max_retries):
    try:
        author = scholarly.search_author_id(scholar_id)
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
