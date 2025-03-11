import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Disease Prediction", page_icon=" ")

# Hide Streamlit default style
theme_hide = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(theme_hide, unsafe_allow_html=True)

# Load models with error handling
def load_model(path):
    try:
        return pickle.load(open(path, 'rb'))
    except FileNotFoundError:
        st.error(f"Error: Model file not found at {path}")
        return None

models = {
    'Parkinsons': load_model("D:\medicaldiagnosis\parkinsons_model.sav"),
    'Heart Disease': load_model("D:\medicaldiagnosis\Heart_disease__model.sav"),
    'Lung Cancer': load_model("D:\medicaldiagnosis\LungCancer__model.sav")
}

# Disease selection
st.markdown("Select a Disease to Predict")
selected = st.selectbox(
    '',
    ['Parkinsons Prediction', 'Heart Disease Prediction', 'Lung Cancer Prediction']
)

def display_input(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1)

# Parkinson's Prediction
if selected == "Parkinsons Prediction" and models['Parkinsons']:
    st.markdown("Parkinson's Disease Prediction")
    st.markdown("Enter the following details:")
    
    inputs = [
        display_input("MDVP:Fo(Hz)", "Fundamental frequency", "fo"),
        display_input("MDVP:Fhi(Hz)", "Highest fundamental frequency", "fhi"),
        display_input("MDVP:Flo(Hz)", "Lowest fundamental frequency", "flo"),
        display_input("MDVP:Jitter(%)", "Jitter percentage", "jitter"),
        display_input("MDVP:Jitter(Abs)", "Absolute jitter", "jitter_abs"),
        display_input("MDVP:RAP", "Relative amplitude perturbation", "rap"),
        display_input("MDVP:PPQ", "Pitch period perturbation quotient", "ppq"),
        display_input("Jitter:DDP", "Divergence from DDP", "ddp"),
        display_input("MDVP:Shimmer", "Shimmer value", "shimmer"),
        display_input("MDVP:Shimmer(dB)", "Shimmer in dB", "shimmer_db"),
        display_input("Shimmer:APQ3", "Three-point Amplitude Perturbation Quotient", "apq3"),
        display_input("Shimmer:APQ5", "Five-point Amplitude Perturbation Quotient", "apq5"),
        display_input("MDVP:APQ", "MDVP Amplitude Perturbation Quotient", "apq"),
        display_input("Shimmer:DDA", "Average absolute differences of differences", "dda"),
        display_input("NHR", "Noise-to-Harmonics Ratio", "nhr"),
        display_input("HNR", "Harmonics-to-Noise Ratio", "hnr"),
        display_input("RPDE", "Recurrence period density entropy", "rpde"),
        display_input("DFA", "Detrended fluctuation analysis", "dfa"),
        display_input("spread1", "First spread measure", "spread1"),
        display_input("spread2", "Second spread measure", "spread2"),
        display_input("D2", "Correlation dimension", "d2"),
        display_input("PPE", "Pitch period entropy", "ppe")
    ]
    
    if st.button("Predict Parkinson's"):
        result = models['Parkinsons'].predict([np.array(inputs)])
        st.success("Positive for Parkinson's" if result[0] == 1 else "Negative for Parkinson's")

# Heart Disease Prediction
elif selected == "Heart Disease Prediction" and models['Heart Disease']:
    st.markdown("Heart Disease Prediction")
    st.markdown("Enter the following details:")
    
    inputs = [
        display_input('Age', 'Enter age of the person', 'age'),
        display_input('Sex', '1 = male, 0 = female', 'sex'),
        display_input('Chest Pain types', 'Type (0-3)', 'cp'),
        display_input('Resting Blood Pressure', 'Blood pressure', 'trestbps'),
        display_input('Serum Cholesterol', 'mg/dl', 'chol'),
        display_input('Fasting Blood Sugar', '>120 mg/dl (1 = true, 0 = false)', 'fbs'),
        display_input('Resting ECG', 'ECG results (0-2)', 'restecg'),
        display_input('Max Heart Rate', 'Achieved', 'thalach'),
        display_input('Exercise-Induced Angina', '1 = Yes, 0 = No', 'exang'),
        display_input('Oldpeak', 'ST depression', 'oldpeak'),
        display_input('Slope', 'Slope value (0-2)', 'slope'),
        display_input('Major Vessels', 'Number (0-3)', 'ca'),
        display_input('Thalassemia', 'Type (0-3)', 'thal')
    ]
    
    if st.button("Predict Heart Disease"):
        result = models['Heart Disease'].predict([np.array(inputs)])
        st.success("Positive for Heart Disease" if result[0] == 1 else "Negative for Heart Disease")

# Lung Cancer Prediction
elif selected == "Lung Cancer Prediction" and models['Lung Cancer']:
    st.markdown("Lung Cancer Prediction")
    st.markdown("Enter the following details:")
    
    inputs = [
        display_input("Age", "Enter age of the person", "lc_age"),
        display_input("Gender", "1 = Male, 0 = Female", "gender"),
        display_input("Smoking", "1 = Yes, 0 = No", "smoke"),
        display_input("Yellow Fingers", "1 = Yes, 0 = No", "yellow_fingers"),
        display_input("Chest Pain", "1 = Yes, 0 = No", "chest_pain"),
        display_input("Anxiety", "1 = Yes, 0 = No", "anxiety"),
        display_input("Peer Pressure", "1 = Yes, 0 = No", "peer_pressure"),
        display_input("Chronic Disease", "1 = Yes, 0 = No", "chronic_disease"),
        display_input("Fatigue", "1 = Yes, 0 = No", "fatigue"),
        display_input("Allergy", "1 = Yes, 0 = No", "allergy"),
        display_input("Wheezing", "1 = Yes, 0 = No", "wheezing"),
        display_input("Alcohol Consumption", "1 = Yes, 0 = No", "alcohol"),
        display_input("Coughing Blood", "1 = Yes, 0 = No", "coughing_blood"),
        display_input("Swallowing Difficulty", "1 = Yes, 0 = No", "swallowing_diff"),
        display_input("Shortness of Breath", "1 = Yes, 0 = No", "short_breath")
    ]
    
    if st.button("Predict Lung Cancer"):
        result = models['Lung Cancer'].predict([np.array(inputs)])
        st.success("Positive for Lung Cancer" if result[0] == 1 else "Negative for Lung Cancer")
