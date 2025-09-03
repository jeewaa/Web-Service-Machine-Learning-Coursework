from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
model = joblib.load('bank_model.pkl')
encoder = joblib.load('encoder.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df_input = pd.DataFrame([data])
    # Preprocess: encode categoricals, scale numerics (assume other features default or from avg)
    # ... (similar to preprocessing)
    pred = model.predict(processed_input)
    return jsonify({'subscription': 'yes' if pred[0] == 1 else 'no'})

if __name__ == '__main__':
    app.run()