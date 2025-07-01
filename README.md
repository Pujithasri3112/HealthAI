HealthAI - Intelligent Healthcare Assistant
Overview
HealthAI is a Streamlit-based web application that serves as an intelligent healthcare assistant. The application provides AI-powered health insights, disease prediction, treatment plan generation, and patient chat functionality. Built with Python, it uses Streamlit for the frontend interface and integrates with mock AI responses (designed to work with IBM Watson's Granite model in production).

System Architecture
Frontend Architecture
Framework: Streamlit web framework
Layout: Wide layout with expandable sidebar
Components: Modular component structure with separate files for different features
Visualization: Plotly for interactive charts and health data visualization
State Management: Streamlit session state for maintaining user data and chat history
Backend Architecture
Language: Python 3.11+
Structure: Utility-based architecture with separate modules for data generation and AI responses
Mock Data: Patient data generation using pandas and numpy for realistic health metrics
AI Integration: Mock responses with placeholder for IBM Watson ML integration
Key Components
Patient Chat (components/patient_chat.py): Interactive chat interface for health queries
Disease Prediction (components/disease_prediction.py): Symptom assessment and condition insights
Treatment Plans (components/treatment_plans.py): Personalized treatment recommendations
Health Analytics (components/health_analytics.py): Data visualization dashboard
Utils Module: Patient data generation and AI response handling
Data Flow
User Interaction: Users interact through Streamlit interface
Session Management: User data stored in Streamlit session state
Data Generation: Mock patient data generated using pandas/numpy
AI Processing: User queries processed through mock AI response system
Visualization: Health metrics displayed using Plotly charts
Response Delivery: AI responses delivered through chat interface
External Dependencies
Core Dependencies
Streamlit (>=1.46.1): Web application framework
Pandas (>=2.3.0): Data manipulation and analysis
Plotly (>=6.2.0): Interactive data visualization
NumPy: Numerical computing (indirect dependency)
Planned Integrations
IBM Watson ML: AI model integration (environment variables configured)
Postgres Database: Data persistence (not currently implemented)
Deployment Strategy
Replit Configuration
Environment: Python 3.11 with Nix package manager
Deployment Target: Autoscale deployment
Port Configuration: Server runs on port 5000
Startup Command: streamlit run app.py --server.port 5000
Environment Variables
WATSONX_API_KEY: IBM Watson API key (optional)
WATSONX_PROJECT_ID: IBM Watson project ID (optional)
Server Configuration
Headless mode enabled for deployment
Custom theme with healthcare-friendly colors
Address bound to 0.0.0.0 for external access
Key Features
Medical Disclaimer System
Prominent medical disclaimers throughout the application
Warning messages for diagnostic and treatment features
Clear messaging about the informational nature of AI responses
Mock Data Generation
Realistic patient health metrics (heart rate, blood pressure, glucose, etc.)
Time-series data generation for health analytics
Symptom tracking and correlation analysis
Modular Component Design
Separate components for different healthcare features
Reusable utility functions for data and AI operations
Clean separation of concerns for maintainability
