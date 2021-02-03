import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="password123")
print("mydb")
if(mydb):
    print("connected successfully")
else:
    print("connection unsuccessfull")