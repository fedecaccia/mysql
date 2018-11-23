import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1111"
)

print(mydb)