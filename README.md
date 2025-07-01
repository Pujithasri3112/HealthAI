# HealthAI – Intelligent Healthcare Assistant 🏥🤖


HealthAI is a Streamlit-based intelligent healthcare assistant designed to deliver AI-powered health insights, disease prediction, treatment recommendations, and an interactive patient chat experience.

This application leverages mock AI responses for development and testing, with a planned integration of IBM Watson's Granite model for real-world usage.

# 🧠 Overview
HealthAI provides a seamless healthcare interface using modern technologies like Streamlit, Plotly, and Python, offering:

Conversational support for health-related queries

Disease prediction based on user-input symptoms

Personalized treatment plans

Interactive health analytics dashboard

# ⚙️ System Architecture
# 🖥️ Frontend
Framework: Streamlit

Layout: Wide layout with an expandable sidebar

Modular Design: Each feature resides in a separate component file

Visualization: Interactive charts via Plotly

State Management: st.session_state used for user context and chat history

# 🧪 Backend
Language: Python 3.11+

Architecture: Utility-based modular design

Mock AI Responses: Placeholder logic for real-world AI integration

Data Simulation: Realistic health metrics generated with pandas and numpy

# 🧩 Key Components
Module	Description
components/patient_chat.py	Chat interface for answering medical queries using mock AI
components/disease_prediction.py	Input symptoms and receive predicted conditions
components/treatment_plans.py	Get personalized treatment suggestions based on symptoms and conditions
components/health_analytics.py	Interactive dashboards for visualizing health metrics
utils/	Utilities for data generation, AI integration placeholders, etc.

# 🔁 Data Flow
plaintext
Copy
Edit
User Input --> Streamlit UI --> Session State Handling
        --> Mock Data Generation --> AI Processing (Mock)
        --> Plotly Visualizations --> Chat & Result Display
📦 Dependencies
🔑 Core
Streamlit >=1.46.1

Pandas >=2.3.0

Plotly >=6.2.0

NumPy


# 🔮 Planned Integrations
IBM Watson ML / Granite: Real AI model for disease prediction and chat responses

PostgreSQL Database: Persistent storage for user and health data

# 🚀 Deployment
Replit
Environment: Python 3.11 + Nix

Port: 5000

Command:


streamlit run app.py --server.port 5000
Address: 0.0.0.0

Headless Mode: Enabled

Theme: Custom healthcare-friendly design

Environment Variables

WATSONX_API_KEY=your_ibm_watson_api_key
WATSONX_PROJECT_ID=your_ibm_project_id
# 🛡️ Key Features
# ✅ Medical Disclaimer System
Prominent notices across the app

Clear messaging that results are for informational purposes only

# ✅ Mock Data Generation
Realistic health indicators (heart rate, blood pressure, etc.)

Time-series and symptom tracking

Data used for health analytics and insights

# ✅ Modular Design
Each component is independently maintained

Reusable utility functions

Clean separation of concerns for scalability



