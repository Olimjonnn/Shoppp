import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "12345678"
)
print(mydb)