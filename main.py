from scrape import scrape_site
from parse import parse_html_text

html = scrape_site("https://paiza.jp/career/job_offers")
soup = parse_html_text(html.text)