import Soup
import StringOperation


class Parser:
    offer_id_list = []
    company_name_list = []

    def __init__(self):
        self.offer_id_list = []
        self.company_name_list = []

    def __del__(self):
        del self.offer_id_list
        del self.company_name_list

    def parse(self, html_text):
        soup = Soup.Soup()
        text = soup.markup(html_text)
        self.get_offer_id(text)
        self.get_company_name(text)
        # for each in soup.find_all("a"):
        # print(each.text)
        return

    def get_offer_id(self, soup):
        self.offer_id_list = []
        for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
            href = each.find("a").get("href")
            so = StringOperation.StringOperation()
            back = so.get_back("=", href)
            id = so.get_forward("#", back)
            self.offer_id_list = id
            print(id)

    def get_offer_id_list(self):
        return self.offer_id_list

    def get_company_name(self, soup):
        for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
            company_name = each.find("a").text
            self.company_name_list = company_name
            print(company_name)

    def get_company_name_list(self):
        return self.company_name_list
