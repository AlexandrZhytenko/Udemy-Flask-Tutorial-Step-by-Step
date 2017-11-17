# flask.redirect(location, code=302, Response=None)
# Returns a response object (a WSGI application) that, if called,
# redirects the client to the target location

# flask.url_for(endpoint, **values)
# Generates a URL to the given endpoint with the method provided

from flask import Flask, render_template, request, redirect, url_for

import requests

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('request_info'))

@app.route('/info')
def info():
    return redirect(url_for('request_info'), code=301)

@app.route('/request-info')
def request_info():
    # Request.remote_addr remote address of the client
    geoip_url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)

    # get(key, default=None, type=None)
    # Return the default value if the requested data doesnt exist
    client_location = requests.get(geoip_url).json()
    return render_template('request/info.html', client_location=client_location)







