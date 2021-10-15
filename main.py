import Crawler
import Parser
import Data
import time

crawler = Crawler.Crawler()
parser = Parser.Parser()
data = Data.Data()

data.truncate_company_name()

base_url = "https://paiza.jp"
html = crawler.crawl("https://paiza.jp/career/job_offers")
print(html.text)

while True:
    parser.parse(html.text)
    data.insert_company_name(parser.get_offer_id_list(), parser.get_company_name_list())
    next_page = parser.next(html.text)
    if next_page != "":
        time.sleep(3)
        html = crawler.crawl(base_url + next_page)
        print(html.text)
    else:
        break

del crawler
del parser
del data