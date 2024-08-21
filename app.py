import sqlite3

import shortuuid
from flask import Flask, request, redirect, render_template

app = Flask(__name__)


# Initialize SQLite database
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS urls (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            original_url TEXT NOT NULL,
                            short_url TEXT NOT NULL
                        );''')


init_db()


# Route for the home page where the user can shorten a URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = shortuuid.ShortUUID().random(length=6)

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
            conn.commit()

        return render_template('shortened.html', short_url=short_url)

    return render_template('index.html')


# Route for redirecting to the original URL
@app.route('/<short_url>')
def redirect_url(short_url):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT original_url FROM urls WHERE short_url = ?", (short_url,))
        result = cur.fetchone()

        if result:
            return redirect(result[0])
        else:
            return "URL not found", 404


if __name__ == '__main__':
    app.run(debug=True)
