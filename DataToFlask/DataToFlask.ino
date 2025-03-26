#include <WiFi.h>
#include <HTTPClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverURL = "http://127.0.0.1:5000/process-soil-data";  // Change IP if needed

// Soil Temperature Sensor (DS18B20)
#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Analog Pins for Soil Sensors
#define SOIL_MOISTURE_PIN 34  // Capacitive Soil Moisture Sensor
#define NPK_SENSOR_PIN 35     // Gravity NPK Sensor
#define PH_SENSOR_PIN 32      // Gravity Analog pH Sensor

void setup() {
    Serial.begin(115200);

    // Initialize WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    // Initialize DS18B20 Temperature Sensor
    sensors.begin();
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(serverURL);
        http.addHeader("Content-Type", "application/json");

        // Read Sensor Data
        int moisture = analogRead(SOIL_MOISTURE_PIN);
        int npk = analogRead(NPK_SENSOR_PIN);
        int phRaw = analogRead(PH_SENSOR_PIN);

        // Convert Raw Readings to Meaningful Values
        float soilMoisture = map(moisture, 0, 4095, 0, 100); // Convert to percentage
        float nitrogen = map(npk, 0, 4095, 40, 60);  // Simulated NPK scaling
        float phosphorus = map(npk, 0, 4095, 25, 35);
        float potassium = map(npk, 0, 4095, 15, 25);
        float soilpH = map(phRaw, 0, 4095, 4, 9); // pH scale approximation

        // Get Temperature from DS18B20
        sensors.requestTemperatures();
        float soilTemperature = sensors.getTempCByIndex(0);

        // Create JSON Payload
        String jsonData = "{";
        jsonData += "\"id\":\"sensor123\",";
        jsonData += "\"password\":\"password123\",";
        jsonData += "\"Nitrogen_Content(ppm)\":" + String(nitrogen) + ",";
        jsonData += "\"Phosphorus_Content(ppm)\":" + String(phosphorus) + ",";
        jsonData += "\"Potassium_Content(ppm)\":" + String(potassium) + ",";
        jsonData += "\"Moisture_Content(%)\":" + String(soilMoisture) + ",";
        jsonData += "\"Soil_Temperature(°C)\":" + String(soilTemperature) + ",";
        jsonData += "\"Soil_pH\":" + String(soilpH);
        jsonData += "}";

        // Send Data to Flask Server
        int httpResponseCode = http.POST(jsonData);
        Serial.println("Response Code: " + String(httpResponseCode));
        Serial.println("Sent JSON: " + jsonData);

        http.end();
    }
    delay(30000); // Send data every 30 seconds
}
