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
""" mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult) """

# WHERE
""" sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

# WILDCARD CHARACTERS
""" sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

# PREVENT SQL INJECTION
""" sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

# ORDER BY
""" sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """
  
# ORDER BY DESC
""" sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

# DELETE
""" sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted") """

# DELETE PREVENT INJECTION
""" sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted") """

# DROP TABLE
""" sql = "DROP TABLE customers"
mycursor.execute(sql) """

# DROP TABLE IF EXISTS
""" sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql) """

# UPDATE TABLE
""" sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected") """

# UPDATE TABLE: PREVENT SQL INJECTION
""" sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected") """

# SELECT LIMIT
""" mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

# START FROM ANOTHER POSITION
""" mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """
  
# JOIN
""" sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """
  
# LEFT JOIN
""" sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """

# RIGHT JOIN
""" sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) """