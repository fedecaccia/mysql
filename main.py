import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1111"
)

print(mydb)

# Create a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists