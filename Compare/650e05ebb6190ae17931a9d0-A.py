import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE IF NOT EXISTS table_name (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert a record
cur.execute("INSERT INTO table_name (name, age) VALUES (?, ?)", ("John Doe", 30))

# Read all records
cur.execute("SELECT * FROM table_name")
records = cur.fetchall()

# Update a record
cur.execute("UPDATE table_name SET age = ? WHERE id = ?", (31, 1))

# Delete a record
cur.execute("DELETE FROM table_name WHERE id = ?", (1,))

# Close the cursor and connection
cur.close()
conn.close()