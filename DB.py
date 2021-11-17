import pymysql


class DB:
    connection = pymysql.Connection

    def open(self):
        print("DB.open")
        self.connection = pymysql.connect(
            host='localhost',
            user='user1',
            passwd='user1',
            db='job_list',
            charset='utf8')

    def close(self):
        print("DB.close")
        self.connection.close()

    def insert(self, table_name, col_name, list1, list2):
        sql = "INSERT IGNORE INTO " + table_name + " ( offer_id, " + col_name + ") VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            for item1, item2 in zip(list1, list2):
                cursor.execute(sql, (item1, item2))
                self.connection.commit()

    def truncate(self, table_name):
        sql = "TRUNCATE TABLE " + table_name
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
    
    def combine(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows