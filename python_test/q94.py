import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT customers.name, orders.product_name FROM customers INNER JOIN orders ON customers.id = orders.customer_id")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)