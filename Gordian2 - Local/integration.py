from flask import Flask
from flask import request
from Gordian2 import Gordian

app = Flask(__name__)

@app.route("/")
def run_algorithm():
    (links, time, knots) = Gordian(request.data.decode("utf-8"))
    return {"links": links, "time": time, "knots": knots}
