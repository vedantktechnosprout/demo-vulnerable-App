from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        username = request.form['username']
        # VULNERABLE: Direct string concatenation for SQLi
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE name = '{username}'"  # Exploitable e.g., ' OR 1=1 --
        c.execute(query)
        results = c.fetchall()
        conn.close()
    return render_template('index.html', results=results)  # Now passes to template for XSS demo

if __name__ == '__main__':
    import os
    if not os.path.exists('users.db'):
        exec(open('database.py').read())  # Run DB init if needed
    app.run(host='0.0.0.0', port=5000, debug=True)  # Exposes all interfaces
