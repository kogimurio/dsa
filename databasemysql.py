import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="kogi@murio",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS products"

mycursor.execute(sql)
print('Table dropped')



