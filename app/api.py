#!/usr/bin/env python

# -----------------Import Modules----------------- #

from flask import Flask, request
import json
import requests

# local modules
from assets import gen_message

# -----------------Main Functions----------------- #

app = Flask(__name__)
botname = "ReptileDB Bot"

@app.route("/")
def hello():

    return "flask"

@app.route("/bot", methods=["POST"])
def bot():
    # json received
    data = request.json
    # token for POST to mattermost
    token = data["token"]
    # generate text
    msg = gen_message.Message()
    text = ""
    if "real python" in data["text"]:
        text = msg.animalmsg("python")
    else:
        text = msg.default(data["user_name"])
    # generate dict
    payload = {
        "text": text,
        "username": botname,
        "MATTERMOST_TOKEN": token
    }
    # format dict to JSON
    json_payload = json.dumps(payload)

    return json_payload

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)