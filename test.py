import sqlite3
connection =sqlite3.connect('data.db')

cursor=connection.cursor()
# cursor  responsible  for  executing  a query    ;   

create_table="CREATE TABLE users (id INTEGER PRIMARY KEY , username  text , password text)"
cursor.execute(create_table)

user=(1,'param','abcd')
insert_query  =  "INSERT INTO users  VALUES (? , ? , ? )"
cursor.execute(insert_query,user)

# list of tuples  
users=[
    (2,'kaajal','abcd'),
    (3,'heena','abcd')
]
cursor.executemany(insert_query,users)

select_query="Select * from users"

for row in cursor.execute(select_query):
    print(row)

connection.commit();

connection.close();


