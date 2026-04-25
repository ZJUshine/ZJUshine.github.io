from serpapi import GoogleSearch
import json
from datetime import datetime
import os


def get_metric(table, *metric_names):
    if not isinstance(table, list):
        return {}
    for row in table:
        if not isinstance(row, dict):
            continue
        for metric_name in metric_names:
            metric = row.get(metric_name)
            if isinstance(metric, dict):
                return metric
    return {}


def get_recent_value(metric):
    if not isinstance(metric, dict):
        return 0
    for key, value in metric.items():
        if key != "all":
            return value
    return 0


def get_cites_per_year(graph):
    if not isinstance(graph, list):
        return {}
    return {
        str(item["year"]): item["citations"]
        for item in graph
        if isinstance(item, dict) and "year" in item and "citations" in item
    }


# 从环境变量获取配置
scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'cz6jVd0AAAAJ')
serpapi_key = os.environ.get('SERPAPI_KEY', '9938fa8825ae54f488af513966a790e1a3697bbcb409cfce0ece552fa9e9228c')

if not serpapi_key:
    raise ValueError("SERPAPI_KEY environment variable is required")

author = None

try:
    # 获取作者基本信息和引用统计
    params = {
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "hl": "en",
        "api_key": serpapi_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    if "error" in results:
        raise Exception(results["error"])

    author_info = results.get("author", {})
    cited_by = results.get("cited_by", {})
    cited_by_table = cited_by.get("table", [])
    citations = get_metric(cited_by_table, "citations")
    h_index = get_metric(cited_by_table, "h_index", "indice_h")
    i10_index = get_metric(cited_by_table, "i10_index", "indice_i10")

    # 获取所有文章（处理分页）
    all_articles = []
    start = 0
    while True:
        params_articles = {
            "engine": "google_scholar_author",
            "author_id": scholar_id,
            "api_key": serpapi_key,
            "hl": "en",
            "start": start,
            "num": 100
        }
        search_articles = GoogleSearch(params_articles)
        articles_results = search_articles.get_dict()

        articles = articles_results.get("articles", [])
        if not articles:
            break
        all_articles.extend(articles)
        start += len(articles)

        # 安全限制，防止无限循环
        if start >= 1000:
            break

    # 构建兼容 scholarly 格式的 author 对象
    author = {
        "name": author_info.get("name", ""),
        "affiliation": author_info.get("affiliations", ""),
        "email_domain": author_info.get("email", ""),
        "interests": [interest.get("title", "") for interest in author_info.get("interests", [])],
        "citedby": citations.get("all", 0),
        "citedby5y": get_recent_value(citations),
        "hindex": h_index.get("all", 0),
        "hindex5y": get_recent_value(h_index),
        "i10index": i10_index.get("all", 0),
        "i10index5y": get_recent_value(i10_index),
        "cites_per_year": get_cites_per_year(cited_by.get("graph", [])),
        "scholar_id": scholar_id,
        "url_picture": author_info.get("thumbnail", ""),
    }

    # 转换文章格式
    publications = []
    for article in all_articles:
        pub = {
            "author_pub_id": f"{scholar_id}:{article.get('citation_id', '')}",
            "bib": {
                "title": article.get("title", ""),
                "citation": article.get("authors", ""),
                "pub_year": str(article.get("year", "")),
            },
            "num_citations": article.get("cited_by", {}).get("value", 0),
            "citedby_url": article.get("cited_by", {}).get("link", ""),
            "pub_url": article.get("link", ""),
        }
        publications.append(pub)

    author["publications"] = publications

    print(json.dumps(author, indent=2))

except Exception as e:
    print(f"Error: {e}")
    raise

if author is not None:
    name = author.get('name', '')
    updated_time = str(datetime.now())
    publications = author.get('publications', [])
    publications_dict = {v.get('author_pub_id', f'pub_{i}'): v for i, v in enumerate(publications)} if isinstance(publications, list) else {}

    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w') as outfile:
        json.dump({**author, 'updated': updated_time, 'publications': publications_dict}, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with open('results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
