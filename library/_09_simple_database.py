import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)

# class sqlite3.Connection
# https://docs.python.org/2/library/sqlite3.html
# A SQLite database connection

# class flask.Config(root_path, defaults=None)
# Works exactly like a dict but provides ways to fill it from files or special dictionarie
def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.route('/')
def hello_world():
    db_connection = connect_db()
    # execute(sql[, parameters])
    # https://docs.python.org/2/library/sqlite3.html
    # This is a nonstandard shortcut that creates an intermediate cursor object by
    # calling the cursor method
    # The SELECT statement is used to select data from a database
    cursor = db_connection.execute('SELECT id, name FROM author;')

    # class sqlite3.Cursor
    # fetchall()
    # Fetches all(remaining) rows of a query result, returning a list.
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('database/authors.html', authors=authors)
