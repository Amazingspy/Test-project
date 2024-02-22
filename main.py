import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Insert data into the table
cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''',
               ('Joe', 'joe@example.com'))
print(f"1 record inserted: {cursor.rowcount} rows affected")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
