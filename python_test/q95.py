import mysql.connector
try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
  )
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))
else:
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM customers")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
finally:
  mydb.close()
