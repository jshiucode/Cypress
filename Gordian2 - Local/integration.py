from flask import Flask
from flask import request
from flask_cors import CORS
from Gordian2 import Gordian

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def run_algorithm():
    (links, time, knots) = Gordian(request.data.decode("utf-8"))
    return {"links": links, "elapsed_time": time, "knots": knots}