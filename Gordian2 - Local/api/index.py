from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from algorithm import Gordian2

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def run_algorithm():
    (links, time, knots) = Gordian2.Gordian(request.data.decode("utf-8"))
    return {"links": links, "elapsed_time": time, "knots": knots}

@app.route("/", methods=["GET"])
def home():
    return "You shouldn't be here, go away!", 200


@app.errorhandler(500)
def page_not_found(e):
    return jsonify({"status": 500, "message": "Not Found"}), 500
