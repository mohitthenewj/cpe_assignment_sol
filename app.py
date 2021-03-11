#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask.logging import create_logger

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

def scale(payload):
    """Scales Payload"""
    
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@app.route("/")
def home():
    """Home page, add code here """
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:

        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    json_payload = request.json
    inference_payload = pd.DataFrame(json_payload)
    # scale the input
    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, clf
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    """Add code here """
    # Run flask application
