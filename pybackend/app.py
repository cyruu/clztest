# from flask import Flask,request,jsonify
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# @app.route("/getflaskdata", methods=["POST"])
# def getflaskdata():
#     df = pd.read_csv("./reviews.csv")
#     reviews = df["review"]
#     output = df["output"]
    
#     #lowercase
#     reviews = reviews.str.lower()
#     print(reviews)
#     data = request.json
#     return jsonify({"sentiment":data["bodyData"]})

# if __name__ == "__main__":
#     print("running in porrt 8000")
#     app.run(debug=True, port=8000)