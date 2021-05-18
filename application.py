from flask import Flask
import requests
application = Flask(__name__)
app = application

@application.route("/")
def olaMundo():
    return {"ola": "mundo"}

@application.route("/teste")
def olaMundo2():
    response = requests.get("https://api.github.com/users/filipeclacerda/repos")
    return {"resposta": response}