from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained models
erosion_model = joblib.load('soil_erosion_model.pkl')
fertility_model = joblib.load('fertility_status_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Serves the HTML page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form submission
        data = request.form

        # Extract input features
        features = [
            float(data['Soil_Moisture']),
            float(data['pH_Level']),
            float(data['Temperature']),
            float(data['Nitrogen']),
            float(data['Phosphorus']),
            float(data['Potassium']),
            float(data['Rainfall']),
            float(data['Land_Slope']),
            float(data['Organic_Matter']),
            float(data['Vegetation_Cover'])
        ]

        features_array = np.array([features])

        # Make predictions
        erosion_pred = erosion_model.predict(features_array)[0]
        fertility_pred = fertility_model.predict(features_array)[0]

        # Convert predictions to readable labels
        erosion_labels = {0: "Low", 1: "Medium", 2: "High"}
        fertility_labels = {0: "Infertile", 1: "Moderate", 2: "Fertile"}

        result = {
            "Soil_Erosion": erosion_labels[erosion_pred],
            "Fertility_Status": fertility_labels[fertility_pred]
        }

        return render_template('index.html', result=result)  # Return results to HTML page

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
