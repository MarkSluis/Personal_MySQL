from personal_csv_lib import CsvFunc
from personal_mysql_lib import MySQL

# Test
# 1. import csv as object
pokemonfile = CsvFunc("pokemon_small.csv")
# 2. print headers
pokemonfile.get_headers_from_csv()
# 3 print lst
pokemon_lst = pokemonfile.create_list_from_csv()
print(pokemon_lst)
# print list with dict:
pokemon_lst = pokemonfile.create_dicts_from_csv()

# Test dropping and creating schemes
db = MySQL("localhost", "bitacademy", "bitacademy")
db.show_database()
db.try_to_delete_and_create_database("academy")
db.drop_database("academy")
db.try_to_delete_and_create_database("academy")

# Test creating and alter table
dct_new_table = {"id": "INT AUTO_INCREMENT PRIMARY KEY", "first_name": "VARCHAR(255)"}
dct_add_column = {"last_name": "VARCHAR(255)"}

db.create_table_in_database("academy", "persons", dct_new_table)
db.show_tables_in_database("academy")
db.add_column_in_table_in_database("academy", "persons", dct_add_column)
db.show_tables_in_database("academy")

# Test insert data in table
lst_data = [{"first_name": "Mark", "last_name": "Sluis"}, {"first_name": "Marit", "last_name": "de Boer"}, {"first_name": "Femke", "last_name": "de Boer"}, {"first_name": "Pip", "last_name": "Sluis"}, {"first_name": "Dwarrel", "last_name": "Lego"}]
db.insert_dctdata_in_list_in_table_in_database("academy", "persons", lst_data)

# Test select data
db.print_select("academy", "persons", ["first_name", "last_name"])
db.print_select("academy", "persons", "first_name")
db.print_select("academy", "persons")

# Help
db.help()
