import pymysql


class DB:
    connection = pymysql.Connection

    def open(self):
        # データベースに接続します。
        self.connection = pymysql.connect(
            host='localhost',
            user='user1',
            passwd='user1',
            db='job_list',
            charset='utf8')

    def close(self):
        self.connection.close()
