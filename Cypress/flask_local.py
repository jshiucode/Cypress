from flask import Flask
from flask import request
from flask_cors import CORS
from algorithm.Cypress import Cypress

app = Flask(__name__)
CORS(app)


"""
For running locally with React frontend (non-vercel)
"""
@app.route("/", methods=["POST"])
def run_algorithm():
    (links, time, knots) = Cypress(request.data.decode("utf-8"))
    return {"links": links, "elapsed_time": time, "knots": knots}