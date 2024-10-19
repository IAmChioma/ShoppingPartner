from flask import Flask
from flask_cors import CORS
import request_session

app = Flask(__name__)
CORS(app)

@app.route("/search/<searchphrase>")
def hello_world(searchphrase):
    return request_session.walmart_request(searchphrase)

if __name__ == "__main__":
    app.Run()

