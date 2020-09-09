import sqlite3
import pathlib

"""
Class Database is to create and connect to the data for recording and retrieving data
"""

class Database:
    db_path = pathlib.Path(__file__).parent.parent / "database" / "sensehat.db"
    tb_name = "SENSEHAT_data"
    conn = None
    curs = None


    #Connect to database
    @staticmethod
    def setup_connection(tb_name, db_path):
        if db_path != None:
            Database.db_path = db_path
        if tb_name != None:
            Database.tb_name = tb_name
        Database.conn = sqlite3.connect(Database.db_path)
        Database.curs = Database.conn.cursor()  

    #Retrieve data by equation
    @staticmethod
    def execute_equation(equation, extra = "", tb_name = None, db_path = None):
        Database.setup_connection(tb_name, db_path)
        rows = Database.curs.execute(
            "SELECT " 
            + equation
            + " FROM "
            + Database.tb_name
            + extra)
        for row in rows:
            return_value = row
        Database.conn.close()
        return return_value[0]
        
    #Retrieve data of one record
    @staticmethod
    def select_a_record(columns, extra = "", tb_name = None, db_path = None):
        Database.setup_connection(tb_name, db_path)
        rows = Database.curs.execute(
            "SELECT " 
            + columns 
            + " FROM "
            + Database.tb_name
            + extra
        )
        for row in rows:
            return_value = row
        Database.conn.close()
        return return_value

    #Insert data record by record
    @staticmethod
    def insert_record(values, parameters, tb_name = None, db_path = None):
        Database.setup_connection(tb_name, db_path)      
        Database.curs.execute("INSERT INTO " + Database.tb_name + " values" + values, parameters)
        Database.conn.commit()
        Database.conn.close()

    #Create a new table
    @staticmethod
    def create_table(columns, tb_name = None, db_path = None):
        Database.setup_connection(tb_name, db_path)
        Database.curs.execute("DROP TABLE IF EXISTS "+ Database.tb_name)
        Database.curs.execute("CREATE TABLE " + Database.tb_name + columns)
        Database.conn.close()

    #Update the lastet record in the database
    @staticmethod
    def update_last_record(column, parameter, tb_name = None, db_path = None):
        timestamp = Database.execute_equation("MAX(timestamp)")
        Database.setup_connection(tb_name, db_path)
        Database.curs.execute(
            "UPDATE " 
            + Database.tb_name 
            + " set " 
            + column
            + " = (?) WHERE timestamp = '"
            + timestamp
            + "'"
            , parameter
        )
        Database.conn.commit()
        Database.conn.close()
