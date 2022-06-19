from flask import *
import requests
import json

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        return nostr(request.form['paste'])
    return render_template('create.html')

def nostr(paste):
    url = "http://127.0.0.1:5000/create?paste="+paste

    payload={}
    headers = {
     'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    eventid = json.loads(response.text)

    return eventid


if __name__ == "__main__":
    app.run('127.0.0.1', port=5555)
