import streamlit as st
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LogisticRegression

# Load data
heart_data = pd.read_csv("heart_cleveland.csv")


# Define features and target variable
X = heart_data.drop(columns='condition', axis=1)
Y = heart_data['condition']

# Train model
model = LogisticRegression()
model.fit(X, Y)

# Create Streamlit app
st.title("Prediksi Penyakit Jantung ")
st.write("Masukkan nilai-nilai berikut untuk melakukan prediksi:")

# Create input fields for features

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Usia:")
with col2:
    sex = st.selectbox("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
if sex == "Laki-laki":
    sex = 1
else:
    sex = 0
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

# Create prediction button
if st.button("Prediksi"):
    # Create input vector
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display prediction
    if prediction >= 0.0:
        st.write("Anda berpotensi mengidap penyakit jantung.")
    else:
        st.write("Anda tidak berpotensi mengidap penyakit jantung.")
