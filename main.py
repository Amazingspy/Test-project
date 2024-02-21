import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SQL query to create a table
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     email TEXT NOT NULL UNIQUE
#                 )''')
# print("Table created successfully")
cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''',
               ('John Doe', 'john@example.com'))
print(f"1 record inserted: {cursor.rowcount} rows affected")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
