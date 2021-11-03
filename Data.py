import DB
import pandas as pd


class Data:
    db = DB.DB()
    job_list = "job_list"
    offer_id = "offer_id"
    company_name = "company_name"
    path_rank = "path_rank"
    occupation = "occupation"
    salary_min = "salary_min"
    salary_max = "salary_max"
    location = "location"
    environment = "environment"
    framework = "framework"

    def __init__(self):
        self.db.open()

    def __del__(self):
        self.db.close()

    def truncate(self):
        self.db.truncate(self.job_list)
        self.db.truncate(self.path_rank)
        self.db.truncate(self.occupation)
        self.db.truncate(self.salary_min)
        self.db.truncate(self.salary_max)
        self.db.truncate(self.location)
        self.db.truncate(self.environment)
        self.db.truncate(self.framework)

    def insert(self, parser):
        self.insert_company_name(parser.get_offer_id_list(),
                                 parser.get_company_name_list())
        self.insert_rank(parser.get_offer_id_list(),
                         parser.get_path_rank_list())
        self.insert_occupation(parser.get_offer_id_list(),
                               parser.get_occupation_list())
        self.insert_salary_min(parser.get_offer_id_list(),
                               parser.get_salary_min_list())
        self.insert_salary_max(parser.get_offer_id_list(),
                               parser.get_salary_max_list())
        self.insert_location(parser.get_offer_id_list(),
                             parser.get_location_list())
        self.insert_environment(parser.get_offer_id_list(),
                                parser.get_environment_list())
        self.insert_framework(parser.get_offer_id_list(),
                              parser.get_framework_list())

    def insert_company_name(self, offer_id_list, company_name_list):
        self.db.insert(self.job_list, self.company_name,
                       offer_id_list, company_name_list)

    def insert_rank(self, offer_id_list, rank_list):
        self.db.insert(self.path_rank, self.path_rank,
                       offer_id_list, rank_list)

    def insert_occupation(self, offer_id_list, occupation_list):
        self.db.insert(self.occupation, self.occupation,
                       offer_id_list, occupation_list)

    def insert_salary_min(self, offer_id_list, salary_min_list):
        self.db.insert(self.salary_min, self.salary_min,
                       offer_id_list, salary_min_list)

    def insert_salary_max(self, offer_id_list, salary_max_list):
        self.db.insert(self.salary_max, self.salary_max,
                       offer_id_list, salary_max_list)

    def insert_location(self, offer_id_list, location_list):
        self.db.insert(self.location, self.location,
                       offer_id_list, location_list)

    def insert_environment(self, offer_id_list, environment_list):
        self.db.insert(self.environment, self.environment,
                       offer_id_list, environment_list)

    def insert_framework(self, offer_id_list, framework_list):
        self.db.insert(self.framework, self.framework,
                       offer_id_list, framework_list)

    def combine(self):
        sql = "SELECT \
            job_list.*, \
            path_rank.path_rank, \
            occupation.occupation, \
            salary_min.salary_min, \
            salary_max.salary_max, \
            location.location, \
            environment.environment, \
            framework.framework \
        FROM \
            job_list \
        LEFT JOIN \
            path_rank \
        ON \
            job_list.offer_id = path_rank.offer_id \
        LEFT JOIN \
            occupation \
        ON \
            job_list.offer_id = occupation.offer_id \
        LEFT JOIN \
            salary_min \
        ON \
            job_list.offer_id = salary_min.offer_id \
        LEFT JOIN \
            salary_max \
        ON \
            job_list.offer_id = salary_max.offer_id \
        LEFT JOIN \
            location \
        ON \
            job_list.offer_id = location.offer_id \
        LEFT JOIN \
            environment \
        ON \
            job_list.offer_id = environment.offer_id \
        LEFT JOIN \
            framework \
        ON \
            job_list.offer_id = framework.offer_id"
        rows = self.db.combine(sql)

        new_result = [one for one in rows]
        dataset = pd.DataFrame(new_result)
        dataset.columns = [self.offer_id, self.company_name, self.occupation,
                           self.salary_min, self.salary_max, self.location, self.environment, self.framework]
        return dataset

    def output_csv(self, dataframe):
        dataframe.to_csv("sample.csv")
