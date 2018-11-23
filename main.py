import mysql.connector
from mysql.connector.errors import DatabaseError, ProgrammingError

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1111",
    # database="mydatabase"
)

print(mydb)

# Create a database

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE mydatabase")
except DatabaseError:
    print("DB already exists")

# Check if database Exists

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# CREATE TABLE

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1111",
  database="mydatabase"
)


# To understand buffered see: https://stackoverflow.com/questions/46682012/what-is-a-mysql-buffered-cursor-w-r-t-python-mysql-connector
mycursor = mydb.cursor(buffered=True)
try:    
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
except DatabaseError:
    print("DB already exists")

# Check if table exists

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# ALTER TABLE primary key on an existing table
try:
    mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
except ProgrammingError:
    print("Table already has id property.")

# INSERT in table

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
# commit() is required to make the changes, otherwise no changes are made to the table.
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

# SELECT from table

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# The fetchone() method will return the first row of the result:
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# SELECT WHERE

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# sql = "SELECT * FROM customers WHERE name ='John'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Wildcad characters
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Prevent SQL Injection

# When query values are provided by the user, you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# Escape query values by using the placholder %s method:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x) 
