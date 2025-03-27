import requests
import time
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# API URL
API_URL = "https://soil-predictor-production.up.railway.app//process-soil-data"

# Authentication credentials
AUTH = {"id": "sensor123", "password": "password123"}

def generate_dummy_data():
    """Generate random sensor data values."""
    return {
        "Soil_pH": round(random.uniform(5.5, 7.5), 2),
        "Moisture_Content(%)": round(random.uniform(10, 50), 2),
        "Soil_Temperature(°C)": round(random.uniform(15, 35), 2),
        "Nitrogen_Content(ppm)": round(random.uniform(20, 100), 2),
        "Phosphorus_Content(ppm)": round(random.uniform(10, 50), 2),
        "Potassium_Content(ppm)": round(random.uniform(10, 60), 2),
        "Rainfall": round(random.uniform(50, 300), 2),
        "Land_Slope": round(random.uniform(0, 30), 2),
        "Organic_Matter": round(random.uniform(1, 10), 2),
        "Vegetation_Cover": round(random.uniform(30, 90), 2)
    }

def send_data():
    """Continuously send simulated sensor data at intervals."""
    while True:
        data = {
            "auth": AUTH,  # Authentication credentials
            "data": generate_dummy_data()  # Randomly generated sensor values
        }

        try:
            response = requests.post(API_URL, json=data, timeout=5)  # Send request with 5-sec timeout
            response_data = response.json()

            if response.status_code == 200:
                logging.info(f"✅ Data Sent: {data['data']}")
                logging.info(f"✅ Response: {response_data}")
            else:
                logging.warning(f"⚠️ API Error {response.status_code}: {response_data}")

        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Error sending data: {e}")

        time.sleep(10)  # Send data every 10 seconds

if __name__ == "__main__":
    send_data()