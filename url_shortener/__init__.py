import sqlite3, os
from flask import Flask, render_template, url_for, redirect, g, request
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(os.path.join(app.root_path, 'links.db'))
    return db

def get_links(db: sqlite3.Connection):
    links = db.cursor().execute("SELECT original, short FROM links").fetchall()
    links = tuple(links[i] for i in range(len(links)))
    return links

@app.route('/')
def index():
    links = get_links(get_db())
    return render_template('index.html', links=links)

@app.route('/<short_url>')
def redirecter(short_url):
    original = get_db().cursor().execute("SELECT original FROM links WHERE short=?", (short_url,)).fetchone()
    if original is None:
        return url_for('index')
    else:
        original = original[0]
    # return render_template('redirect.html', short_url=short_url, original=original)
    return redirect(f"https://{original}")

@app.route('/new', methods=['POST'])
def new_link():
    original = request.form['original']
    short_url = request.form['short_url']
    get_db().cursor().execute("INSERT INTO links (original, short) VALUES (?, ?)", (original, short_url))
    get_db().commit()
    return redirect(url_for('redirecter', short_url=short_url))

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def main():
    app.run(debug=True)