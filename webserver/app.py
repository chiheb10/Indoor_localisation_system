import json
import os
import flask
from flask import Flask, Response, render_template, send_from_directory, send_file
import serial
# Needed for the demo, but perhaps not in actual use
import itertools
import random
import time
import re
import socket

# Server sent events
class ServerSentEvent:
    FIELDS = ('event', 'data', 'id')
    def __init__(self, data, event=None, event_id=None):
        self.data = data
        self.event = event 
        self.id = event_id 

    def encode(self):
        if not self.data:
            return ""
        ret = []
        for field in self.FIELDS:
            entry = getattr(self, field) 
            if entry is not None:
                ret.extend(["%s: %s" % (field, line) for line in entry.split("\n")])
        return "\n".join(ret) + "\n\n"

# The Flask application
app = Flask(__name__)

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route("/", methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route("/stream")
def stream():
    def gen():
        count = itertools.count()
        #client_socket= socket.socket()  # instantiate
        #client_socket.connect(("127.0.0.1", 8080))  # connect to the server
        i=0
        x=range(20,200,4)
        y=range(55,250,7)
        while True:
            #dat = client_socket.recv(1024).decode()
            #v=dat.split()
            xx=x[i]
            yy=y[i]
            i=i+1
            #xx=int(v[0])//2+255
            #yy=int(v[1])//2+10
            data = json.dumps({"x1":yy, "y1":xx})
            ev = ServerSentEvent(data)
            print(ev.encode())
            yield ev.encode()
            time.sleep(0.05)
    return Response(gen(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)
