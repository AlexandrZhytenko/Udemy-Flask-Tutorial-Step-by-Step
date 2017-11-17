"""Raising custom erros.
Sometimes users will perform invalid actions
(either intentionally, or unintentionally)
In order to protect our application and also inform the user about her
mistake, we'll need to raise custom errors.
The HTTP protocol support error responses with different
status codes. For example:
* 4XX: Client Error.
       These errors are caused by user's fault. The user tried to perform
       an invalid operation, forgot to send some data, etc.
* 5XX: Server Error.
       These are errors generated in our end. The error was produced
       in the server.
If we're raising an error after a user's action, we'll probably raise a `4XX`.
The most common `4XX` errors are:
* 404 (Not Found): Resource not found
* 400 (Bad Request): A general error. Used for example if the user forgets
                     to submit important data.
* 401 (Unauthorized): The user hasn't been authorized to access this resource.
                      Usually, will need to perform some type of authentication
* 403 (Forbidden): Similar to 401, but in this case the server knows who
                   the user is, but that user is not allowed to access
                   that resource. Usually an unprivileged user is trying to
                   perform admin actions.
Useful Resources:
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error
"""

from flask import Flask

# flask.render_template(template_name_or_list, **context)
# Renders a template from the template folder with the given context

# flask.abort()
# http://flask.pocoo.org/docs/0.12/api/#flask.abort
# When passed a dict of code exception items it can be used as callable that raises exceptions
from flask import render_template, abort

app = Flask(__name__)

AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Edgar_Allan_Poe_daguerreotype_crop.png/300px-Edgar_Allan_Poe_daguerreotype_crop.png'
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Borges_1921.jpg'
    }
}

@app.route('/')
def authors():
    return render_template('routing/authors.html')

@app.route('/author/<string:authors_last_name>')
def author(authors_last_name):
    if authors_last_name not in AUTHORS_INFO:
        abort(404)
    return render_template('routing/author.html',
                           author=AUTHORS_INFO[authors_last_name])

@app.route('/author/<string:authors_last_name>/edit')
def author_admin(authors_last_name):
    abort(401)

# errorhandler(code_or_exception)
# http://flask.pocoo.org/docs/0.12/api/#flask.Flask.errorhandler
# A decorator that is used to register a function given an error code
@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html'), 404


