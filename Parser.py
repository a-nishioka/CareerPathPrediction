from io import TextIOWrapper
from File import File
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
    pass_rank_list = []
    occupation_list = []
    salary_min_list = []
    salary_max_list = []
    location_list = []
    environment_list = []
    framework_list = []
    last_page = 0
    next_page = 0
    f = TextIOWrapper

    def __init__(self):
        self.soup = Soup.Soup()
        self.parse_tree = ""
        self.so = StringOperation.StringOperation()
        self.token = Token.Token()
        self.offer_id_list = []
        self.company_name_list = []
        self.pass_rank_list = []
        self.occupation_list = []
        self.salary_min_list = []
        self.salary_max_list = []
        self.location_list = []
        self.environment_list = []
        self.framework_list = []
        self.last_page = 0
        self.next_page = 0
        self.f = open("Occupation.txt", 'w', encoding='UTF-8')

    def __del__(self):
        del self.soup
        del self.parse_tree
        del self.so
        del self.token
        del self.offer_id_list
        del self.company_name_list
        del self.pass_rank_list
        del self.occupation_list
        del self.salary_min_list
        del self.salary_max_list
        del self.location_list
        del self.environment_list
        del self.framework_list
        del self.last_page
        del self.next_page
        self.f.close()

    def parse(self, html_text):
        self.parse_tree = self.soup.markup(html_text)
        if self.last_page == 0:
            self.get_last_page_num()
        self.get_offer_id()
        self.get_company_name()
        self.get_pass_rank()
        self.get_occupation()
        self.get_salary_min()
        self.get_salary_max()
        self.get_location()
        self.get_environment()
        self.get_framework()
        return

    def next(self):
        tag = self.parse_tree.find("a", {"rel": 'next'})
        if(tag != None):
            num = int(self.so.get_forward("=", tag.get("href")))
            if(num > self.next_page):
                self.next_page = num
            return tag.get("href")
        else:
            return ""

    def get_next_page(self):
        return self.next_page

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
        self.company_name_list = []
        for each in self.parse_tree.find_all("h4", class_="c-job_offer-recruiter__name"):
            company_name = each.find("a").text.strip()
            self.company_name_list.append(company_name)

    def get_company_name_list(self):
        return self.company_name_list

    def get_pass_rank(self):
        self.pass_rank_list = []
        for each in self.parse_tree.find_all("div", class_="c-job_offer-box__header-rank-wrap"):
            pass_rank = each.find("span").text.strip()
            self.pass_rank_list.append(str(pass_rank))

    def get_pass_rank_list(self):
        return self.pass_rank_list

    def get_occupation(self):
        self.occupation_list = []
        for each1 in self.parse_tree.find_all("div", class_="c-job_offer-detail__occupation"):
            occupation = each1.text.strip()
            occupation = self.so.replace('・', ' ', occupation)
            occupation = self.so.replace('／', ' ', occupation)
            occupation = self.so.replace('/', ' ', occupation)
            occupation = self.so.replace('シニア', '', occupation)
            part_of_speech_list = ["名詞"]
            pos_occupation = self.token.get_part_of_speech(part_of_speech_list, occupation)
            reunion = []
            for each2 in pos_occupation:
                occupation = self.so.remove_punctuation(each2)
                occupation = self.so.remove_prefecture(occupation)
                occupation = self.so.remove_region(occupation)
                occupation = self.so.remove_city(occupation)
                occupation = self.so.remove_language(occupation)
                occupation = self.so.remove_framework(occupation)
                occupation = self.so.remove_position(occupation)
                occupation = self.so.remove_hiragana(occupation)
                occupation = occupation.upper()
                occupation = self.so.remove_stop_word(occupation)
                if(occupation != ""):
                    self.f.write(str(occupation + "\n"))
                    reunion.append(occupation)
            result = ""
            result = self.so.replace(" ", "", ''.join(reunion)).strip()
            # 職種リストの中に定義されている職種を見つけたら、","を挿入する
            for each3 in self.so.occupation_list:
                if((result.find(each3) != -1) and ((result.find(each3) + len(each3)) < len(result))):
                    result = self.so.replace(each3, each3 + ",", result, 1).strip()
                    next
            if(result == ""):
                self.occupation_list.append("エンジニア")
            else:
                result = self.so.replace(",,", ",", result)
                self.occupation_list.append(result)
            print(result)
            
                
    def get_occupation_list(self):
        return self.occupation_list

    def get_salary_min(self):
        self.salary_min_list = []
        for each in self.parse_tree.find_all("strong", class_="c-job_offer-detail__salary"):
            min = ""
            min = self.so.get_back("万 〜", each.text)
            if(min == ""):
                min = self.so.get_back("万円 〜", each.text)
            if(min == ""):
                min = self.so.get_back("万円", each.text)
            min = self.so.replace(",", "", str(min)).strip()
            if(min == ""):
                min = 0
            self.salary_min_list.append(int(min))

    def get_salary_min_list(self):
        return self.salary_min_list

    def get_salary_max(self):
        self.salary_max_list = []
        for each in self.parse_tree.find_all("strong", class_="c-job_offer-detail__salary"):
            max = ""
            max = self.so.get_forward("〜 ", each.text)
            if(max != ""):
                max = self.so.get_back("万円", max)
            max = self.so.replace(",", "", str(max)).strip()
            if(max == ""):
                max = 0
            self.salary_max_list.append(int(max))

    def get_salary_max_list(self):
        return self.salary_max_list

    def get_location(self):
        self.location_list = []
        keys = self.parse_tree.find_all(
            "span", class_="c-job_offer-detail__term-text")
        values = self.parse_tree.find_all(
            "td", class_="c-job_offer-detail__description")
        for key, value in zip(keys, values):
            if(key.text.strip() == "勤務地"):
                part_of_speech_list = ["名詞"]
                address = self.token.get_part_of_speech(
                    part_of_speech_list, value.text)
                if len(address) > 0:
                    self.location_list.append(str(address[0]))
                    next

    def get_location_list(self):
        return self.location_list

    def get_environment(self):
        self.environment_list = []
        keys = self.parse_tree.find_all(
            "span", class_="c-job_offer-detail__term-text")
        values = self.parse_tree.find_all(
            "td", class_="c-job_offer-detail__description")
        for key, value in zip(keys, values):
            if(key.text.strip() == "開発環境"):
                languages = []
                for each in value.find_all("a", class_="c-job_offer-detail__description-link"):
                    languages.append(each.text)
                self.environment_list.append(str(','.join(languages)))

    def get_environment_list(self):
        return self.environment_list

    def get_framework(self):
        self.framework_list = []
        keys = self.parse_tree.find_all(
            "span", class_="c-job_offer-detail__term-text")
        values = self.parse_tree.find_all(
            "td", class_="c-job_offer-detail__description")
        for key, value in zip(keys, values):
            if(key.text.strip() == "フレームワーク"):
                frameworks = []
                for each in value.find_all("a", class_="c-job_offer-detail__description-link"):
                    frameworks.append(each.text)
                self.framework_list.append(str(','.join(frameworks)))

    def get_framework_list(self):
        return self.framework_list

    def get_last_page_num(self):
        for each in self.parse_tree.find_all("a", class_="c-pager-link"):
            num = int(self.so.get_forward("=", each.get("href")))
            if(num > self.last_page):
                self.last_page = num

    def get_last_page(self):
        return self.last_page
