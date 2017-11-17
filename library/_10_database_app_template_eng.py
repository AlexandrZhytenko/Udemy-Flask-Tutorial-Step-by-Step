import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

# before_request(f)
# Registers a function to run before each request
@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def hello_world():
    # execute(sql[, parameters])
    # Executes an SQL statement
    cursor = g.db.execute('SELECT id, name, country_id FROM author;')
    authors = [dict(id=row[0], name=row[1], country=row[2]) for row in cursor.fetchall()]
    return render_template('database/authors_template_engine.html', authors=authors)