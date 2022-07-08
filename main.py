import dbcon

# Database Connection
mydb = dbcon.mydb
mycursor = mydb.cursor()

# 1. CREATE DATABASE
# mycursor.execute("CREATE DATABASE mydatabase")

# 2. Check if Database Exists
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# 3. CREATE TABLE IF NOT EXISTS  
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# 4. ALTER TABLE
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 5. SHOW TABLES
"""
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
"""
# 6. INSERT
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
"""
# 7. INSERT MULTIPLE RECORD
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
"""
# 8. INSERT ONE ROW, AND RETURN THE ID:
""" sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid) """

# 9. SELECT FROM A TABLE
# mycursor.execute("SELECT * FROM customers")
""" mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """
  
# 10. Fetch only one row:
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)





















