#!/usr/bin/env python

from flask import Flask, request
import json
import requests

from assets import gen_message
msg = gen_message.Message()

app = Flask(__name__)

# bot config
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
    text = ""
    if "real python" in data["text"]:
        text = msg.get_reptile_info("python")
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