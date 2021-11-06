import Crawler
import Parser
import Data
import time
import File
import datetime

crawler = Crawler.Crawler()
parser = Parser.Parser()
data = Data.Data()
file = File.File()

data.truncate()

base_url = "https://paiza.jp"
html = crawler.crawl("https://paiza.jp/career/job_offers")
#file.write_html(html.text)

# データパース
parser.parse(html.text)
data.insert(parser)
print("[", datetime.datetime.now().isoformat(), "]", "Progress:", "  1 / {:3d}".format(parser.get_last_page()))
next_page = parser.next()

while True:
    if next_page != "":
        time.sleep(1)
        html = crawler.crawl(base_url + next_page)
        #file.write_html(html.text)
        parser.parse(html.text)
        data.insert(parser)
        print("[", datetime.datetime.now().isoformat(), "]", "Progress:", "{:3d} / {:3d}".format(parser.get_next_page(), parser.get_last_page()))
        next_page = parser.next()
    else:
        break

del file
del crawler
del parser
del data