from flask import Flask, render_template, request

# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
import requests

app = Flask(__name__)

@app.route('/request-info')
def request_info():
    # Request.remote_addr remote address of the client
    geoip_url= 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    # get(key, default=None, type=None)
    # Return the default value if the requested data doesnt exist
    client_location = requests.get(geoip_url).json()
    return render_template('request/info.html', client_location=client_location)









