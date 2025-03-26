from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load your saved models
erosion_model = joblib.load('Erosion_Level_model.pkl')
irrigation_model = joblib.load('Irrigation_Need_model.pkl')
soil_condition_model = joblib.load('Soil_Condition_model.pkl')

# Define the feature names
feature_names = ["Soil_pH", "Moisture_Content(%)", "Soil_Temperature(°C)", "Nitrogen_Content(ppm)", "Phosphorus_Content(ppm)", "Potassium_Content(ppm)"]

# Variable to store the latest data
latest_data = {}

@app.route('/process-soil-data', methods=['POST'])
def process_soil_data():
    global latest_data
    data = request.json['data']
    
    # Convert the input data to a DataFrame with the appropriate column names
    features = pd.DataFrame([data], columns=feature_names)
    
    # Make predictions using the models
    erosion_prediction = erosion_model.predict(features)[0]
    irrigation_prediction = irrigation_model.predict(features)[0]
    soil_condition_prediction = soil_condition_model.predict(features)[0]
    
    # Update the latest data
    latest_data = {
        'soil_values': data,
        'Erosion_Level': int(erosion_prediction),
        'Irrigation_Need': int(irrigation_prediction),
        'Soil_Condition': int(soil_condition_prediction)
    }
    
    return jsonify({'status': 'success', 'data': latest_data})

@app.route('/latest-soil-data', methods=['GET'])
def get_latest_soil_data():
    return jsonify(latest_data)

# Route to serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)