#
#  Example usage of ServerSentEvents with Flask.
#  Created On 21 November 2022
#

# to start the server, execute the following command 👇
# python -m flask --app examples/routes run


from flask import Flask
from src import ServerSentEvents

app = Flask(__name__)
sse: ServerSentEvents = None


@app.route("/send")
def send():
    global sse

    if sse:
        sse.send({"msg": "Python is awesome!"})
    else:
        return "NO CONNECTION"

    return "OK"


@app.route("/end")
def end():
    global sse

    if sse:
        sse.send(event="end")
        sse = None
    else:
        return "NO CONNECTION"

    return "FINISHED"


@app.route("/subscribe")
def subscribe():
    global sse

    # create a new server sent events channel
    sse = ServerSentEvents()

    return sse.response()
