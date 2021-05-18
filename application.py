from flask import Flask, request
application = Flask(__name__)
app = application

@application.route("/")
def olaMundo():
    return {"ola": "mundo"}

@application.route("/teste")
def olaMundo():
    return {"ola": "mundo2"}