#sqlite is already install on python so doesn't have to be installed on sqlite
import sqlite3 

# this creates a sql connection
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

drop_table = "DROP TABLE users"
cursor.execute(drop_table)

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', '1234')
insert_query = "INSERT INTO users values (?,?,?)"
cursor.execute(insert_query,user)

users = [
    (2, 'rolf', '1235'),
    (3, 'anne', '1236')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()