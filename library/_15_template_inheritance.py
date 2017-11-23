from flask import Flask, request, render_template
import sqlite3
# https://docs.python.org/2/library/sqlite3.html
from . import config

app = Flask(__name__)

# to create a Connection object that represents our database
# sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements])
# Opens a connection to the SQLite database file database
def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('inheritance/child_template_form.html')
    elif request.method == 'POST':
        db = connect_db()
        # The INSERT INTO statement is used to insert new records in a table
        sql_query = """
            INSERT INTO book ("title", "isbn", "author_id") VALUES (:title, :isbn, :author_id);
        """
        # execute(sql[, parameters])
        # This is a nonstandard shortcut that creates an intermediate cursor object
        # by calling the cursor method
        # Executes an SQL statement
        db.execute(sql_query, {
            'title': request.form['title'],
            'isbn': request.form['isbn'],
            'author_id': int(request.form['author']),
        })
        db.commit()
        return "The new book {} was correctly saved".format(request.form['title'])