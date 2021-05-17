from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def olaMundo():
    return {"ola": "mundo"}
