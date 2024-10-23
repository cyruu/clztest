from flask import Flask,request,jsonify
from flask_cors import CORS
import pandas as pd
from NaiveBayesClass import NaiveBayesClass

app = Flask(__name__)
CORS(app)

@app.route("/calcsentiment", methods=["POST"])
def calcsentiment():
    nb = NaiveBayesClass()
    data = request.json
    sentence = data["sentence"]
    sentiment = nb.calculateSentiment(sentence)
    return jsonify({"sentiment":sentiment})

if __name__ == "__main__":
    print("running in porrt 8001")
    app.run(debug=True, port=8001)