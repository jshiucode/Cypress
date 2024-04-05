from flask import Flask
from flask import request
from Gordian2 import Gordian

app = Flask(__name__)

@app.route("/")
def run_algorithm():
    return [1,2]
