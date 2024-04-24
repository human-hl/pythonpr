# import sqlite3 as sq 
# print("1")
# connection = sq.connect('Users.db')
# cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# password TEXT NOT NULL
# )
# ''')

# # cursor.execute('INSERT INTO Users (username, email, password ) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', '12345'))

# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()

# for user in users:
#   print(user)

# connection.commit()
# connection.close()
