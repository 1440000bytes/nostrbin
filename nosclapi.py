from flask import Flask
from flask import request,jsonify
import pexpect

app = Flask(__name__)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/create")
def publish():

    paste = request.args.get('paste')

    noscl = pexpect.spawn ('noscl publish "' + paste + '"')
    noscl.expect ('Seen ')
    output = str(noscl.read())
    eventid = output.replace('b"','').replace(" on 'wss://nostr-pub.wellorder.net'.","").replace('\\r\\n"','')
    noscl.interact()

    eventid = jsonify({
        "eventid": eventid
        })

    return eventid

if __name__ == "__main__":
    app.run()
