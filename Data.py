import DB


class Data:
    db = DB.DB()

    def __init__(self):
        self.db.open()

    def __del__(self):
        self.db.close()

    def truncate(self):
        self.db.truncate("job_list")
        self.db.truncate("occupation")
        self.db.truncate("salary_min")
        self.db.truncate("salary_max")
        self.db.truncate("location")
        self.db.truncate("environment")
        self.db.truncate("framework")

    def insert(self, parser):
        self.insert_company_name(parser.get_offer_id_list(),
                                 parser.get_company_name_list())
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
        self.db.insert("job_list", "company_name",
                       offer_id_list, company_name_list)

    def insert_occupation(self, offer_id_list, occupation_list):
        self.db.insert("occupation", "occupation",
                       offer_id_list, occupation_list)

    def insert_salary_min(self, offer_id_list, salary_min_list):
        self.db.insert("salary_min", "salary_min",
                       offer_id_list, salary_min_list)

    def insert_salary_max(self, offer_id_list, salary_max_list):
        self.db.insert("salary_max", "salary_max",
                       offer_id_list, salary_max_list)

    def insert_location(self, offer_id_list, location_list):
        self.db.insert("location", "location",
                       offer_id_list, location_list)

    def insert_environment(self, offer_id_list, environment_list):
        self.db.insert("environment", "environment",
                       offer_id_list, environment_list)

    def insert_framework(self, offer_id_list, framework_list):
        self.db.insert("framework", "framework",
                       offer_id_list, framework_list)

    def combine(self):
        sql = "SELECT \
            job_list.*, \
            occupation.occupation, \
            salary_min.salary_min, \
            salary_max.salary_max, \
            location.location, \
            environment.environment, \
            framework.framework \
        FROM \
            job_list \
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




        return self.db.combine(sql)
