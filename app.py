import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Set Page Config
st.set_page_config(page_title="Disease Prediction", page_icon="🩺")

# Hide Streamlit Style
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Background Image
background_image_url = "https://static.vecteezy.com/system/resources/thumbnails/009/213/272/small/healthcare-and-medical-background-with-cardiogram-line-free-vector.jpg"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to load model
def load_model(path):
    with open(path, "rb") as file:
        return pickle.load(file)

# Load models
models = {
    'Parkinsons Prediction': load_model("D:/medicaldiagnosis/parkinsons_model.sav"),
    'Heart Disease Prediction': load_model("D:\medicaldiagnosis\Heart_disease__model.sav"),
    'Lung Cancer Prediction': load_model("D:\medicaldiagnosis\LungCancer__model.sav"),
}

# Disease selection
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Parkinsons Prediction', 'Heart Disease Prediction', 'Lung Cancer Prediction']
)

# Function for input fields
def display_input(label, tooltip, key, type="text"):
    if type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)
    return st.text_input(label, key=key, help=tooltip)

# Parkinson's Prediction
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction")
    st.write("Enter the following details:")

    fo = display_input("MDVP:Fo(Hz)", "Fundamental frequency", "fo", "number")
    fhi = display_input("MDVP:Fhi(Hz)", "Highest fundamental frequency", "fhi", "number")
    flo = display_input("MDVP:Flo(Hz)", "Lowest fundamental frequency", "flo", "number")
    jitter = display_input("MDVP:Jitter(%)", "Jitter percentage", "jitter", "number")
    jitter_abs = display_input("MDVP:Jitter(Abs)", "Absolute jitter", "jitter_abs", "number")
    rap = display_input("MDVP:RAP", "Relative amplitude perturbation", "rap", "number")
    ppq = display_input("MDVP:PPQ", "Pitch period perturbation quotient", "ppq", "number")
    ddp = display_input("Jitter:DDP", "Divergence from DDP", "ddp", "number")
    shimmer = display_input("MDVP:Shimmer", "Shimmer value", "shimmer", "number")
    shimmer_db = display_input("MDVP:Shimmer(dB)", "Shimmer in dB", "shimmer_db", "number")
    apq3 = display_input("Shimmer:APQ3", "Three-point Amplitude Perturbation Quotient", "apq3", "number")
    apq5 = display_input("Shimmer:APQ5", "Five-point Amplitude Perturbation Quotient", "apq5", "number")
    apq = display_input("MDVP:APQ", "MDVP Amplitude Perturbation Quotient", "apq", "number")
    dda = display_input("Shimmer:DDA", "Average absolute differences of differences", "dda", "number")
    nhr = display_input("NHR", "Noise-to-Harmonics Ratio", "nhr", "number")
    hnr = display_input("HNR", "Harmonics-to-Noise Ratio", "hnr", "number")
    rpde = display_input("RPDE", "Recurrence period density entropy", "rpde", "number")
    dfa = display_input("DFA", "Detrended fluctuation analysis", "dfa", "number")
    spread1 = display_input("spread1", "First spread measure", "spread1", "number")
    spread2 = display_input("spread2", "Second spread measure", "spread2", "number")
    d2 = display_input("D2", "Correlation dimension", "d2", "number")
    ppe = display_input("PPE", "Pitch period entropy", "ppe", "number")

    if st.button("Predict Parkinson's Disease"):
        prediction = models['Parkinsons Prediction'].predict([[fo, fhi, flo, jitter, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(result)

# Heart Disease Prediction
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    st.write("Enter the following details:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex', '1 = male, 0 = female', 'sex', 'number')
    cp = display_input('Chest Pain types', 'Type (0-3)', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol', 'mg/dl', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar', '>120 mg/dl (1 = true, 0 = false)', 'fbs', 'number')
    restecg = display_input('Resting ECG', 'ECG results (0-2)', 'restecg', 'number')
    thalach = display_input('Max Heart Rate', 'Achieved', 'thalach', 'number')
    exang = display_input('Exercise-Induced Angina', '1 = Yes, 0 = No', 'exang', 'number')
    oldpeak = display_input('Oldpeak', 'ST depression', 'oldpeak', 'number')
    slope = display_input('Slope', 'Slope value (0-2)', 'slope', 'number')
    ca = display_input('Major Vessels', 'Number (0-3)', 'ca', 'number')
    thal = display_input('Thalassemia', 'Type (0-3)', 'thal', 'number')


    if st.button("Predict Heart Disease"):
        prediction = models['Heart Disease Prediction'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        result = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
        st.success(result)

# Lung Cancer Prediction
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer Prediction")
    st.write("Enter the following details:")

    age = display_input("Age", "Enter age of the person", "lc_age", "number")
    gender = display_input("Gender", "1 = Male, 0 = Female", "gender", "number")
    smoke = display_input("Smoking", "1 = Yes, 0 = No", "smoke", "number")
    yellow_fingers = display_input("Yellow Fingers", "1 = Yes, 0 = No", "yellow_fingers", "number")
    chest_pain = display_input("Chest Pain", "1 = Yes, 0 = No", "chest_pain", "number")
    anxiety = display_input("Anxiety", "1 = Yes, 0 = No", "anxiety", "number")
    peer_pressure = display_input("Peer Pressure", "1 = Yes, 0 = No", "peer_pressure", "number")
    chronic_disease = display_input("Chronic Disease", "1 = Yes, 0 = No", "chronic_disease", "number")
    fatigue = display_input("Fatigue", "1 = Yes, 0 = No", "fatigue", "number")
    allergy = display_input("Allergy", "1 = Yes, 0 = No", "allergy", "number")
    wheezing = display_input("Wheezing", "1 = Yes, 0 = No", "wheezing", "number")
    alcohol = display_input("Alcohol Consumption", "1 = Yes, 0 = No", "alcohol", "number")
    coughing_blood = display_input("Coughing Blood", "1 = Yes, 0 = No", "coughing_blood", "number")
    swallowing_diff = display_input("Swallowing Difficulty", "1 = Yes, 0 = No", "swallowing_diff", "number")
    short_breath = display_input("Shortness of Breath", "1 = Yes, 0 = No", "short_breath", "number")


    if st.button("Predict Lung Cancer"):
        prediction = models['Lung Cancer Prediction'].predict([[age,gender,smoke,yellow_fingers,chest_pain,anxiety,peer_pressure,chronic_disease,fatigue,allergy,wheezing,alcohol,coughing_blood,swallowing_diff,short_breath]])
        result = "The person has lung cancer" if prediction[0] == 1 else "The person does not have lung cancer"
        st.success(result)
