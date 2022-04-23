import mysql.connector

class MySQL():
    def __init__(self, input_host, input_user, input_password):
        self.host = input_host
        self.user = input_user
        self.password = input_password
    def help(self):
        print("https://github.com/MarkSluis/Personal_MySQL")
    def show_database(self):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
        )
        cursor = db.cursor()
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x)
    def drop_database(self, database):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password
        )
        cursor = db.cursor()
        cursor.execute("DROP DATABASE " + database)
        print(f"Database {database} is deleted")
    def create_database(self, database):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE " + database)
        print(f"Database {database} is created")
    def try_to_delete_and_create_database(self, database):
        try:
            self.drop_database(database)
        except:
            print("Database does not exist")
        self.create_database(database)
    def show_tables_in_database(self, database):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = database
        )
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
    def create_table_in_database(self, database, table, dict_headers):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = database
        )
        cursor = db.cursor()
        string = ""
        for x, y in dict_headers.items():
            temp_string = x + " " + y + ", "
            string = string + " " + temp_string
        string = string[1:len(string) - 2]
        cursor.execute("CREATE TABLE " + table + " (" + string + ")")
        print(f"Table {table} in database {database} is created with the following headers:")
        for i in dict_headers.keys():
            print(i)
    def add_column_in_table_in_database(self, database, table, dict_column):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = database
        )
        cursor = db.cursor()
        string = ""
        for x, y in dict_column.items():
            string = x + " " + y
        cursor.execute("ALTER TABLE " + table + " ADD COLUMN " + string)
        for x in dict_column.keys():
            print(f"Column {x} is added to table {table} in database {database}")
    def insert_dctdata_in_list_in_table_in_database(self, database, table, dict_lst):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = database
        )
        cursor = db.cursor()
        for dct in dict_lst:
            placeholder = ', '.join(['%s'] * len(dct))
            columns = ', '.join(dct.keys())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholder)
            cursor.execute(sql, list(dct.values()))
        print(f"Data is added to {table} in database {database}")
        db.commit()


    def print_select(self, database, table, select_column = "*"):
        db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = database
        )
        cursor = db.cursor()
        if type(select_column) == str:
            cursor.execute("SELECT " + select_column + " FROM " + table)
        elif type(select_column) == list:
            temp_str = ""
            for i in select_column:
                temp_str += i + ", "
            cursor.execute("SELECT " + temp_str[:-2] + " FROM " + table)
        result = cursor.fetchall()
        print("The query is executed and returned: ")
        print(result)
        return result











