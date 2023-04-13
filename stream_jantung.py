import pickle
import streamlit as st
import numpy as np
import sklearn


# Load data
with open('penyakit_jantung.sav', 'rb') as f:
    model = pickle.load(f)


# Create Streamlit app
st.title("Prediksi Penyakit Jantung ")
st.write("Masukkan nilai-nilai berikut untuk melakukan prediksi:")

# Create input fields for features

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Usia:")
with col2:
    sex = st.number_input("Jenis Kelamin:")
with col3:
    cp = st.number_input("Tipe Nyeri Dada:")
with col1:
    trestbps = st.number_input("Tekanan Darah saat Istirahat:")
with col2:
    chol = st.number_input("Kolesterol Serum:")
with col3:
    fbs = st.number_input("Gula Darah Puasa:")
with col1:
    restecg = st.number_input("Elektrokardiogram Saat Istirahat:")
with col2:
    thalach = st.number_input("Denyut Jantung Maksimal:")
with col3:
    exang = st.number_input("Latihan Menyebabkan Nyeri Dada:")
with col1:
    oldpeak = st.number_input("Depresi ST Yang Diamati pada Latihan:")
with col2:
    slope = st.number_input("Slope pada Latihan:")
with col3:
    ca = st.number_input("Jumlah Pembuluh Darah Utama Berwarna:")
with col1:
    thal = st.number_input("Thalassemia:")
    
# code for prediction
heart_diagnosis =''

# Create prediction button
if st.button("Prediksi Penyakit Jantung"):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    if (heart_prediction[0] ==1):
        heart_diagnosis = 'Pasien berpotensi mengidap penyakit jantung.'
    else:
        heart_diagnosis = 'Pasien tidak berpotensi mengidap penyakit jantung.'
 
st.success(heart_diagnosis)
