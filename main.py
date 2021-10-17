import Crawler
import Parser
import Data
import time

crawler = Crawler.Crawler()
parser = Parser.Parser()
data = Data.Data()

data.truncate()

base_url = "https://paiza.jp"
html = crawler.crawl("https://paiza.jp/career/job_offers")

while True:
    parser.parse(html.text)
    data.insert(parser)
    next_page = parser.next()
    if next_page != "":
        time.sleep(3)
        html = crawler.crawl(base_url + next_page)
    else:
        break

del crawler
del parser
del data