from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the trained model
model=pickle.load(open('house_model.pkl', 'rb'))
encoder = pickle.load(open('location_encoder.pkl', 'rb'))

@app.route("/predict", methods=['POST'])

def predict():
    data=request.get_json()

    size=data['size']
    bedrooms=data['bedrooms']
    bathrooms=data['bathrooms']
    location=data['location'].capitalize()  # Ensure location is capitalized to match training data

    # Encode the location using the loaded encoder
    location_encoded = encoder.transform([location])[0]

    # Create a feature DataFrame that matches the model's training feature names
    features = pd.DataFrame([
        {
            'size': size,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'location': location_encoded,
        }
    ])

    predicted_price = model.predict(features)

    return jsonify({'predicted_price': round(predicted_price[0], 2)})
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
