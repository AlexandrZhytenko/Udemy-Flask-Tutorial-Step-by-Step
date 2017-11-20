from flask import Flask, request, render_template

# class flask.Request(environ, populate_request=True, shallow=False)
# The request object used by default in Flask

# attribute method is the current request method (POST, GET etc.)

# attribute form is a A MultiDict with the parsed form data from POST or PUT requests
# class werkzeug.datastructures.MultiDict(mapping=None)
# A MultiDict is a dictionary subclass customized to deal with multiple values for the same key which
# is for example used by the parsing functions in the wrappers

# flask.render_template(template_name_or_list, **context)
# Renders a template from the template folder with the given context


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('forms/form_with_static.html')
    elif request.method == 'POST':
        kwargs = {
            'title': request.form['title'],
            'isbn': request.form['isbn'],
            'author': request.form['author'],
            'secret_key': request.form['SECRET_KEY'],
            'submit_value': request.form['submit'],
        }
        return render_template(
            'forms/basic_form_result.html', **kwargs)