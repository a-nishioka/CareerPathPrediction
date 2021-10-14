from scrape import scrape_site

html = scrape_site("https://paiza.jp/career/job_offers")

# 分析用コード
print(html.text)