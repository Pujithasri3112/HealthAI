import streamlit as st
import os
from datetime import datetime
from utils.ai_integration import init_watson_ml, get_ai_response
from utils.patient_data import initialize_patient_data, get_sample_health_data
from components.patient_chat import display_patient_chat
from components.disease_prediction import display_disease_prediction
from components.treatment_plans import display_treatment_plans
from components.health_analytics import display_health_analytics

# Page configuration
st.set_page_config(
    page_title="HealthAI - Intelligent Healthcare Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

def initialize_session_state():
    """Initialize session state variables"""
    if 'patient_data' not in st.session_state:
        st.session_state.patient_data = initialize_patient_data()
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'watson_ml_client' not in st.session_state:
        st.session_state.watson_ml_client = None

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Initialize Watson ML client
    if st.session_state.watson_ml_client is None:
        with st.spinner("Initializing AI model..."):
            st.session_state.watson_ml_client = init_watson_ml()
    
    # Main header
    st.title("🏥 HealthAI - Intelligent Healthcare Assistant")
    st.markdown("*Powered by IBM Watson ML and Granite-13b-instruct-v2*")
    
    # Sidebar for patient profile
    with st.sidebar:
        st.header("👤 Patient Profile")
        
        # Editable patient information
        patient_data = st.session_state.patient_data
        
        with st.expander("✏️ Edit Profile", expanded=False):
            new_name = st.text_input("Name", value=patient_data['name'])
            new_age = st.number_input("Age", min_value=1, max_value=120, value=patient_data['age'])
            new_gender = st.selectbox("Gender", ["Male", "Female", "Other"], 
                                    index=["Male", "Female", "Other"].index(patient_data['gender']))
            new_blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                                        index=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"].index(patient_data['blood_type']))
            
            # Current vitals
            st.subheader("Current Vitals")
            new_heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, 
                                           value=patient_data['current_vitals']['heart_rate'])
            new_weight = st.number_input("Weight (lbs)", min_value=50, max_value=500, 
                                       value=patient_data['current_vitals']['weight'])
            new_height = st.text_input("Height", value=patient_data['current_vitals']['height'])
            
            # Blood pressure input
            bp_parts = patient_data['current_vitals']['blood_pressure'].split('/')
            new_systolic = st.number_input("Systolic BP", min_value=70, max_value=200, value=int(bp_parts[0]))
            new_diastolic = st.number_input("Diastolic BP", min_value=40, max_value=120, value=int(bp_parts[1]))
            new_temperature = st.number_input("Temperature (°F)", min_value=95.0, max_value=110.0, 
                                            value=patient_data['current_vitals']['temperature'], step=0.1)
            
            # Medical history
            st.subheader("Medical Information")
            new_medications = st.text_area("Current Medications", 
                                         value="\n".join(patient_data['current_medications']),
                                         height=100)
            new_allergies = st.text_area("Allergies", 
                                       value=", ".join(patient_data['allergies']),
                                       height=80)
            new_history = st.text_area("Medical History", 
                                     value="\n".join(patient_data['medical_history']),
                                     height=100)
            
            if st.button("💾 Save Profile Changes", type="primary"):
                # Update patient data in session state
                st.session_state.patient_data.update({
                    'name': new_name,
                    'age': new_age,
                    'gender': new_gender,
                    'blood_type': new_blood_type,
                    'current_vitals': {
                        'heart_rate': new_heart_rate,
                        'blood_pressure': f"{new_systolic}/{new_diastolic}",
                        'temperature': new_temperature,
                        'weight': new_weight,
                        'height': new_height
                    },
                    'current_medications': [med.strip() for med in new_medications.split('\n') if med.strip()],
                    'allergies': [allergy.strip() for allergy in new_allergies.split(',') if allergy.strip()],
                    'medical_history': [hist.strip() for hist in new_history.split('\n') if hist.strip()]
                })
                st.success("Profile updated successfully!")
                st.rerun()
        
        # Display current patient information
        st.write(f"**Name:** {patient_data['name']}")
        st.write(f"**Age:** {patient_data['age']}")
        st.write(f"**Gender:** {patient_data['gender']}")
        st.write(f"**Blood Type:** {patient_data['blood_type']}")
        
        st.divider()
        
        # Current health status
        st.subheader("📊 Current Health Status")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="Heart Rate",
                value=f"{patient_data['current_vitals']['heart_rate']} bpm",
                delta="Normal"
            )
            st.metric(
                label="Blood Pressure",
                value=f"{patient_data['current_vitals']['blood_pressure']}",
                delta="Optimal"
            )
        
        with col2:
            st.metric(
                label="Temperature",
                value=f"{patient_data['current_vitals']['temperature']}°F",
                delta="Normal"
            )
            st.metric(
                label="Weight",
                value=f"{patient_data['current_vitals']['weight']} lbs",
                delta="+2 lbs"
            )
        
        st.divider()
        
        # Medical disclaimer
        st.warning("""
        **⚠️ Medical Disclaimer**
        
        This application provides general health information and should not replace professional medical advice. Always consult with healthcare professionals for medical concerns.
        """)
    
    # Main content area with tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "💬 Patient Chat",
        "🔍 Disease Prediction", 
        "📋 Treatment Plans",
        "📈 Health Analytics"
    ])
    
    with tab1:
        display_patient_chat()
    
    with tab2:
        display_disease_prediction()
    
    with tab3:
        display_treatment_plans()
    
    with tab4:
        display_health_analytics()

if __name__ == "__main__":
    main()