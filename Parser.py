import Soup
import StringOperation


class Parser:
    def parse(self, html_text):
        soup = Soup.Soup()
        soup = soup.get_html_text(html_text)
        self.get_offer_id(soup)
        self.get_company_name(soup)
        # for each in soup.find_all("a"):
        # print(each.text)
        return

    def get_offer_id(self, soup):
        for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
            href = each.find("a").get("href")
            so = StringOperation.StringOperation()
            back = so.get_back("=", href)
            id = so.get_forward("#", back)
            print(id)

    def get_company_name(self, soup):
        for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
            print(each.find("a").text)
