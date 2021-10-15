import Crawler
import Parser
import DB

crawler = Crawler.Crawler()
html = crawler.crawl("https://paiza.jp/career/job_offers")

# 分析用コード
print(html.text)

parser = Parser.Parser()
parser.parse(html.text)

db = DB.DB()
db.open()

db.close()


del parser