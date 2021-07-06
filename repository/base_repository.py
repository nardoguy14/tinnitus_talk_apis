import mysql.connector
from config import AppSettings

class BaseRepository(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=AppSettings.get_settings().mysql_host,
            user=AppSettings.get_settings().mysql_user,
            password=AppSettings.get_settings().mysql_password,
            database=AppSettings.get_settings().mysql_db
        )
        self.cursor = self.mydb.cursor()


    def __enter__(self):
        return self.cursor

    def __exit__(self, a, b, c):
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()
