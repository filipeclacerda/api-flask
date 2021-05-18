from flask import Flask, request
application = Flask(__name__)
app = application

@application.route("/")
def olaMundo():
    return {"ola": "mundo"}

@application.route("/teste")
def olaMundo2():
    return {"ola": "mundo2"}