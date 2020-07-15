import sqlite3

class Database:
    dbname = "sensehat.db"

    @staticmethod
    def select_record(columns, tb_name, extra = ""):
        conn = sqlite3.connect(Database.dbname)
        curs = conn.cursor()
        return_value = curs.execute("SELECT " 
                                    + columns 
                                    + " FROM "
                                    + tb_name
                                    + extra)
        conn.close()
        return return_value

    @staticmethod
    def display_db():
        conn = sqlite3.connect(Database.dbname)
        curs = conn.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SenseHat_data"):
            print (row)
        conn.close()

    @staticmethod
    def insert_record(tb_name, values, parameters):
        conn = sqlite3.connect(Database.dbname)
        curs = conn.cursor()
        curs.execute("INSERT INTO " + tb_name + " values" + values, parameters)
        conn.close()
        Database.display_db()

    @staticmethod
    def create_tb(tb_name, columns):
        conn = sqlite3.connect(Database.dbname)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS "+ tb_name)
        cur.execute("CREATE TABLE " + tb_name + columns)
        conn.close()
