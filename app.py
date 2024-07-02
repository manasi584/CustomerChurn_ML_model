from flask import Flask, request, jsonify
import joblib
import numpy as np
from predict import get_input,predict_churn

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.get_json(force=True)
    prediction = predict_churn(data)
    
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
