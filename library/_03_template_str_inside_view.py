from flask import Flask
from flask import render_template_string

# flask.render_template_string(source, **context)
# Renders a template from the given template source
# string with the given context. Template variables will be autoescaped.

app = Flask(__name__)

@app.route('/')
def hello_world():
    library_name = 'my'
    html = """
    <html>
        <h1>Welcome to {{library_name}} library!</h1>
        <ul>
            {% for author in authors %}
                <li>{{ author }}</li>
            {% endfor %}
        </ul>
    </html>
    """
    # {{...}} -  for Expressions to print to the template output
    # { % ... %} for Statements
    authors = ['Edgard A.Poe', 'Jorge L. Borges', 'Mark Twain', 'Jane Austen']
    render_html = render_template_string(html, library_name=library_name, authors=authors)

    return render_html