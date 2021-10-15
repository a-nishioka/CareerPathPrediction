import Crawler
import Parser
import Data

crawler = Crawler.Crawler()
html = crawler.crawl("https://paiza.jp/career/job_offers")

# 分析用コード
print(html.text)

parser = Parser.Parser()
parser.parse(html.text)

data = Data.Data()

del data
del parser