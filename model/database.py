import sqlite3

class Database:
    db_name = "sensehat.db"

    @staticmethod
    def select_a_record(columns, tb_name, extra = "", db_name = Database.db_name):
        Database.db_name = db_name
        conn = sqlite3.connect(Database.db_name)
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

    # @staticmethod
    # def display_db():
    #     conn = sqlite3.connect("sensehat.db")
    #     curs = conn.cursor()
    #     print ("\nEntire database contents:\n")
    #     for row in curs.execute("SELECT * FROM SENSEHAT_data"):
    #         print (row)
    #     conn.close()

    @staticmethod
    def insert_record(tb_name, values, parameters, db_name = Database.db_name):
        Database.db_name = db_name
        conn = sqlite3.connect(Database.db_name)
        curs = conn.cursor()        
        curs.execute("INSERT INTO " + tb_name + " values" + values, parameters)
        conn.commit()
        conn.close()
        # Database.display_db()

    @staticmethod
    def create_tb(tb_name, columns, db_name = Database.db_name):
        Database.db_name = db_name
        conn = sqlite3.connect(Database.db_name)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS "+ tb_name)
        cur.execute("CREATE TABLE " + tb_name + columns)
        conn.close()
    
