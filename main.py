from scrape import scrape_site
from parse import parse_html_text

html = scrape_site("https://paiza.jp/career/job_offers")

# 分析用コード
print(html.text)

parse_html_text(html.text)