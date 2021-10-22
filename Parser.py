import Soup
import StringOperation
import Token
from statistics import median

class Parser:
    soup = Soup.Soup()
    parse_tree = ""
    so = StringOperation.StringOperation()
    token = Token.Token()
    offer_id_list = []
    company_name_list = []
    occupation_list = []
    salary_min_list = []
    salary_max_list = []

    def __init__(self):
        self.soup = Soup.Soup()
        self.parse_tree =""
        self.so = StringOperation.StringOperation()
        self.token = Token.Token()
        self.offer_id_list = []
        self.company_name_list = []
        self.occupation_list = []
        self.salary_min_list = []
        self.salary_max_list = []        

    def __del__(self):
        del self.soup
        del self.parse_tree
        del self.so
        del self.token
        del self.offer_id_list
        del self.company_name_list
        del self.occupation_list
        del self.salary_min_list
        del self.salary_max_list        

    def parse(self, html_text): 
        self.parse_tree = self.soup.markup(html_text)
        self.get_offer_id()
        self.get_company_name()
        self.get_occupation()
        self.get_salary_min()
        self.get_salary_max()
        return

    def next(self):
        tag = self.parse_tree.find("a", {"rel":'next'})
        if(tag != None):
            return tag.get("href")
        else:
            return ""

    def get_offer_id(self):
        self.offer_id_list = []
        for each in self.parse_tree.find_all("h4", class_="c-job_offer-recruiter__name"):
            href = each.find("a").get("href")
            forward = self.so.get_forward("=", href)
            id = self.so.get_back("#", forward).strip()
            self.offer_id_list.append(id)

    def get_offer_id_list(self):
        return self.offer_id_list

    def get_company_name(self):
        for each in self.parse_tree.find_all("h4", class_="c-job_offer-recruiter__name"):
            company_name = each.find("a").text.strip()
            self.company_name_list.append(company_name)

    def get_company_name_list(self):
        return self.company_name_list

    def get_occupation(self):
        for each in self.parse_tree.find_all("div", class_="c-job_offer-detail__occupation"):
            occupation = each.text.strip()
            print(occupation)
            part_of_speech_list = ["名詞"]
            pos_occupation = self.token.get_part_of_speech(part_of_speech_list, occupation)
            print(pos_occupation)
            reunion = []
            for each in pos_occupation:
                removed_punctuation = self.so.remove_punctuation(each)
                removed_prefecture = self.so.remove_prefecture(removed_punctuation)
                removed_region = self.so.remove_region(removed_prefecture)
                removed_city = self.so.remove_city(removed_region)
                reunion.append(removed_city)
            self.occupation_list.append(''.join(reunion))
            print(''.join(reunion))

    def get_occupation_list(self):
        return self.occupation_list

    def get_salary_min(self):
        for each in self.parse_tree.find_all("strong", class_="c-job_offer-detail__salary"):
            min = ""
            min = self.so.get_back("万 〜", each.text)
            if(min == ""):
                min = self.so.get_back("万円 〜", each.text)
            if(min == ""):
                min = self.so.get_back("万円", each.text)
            if(min == ""):
                min = "425"                
            min = self.so.replace(",", "", str(min)).strip()
            self.salary_min_list.append(int(min))

    def get_salary_min_list(self):
        return self.salary_min_list

    def get_salary_max(self):
        for each in self.parse_tree.find_all("strong", class_="c-job_offer-detail__salary"): 
            max = ""
            forward = self.so.get_forward("〜 ", each.text)
            if(forward != ""):
                max = self.so.get_back("万円", forward)
            if (max == ""):
                max = "556"
            max = self.so.replace(",", "", str(max)).strip()
            self.salary_max_list.append(int(max))

    def get_salary_max_list(self):
        return self.salary_max_list