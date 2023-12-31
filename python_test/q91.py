import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE ")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mydb.close()