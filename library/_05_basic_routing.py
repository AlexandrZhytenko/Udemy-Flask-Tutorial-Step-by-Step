from flask import Flask
from flask import render_template

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

@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    return render_template('routing/author.html',
                           author=AUTHORS_INFO[authors_last_name])