import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Load the trained model and scaler
model = joblib.load("mobile_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load the dataset for product selection
data = pd.read_csv("Cellphone.csv")

# Custom CSS for beautiful and stylish look
st.markdown("""
<style>
    /* Overall app styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Title styling */
    .main-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 48px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    
    /* Subtitle styling */
    .subtitle {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        color: #e8f4f8;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Card container */
    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.18);
    }
    
    /* Input label styling */
    .input-label {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 16px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 5px;
    }
    
    /* Prediction text styling */
    .prediction-text {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #e74c3c;
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #3498db, #2980b9);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        font-weight: 600;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: linear-gradient(45deg, #2980b9, #21618c);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.6);
    }
    
    /* Selectbox styling - make visible and beautiful */
    .stSelectbox {
        margin-top: 10px;
        margin-bottom: 15px;
    }
    
    .stSelectbox>div>div {
        background: linear-gradient(135deg, rgba(52, 152, 219, 0.15), rgba(41, 128, 185, 0.15));
        border-radius: 12px;
        border: 2.5px solid #3498db;
        padding: 12px 15px;
        font-weight: 600;
        font-size: 16px;
        color: #2c3e50;
        min-height: 45px;
        display: flex;
        align-items: center;
    }
    
    .stSelectbox>div>div>div {
        color: #2c3e50;
        font-weight: 600;
    }
    
    .stSelectbox svg {
        color: #3498db;
    }
    
    /* Number input styling */
    .stNumberInput>div>div>input {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 2px solid #bdc3c7;
        padding: 10px;
        font-size: 16px;
    }
    
    .stNumberInput>div>div>input:focus {
        border-color: #3498db;
        box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(45deg, #27ae60, #2ecc71);
        color: white;
        border-radius: 10px;
        padding: 15px;
        font-weight: 600;
    }
    
    /* Hide Streamlit's default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📱 Mobile Price Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover the perfect price for your dream mobile phone! 🚀</p>', unsafe_allow_html=True)

# Add image in a card
st.markdown('<div class="card">', unsafe_allow_html=True)

# Try to load image with fallback options
image_loaded = False
image_paths_to_try = [
    "image mobile.png",  # Relative path in same directory as app.py
    os.path.join(os.path.dirname(__file__), "image mobile.png"),  # Explicit relative path
    r"C:\Users\USSER\Downloads\image mobile.png",  # Original local path for local testing
]

for image_path in image_paths_to_try:
    try:
        if os.path.exists(image_path):
            st.image(image_path, caption="✨ Premium Mobile Phone Showcase", width="stretch")
            image_loaded = True
            break
    except Exception as e:
        continue

# If image couldn't be loaded, show a placeholder
if not image_loaded:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; 
                border-radius: 12px; 
                padding: 40px; 
                text-align: center;
                min-height: 200px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                font-weight: bold;">
        📱 Premium Mobile Phone Showcase
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Product selection in a card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #2c3e50; text-align: center;">🔍 Quick Product Lookup</h3>', unsafe_allow_html=True)
product_ids = data['Product_id'].unique().tolist()
st.markdown('<span class="select-label">📦 Select a Product ID</span>', unsafe_allow_html=True)
selected_id = st.selectbox("", ["None"] + product_ids, label_visibility="collapsed")

if selected_id != "None":
    row = data[data['Product_id'] == selected_id].iloc[0]
    st.session_state['sale'] = row['Sale']
    st.session_state['weight'] = row['weight']
    st.session_state['resoloution'] = row['resoloution']
    st.session_state['ppi'] = row['ppi']
    st.session_state['cpu_core'] = row['cpu core']
    st.session_state['cpu_freq'] = row['cpu freq']
    st.session_state['internal_mem'] = row['internal mem']
    st.session_state['ram'] = row['ram']
    st.session_state['RearCam'] = row['RearCam']
    st.session_state['Front_Cam'] = row['Front_Cam']
    st.session_state['battery'] = row['battery']
    st.session_state['thickness'] = row['thickness']
    st.markdown(f'<div style="background: linear-gradient(45deg, #27ae60, #2ecc71); color: white; border-radius: 12px; padding: 15px; text-align: center; font-weight: 700; margin-bottom: 15px;">✅ Product ID {selected_id} loaded successfully!</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input specifications in a card with columns
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #2c3e50; text-align: center;">📝 Enter Mobile Specifications</h3>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p class="input-label">💰 Sale</p>', unsafe_allow_html=True)
    sale = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('sale', 0)), key="sale")
    
    st.markdown('<p class="input-label">⚖️ Weight (g)</p>', unsafe_allow_html=True)
    weight = st.number_input("", min_value=0.0, step=0.1, value=float(st.session_state.get('weight', 0.0)), key="weight")
    
    st.markdown('<p class="input-label">📱 Resolution</p>', unsafe_allow_html=True)
    resoloution = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('resoloution', 0)), key="resoloution")
    
    st.markdown('<p class="input-label">🔍 PPI</p>', unsafe_allow_html=True)
    ppi = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('ppi', 0)), key="ppi")

with col2:
    st.markdown('<p class="input-label">🧠 CPU Cores</p>', unsafe_allow_html=True)
    cpu_core = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('cpu_core', 0)), key="cpu_core")
    
    st.markdown('<p class="input-label">⚡ CPU Frequency (GHz)</p>', unsafe_allow_html=True)
    cpu_freq = st.number_input("", min_value=0.0, step=0.1, value=float(st.session_state.get('cpu_freq', 0.0)), key="cpu_freq")
    
    st.markdown('<p class="input-label">💾 Internal Memory (GB)</p>', unsafe_allow_html=True)
    internal_mem = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('internal_mem', 0)), key="internal_mem")
    
    st.markdown('<p class="input-label">🧠 RAM (GB)</p>', unsafe_allow_html=True)
    ram = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('ram', 0)), key="ram")

with col3:
    st.markdown('<p class="input-label">📷 Rear Camera (MP)</p>', unsafe_allow_html=True)
    RearCam = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('RearCam', 0)), key="RearCam")
    
    st.markdown('<p class="input-label">🤳 Front Camera (MP)</p>', unsafe_allow_html=True)
    Front_Cam = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('Front_Cam', 0)), key="Front_Cam")
    
    st.markdown('<p class="input-label">🔋 Battery (mAh)</p>', unsafe_allow_html=True)
    battery = st.number_input("", min_value=0.0, step=1.0, value=float(st.session_state.get('battery', 0)), key="battery")
    
    st.markdown('<p class="input-label">📏 Thickness (mm)</p>', unsafe_allow_html=True)
    thickness = st.number_input("", min_value=0.0, step=0.1, value=float(st.session_state.get('thickness', 0.0)), key="thickness")

st.markdown('</div>', unsafe_allow_html=True)

# Prediction button and result in a card
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔮 Predict Price"):
        # Create input array
        input_data = np.array([[sale, weight, resoloution, ppi, cpu_core, cpu_freq, internal_mem, ram, RearCam, Front_Cam, battery, thickness]])
        
        # Scale the input
        input_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = model.predict(input_scaled)
        
        st.markdown(f'<p class="prediction-text">💰 Predicted Price: {int(prediction[0])}</p>', unsafe_allow_html=True)
        st.balloons()
st.markdown('</div>', unsafe_allow_html=True)