from turtle import pos
import psycopg2
import credent as creds
import pandas as pd




## ****** LOAD PSQL DATABASE ***** ##
class PostgresManagement:
    def __init__(self):
        # Set up a connection to the postgres server.
        conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
            +" password="+ creds.PGPASSWORD
        conn=psycopg2.connect(conn_string)
        self.connection = conn
        self.cursor = conn.cursor()
        self.schema = 'public'

    def findUsers(self):
        sql_command = "SELECT * FROM users;"
        data = pd.read_sql(sql_command, self.connection)
        return data

    def findBooks(self):
        sql_command = "SELECT * FROM books;"
        data = pd.read_sql(sql_command, self.connection)
        return data
    
    def findRentals(self):
        sql_command = "SELECT * FROM rentals;"
        data = pd.read_sql(sql_command, self.connction)
        return data

    
    ### CRUD SECTION ####
    ##Create##
    def addUser(self, user):
        sql_command = 'INSERT INTO users (username,password,admin) values {}'.format(user)
        print(sql_command)
        try:
            self.cursor.execute(sql_command)
            self.connection.commit()
            print('inserted')
        except:
            self.connection.rollback()
            print('error')

if __name__ == "__main__":
    postgresDB = PostgresManagement()
    print(postgresDB.findUsers())