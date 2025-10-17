import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
c.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
c.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
conn.commit()
conn.close()
