import sqlite3

class Database:
    db_name = "sensehat.db"
<<<<<<< HEAD

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
=======
    tb_name = "SENSEHAT_data"
    conn = None
    curs = None

    @staticmethod
    def setup_connection(tb_name = Database.tb_name, db_name = Database.db_name):
        Database.db_name = db_name
        Database.tb_name = tb_name
        Database.conn = sqlite3.connect(Database.db_name)
        Database.curs = Database.conn.cursor()  

    @staticmethod
    def execute_equation(equation, extra = "", tb_name = Database.tb_name, db_name = Database.db_name):
        Database.setup_connection()
        value = Database.curs.execute(
            "SELECT" 
            + equation
            + "FROM"
            + Database.tb_name
            + extra
        )
        Database.conn.close()
        return value
        
    @staticmethod
    def select_a_record(columns, extra = "", tb_name = Database.tb_name, db_name = Database.db_name):
        Database.setup_connection()
        rows = Database.curs.execute(
            "SELECT" 
            + columns 
            + "FROM"
            + Database.tb_name
            + extra
        )
>>>>>>> context
        for row in rows:
            return_value = row
        Database.conn.close()
        return return_value

    # @staticmethod
    # def display_db():
    #     conn = sqlite3.connect("sensehat.db")
    #     curs = conn.cursor()
    #     print ("\nEntire database contents:\n")
    #     for row in curs.execute("SELECT * FROM SENSEHAT_data"):
    #         print (row)
    #     conn.close()
<<<<<<< HEAD

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
    
=======

    @staticmethod
    def insert_record(values, parameters, tb_name = Database.tb_name, db_name = Database.db_name):
        Database.setup_connection()      
        Database.curs.execute("INSERT INTO " + Database.tb_name + " values" + values, parameters)
        Database.conn.commit()
        Database.conn.close()
        # Database.display_db()

    @staticmethod
    def create_tb(columns, tb_name = Database.tb_name, db_name = Database.db_name):
        Database.setup_connection()
        Database.curs.execute("DROP TABLE IF EXISTS "+ Database.tb_name)
        Database.curs.execute("CREATE TABLE " + Database.tb_name + columns)
        Database.conn.close()

    @staticmethod
    def update_last_record(column, parameter, tb_name = Database.tb_name, db_name = Database.db_name):
        Database.setup_connection()
        Database.curs.execute(
            "UPDATE " 
            + Database.tb_name 
            + " set " 
            + column
            + " = (?)" 
            + "WHERE timestamp = "
            + Database.execute_equation("MAX(timestamp)")
            , parameter
        )
        Database.conn.commit()
        Database.conn.close()
          
>>>>>>> context
