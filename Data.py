import DB


class Data:
    db = DB.DB()

    def __init__(self):
        self.db.open()

    def __del__(self):
        self.db.close()

    def insert_company_name(self, offer_id_list, company_name_list):
        self.db.insert("train_company_name", "offer_id", "company_name", offer_id_list, company_name_list)
        
    def truncate_company_name(self):
        self.db.truncate("train_company_name")

