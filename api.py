from flask import Flask, request
app = Flask("api")

@app.route("/")
def olaMundo():
    return {"ola": "mundo"}
