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
data.truncate_company_name()
data.insert_company_name(parser.get_offer_id_list(), parser.get_company_name_list())

del data
del parser