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
    data.insert_company_name(parser.get_offer_id_list(), parser.get_company_name_list())
    data.insert_salary_min(parser.get_offer_id_list(), parser.get_salary_min_list())
    data.insert_salary_max(parser.get_offer_id_list(), parser.get_salary_max_list())
    next_page = parser.next(html.text)
    if next_page != "":
        time.sleep(3)
        html = crawler.crawl(base_url + next_page)
    else:
        break

del crawler
del parser
del data