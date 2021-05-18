from flask import Flask
import requests
application = Flask(__name__)
app = application

@application.route("/")
def olaMundo():
    return {"ola": "mundo"}

@application.route("/teste")
def olaMundo2():
    response = requests.get("http://flask-env.eba-rt5342sp.us-east-2.elasticbeanstalk.com")
    return {"resposta": response}