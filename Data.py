import DB


class Data:
    db = DB.DB()

    def __init__(self):
        self.db.open()

    def __del__(self):
        self.db.close()

    def truncate(self):
        self.db.truncate("train_company_name")
        self.db.truncate("train_salary_min")
        self.db.truncate("train_salary_max")

    def insert_company_name(self, offer_id_list, company_name_list):
        self.db.insert("train_company_name", "company_name", offer_id_list, company_name_list)
        
    def insert_salary_min(self, offer_id_list, salary_min_list):
        self.db.insert("train_salary_min", "salary_min", offer_id_list, salary_min_list)

    def insert_salary_max(self, offer_id_list, salary_max_list):
        self.db.insert("train_salary_max", "salary_max", offer_id_list, salary_max_list)