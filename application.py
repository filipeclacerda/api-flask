from flask import Flask, request
application = Flask(__name__)
app = application

@application.route("/")
def olaMundo():
    return {"ola": "mundo"}

@application.route("/teste", method="POST")
def olaMundo():
    return {"ola": "mundo2"}