import pymysql

def db_connect():
    # データベースに接続します。
    connection = pymysql.connect(
        host='localhost',
        user='user1',
        passwd='user1',
        db='job_list',
        charset='utf8')

    connection.close()