# 🌱 Soil Predictor System  

This project is a **Flask-based machine learning API** that processes **soil sensor data** and predicts:  
- **Erosion Level**  
- **Irrigation Need**  
- **Soil Condition**  

### 🔥 **Key Features**  
👉 **Real-time soil sensor data processing**  
👉 **Machine learning models for predictions**  
👉 **REST API for communication**  
👉 **Basic Web UI (`index.html`) for visualization**  
👉 **Simulated sensor data generation (`sensor.py`)**  
👉 **Deployed on Railway.app** for remote access  

---

## 🌍 **Live API URL**  
The Flask API is **deployed on Railway.app**:  
🔗 **Base URL:** [`https://soil-predictor-production.up.railway.app`](https://soil-predictor-production.up.railway.app)  

---

## 🛠️ **Setup & Running Locally**  

### **1️⃣ Clone the Repository**  
Open a terminal and run:  
```sh
git clone https://github.com/yourusername/SOIL-PREDICTOR.git
cd SOIL-PREDICTOR
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Flask API Locally**  
```sh
python app.py
```

### **4️⃣ Using the Sensor Simulator**  
```sh
python sensor.py
```

---

## 📁 **Project Structure**
```
SOIL-PREDICTOR/
│── static/                     # Frontend assets
│   ├── index.html               # Web UI for displaying predictions
│   ├── style.css                # CSS for styling
│── app.py                       # Flask API
│── sensor.py                    # Simulated sensor data sender
│── requirements.txt              # Python dependencies
│── runtime.txt                   # Specifies runtime for deployment
│── Procfile                      # Deployment process (for Railway.app)
│── Erosion_Level_model.pkl       # ML Model for erosion prediction
│── Irrigation_Need_model.pkl     # ML Model for irrigation prediction
│── Soil_Condition_model.pkl      # ML Model for soil condition prediction
```

---

## 🤖 **Technologies Used**
- **Flask (Python web framework)**
- **Machine Learning Models (.pkl files via joblib)**
- **HTML & CSS (for frontend UI)**
- **Railway.app (for cloud deployment)**

---

## 🚀 **TODO & Future Improvements**
✔️ **Deploy Flask API on Railway.app**  
✔️ **Basic UI for visualization**  
✔️ **Improve error handling**  
✔️ **Add real-time updates to the frontend**  

🔄 **Integrate real ESP32 and other soil sensors**  
🔄 **Store sensor data in a database**  

---

## 🔥 **Contributions Welcome!**  
Feel free to **fork**, raise **issues**, or submit **pull requests**. 🚀  

