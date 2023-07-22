import pickle
import streamlit as st

#membaca model 
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

#membagi kolom
col1, col2 =st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')

with col2:
    Glucose = st.text_input('Input nilai Glucose')

with col1:
    BloodPressure = st.text_input('Input nilai BloodPressure')

with col2:
    SkinThickness = st.text_input('Input nilai SkinThickness')

with col1:
    Insulin = st.text_input('Input niali Insulin')

with col2:
    BMI = st.text_input('Input nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai DiabetesPedigreeFunction')

with col2:
    Age = st.text_input('Input nilai Age')

#code untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age]])
    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena diabetes'

    st.success(diab_diagnosis)
    

