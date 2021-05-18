import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://flask-env.eba-rt5342sp.us-east-2.elasticbeanstalk.com")
print(response.status_code)
jprint(response.json())