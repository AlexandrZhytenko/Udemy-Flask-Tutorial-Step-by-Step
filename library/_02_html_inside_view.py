from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = """
    <html>
        <h1>Welcome to my library</h1>
        {authors_list}
    </html>
    """
    authors = ['Edgard A.Poe', 'Jorge L. Borges', 'Mark Twain', 'Jane Austen']
    authors_list = '<ul>'
    authors_list += '\n'.join([
        '<li>{author}</li>'.format(author=author) for author in authors])
    authors_list += '</ul>'
    return html.format(authors_list=authors_list)