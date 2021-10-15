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

    def insert(self, table_name, col_name1, col_name2, list1, list2):
        sql = "INSERT INTO " + table_name + " (" + col_name1 + ", " + col_name2 + ") VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            for item1, item2 in zip(list1, list2):
                r = cursor.execute(sql, (item1, item2))
                self.connection.commit()

    def truncate(self, table_name):
        sql = "TRUNCATE TABLE " + table_name
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
                

