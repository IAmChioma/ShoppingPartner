from flask import Flask
import request_session

app = Flask(__name__)

@app.route("/search/<searchphrase>")
def hello_world(searchphrase):
    return request_session.walmart_request(searchphrase)

if __name__ == "__main__":
    app.Run()

