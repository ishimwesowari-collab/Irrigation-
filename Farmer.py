import numpy as np
import pickle
import streamlit as st
def load_model():
    with open('Irrigation.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# --- App title ---
st.title("💧 Irrigation Prediction App")

# --- Category mappings ---
CropType_map = {
    'Coffee': 0, 
    'Garden Flowers': 1, 
    'Groundnuts': 2, 
    'Maize': 3, 
    'Paddy': 4, 
    'Potato': 5, 
    'Pulse': 6, 
    'Sugarcane': 7, 
    'Wheat': 8
}

# --- Input fields ---
CropDays = st.number_input("Crop Days", min_value=0, max_value=300, value=99)
SoilMoisture = st.number_input("Soil Moisture", min_value=0, max_value=2000, value=678)
Temperature = st.number_input("Temperature (°C)", min_value=0, max_value=100, value=24)
Humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=18)
CropType = st.selectbox("Crop Type", list(CropType_map.keys()))

# --- Prediction button ---
if st.button("🌾 Predict Irrigation Need"):
    # Prepare input data
    input_data = np.array([[CropType_map[CropType], CropDays, SoilMoisture, Temperature, Humidity]])
    
    # Make prediction
    try:
        prediction = model.predict(input_data)
        # --- Display result ---
        if prediction[0]==1:
            st.success("💧 It's time for irrigation, insufficient water level")
        else:
            st.success("Sufficient water level")
    except AttributeError as e:
        st.error(f"Error: {e}. Please ensure 'Irrigation.pkl' contains a trained model, not a NumPy array.")