import sqlite3

class Database:
    db_path = "sensehat.db"

    @staticmethod
    def select_a_record(columns, tb_name, extra = ""):
        conn = sqlite3.connect("sensehat.db")
        curs = conn.cursor()
        rows = curs.execute("SELECT " 
                            + columns 
                            + " FROM "
                            + tb_name
                            + extra)
        for row in rows:
            return_value = row
        conn.close()
        return return_value

    @staticmethod
    def display_db():
        conn = sqlite3.connect("sensehat.db")
        curs = conn.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SENSEHAT_data"):
            print (row)
        conn.close()

    @staticmethod
    def insert_record(tb_name, values, parameters):
        conn = sqlite3.connect("sensehat.db")
        curs = conn.cursor()        
        curs.execute("INSERT INTO " + tb_name + " values" + values, parameters)
        conn.commit()
        conn.close()
        Database.display_db()

    @staticmethod
    def create_tb(tb_name, columns):
        conn = sqlite3.connect("sensehat.db")
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS "+ tb_name)
        cur.execute("CREATE TABLE " + tb_name + columns)
        conn.close()