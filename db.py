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
