
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

def init_db():
    conn = sqlite3.connect('bookmarks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS folders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            parent_id INTEGER,
            user_id INTEGER
        )''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            description TEXT,
            content TEXT,
            folder_id INTEGER,
            user_id INTEGER
        )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            session['username'] = username
            return redirect(url_for('home'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already exists"
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/bookmarks', methods=['GET'])
def get_bookmarks():
    if 'user_id' not in session:
        return jsonify([])
    query = request.args.get('q', '')
    conn = sqlite3.connect('bookmarks.db')
    c = conn.cursor()
    if query:
        c.execute("SELECT id, title, url, description FROM links WHERE user_id = ? AND (title LIKE ? OR content LIKE ?)", 
                  (session['user_id'], f'%{query}%', f'%{query}%'))
    else:
        c.execute("SELECT id, title, url, description FROM links WHERE user_id = ?", (session['user_id'],))
    bookmarks = c.fetchall()
    conn.close()
    return jsonify(bookmarks)

@app.route('/api/bookmark', methods=['POST'])
def add_bookmark():
    if 'user_id' not in session:
        return jsonify({'status': 'unauthorized'}), 403
    data = request.get_json()
    conn = sqlite3.connect('bookmarks.db')
    c = conn.cursor()
    c.execute("INSERT INTO links (title, url, description, content, folder_id, user_id) VALUES (?, ?, ?, ?, ?, ?)",
              (data['title'], data['url'], data['description'], data.get('content', ''), data.get('folder_id'), session['user_id']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
