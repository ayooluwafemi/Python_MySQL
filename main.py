import dbcon

mydb = dbcon.mydb
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")