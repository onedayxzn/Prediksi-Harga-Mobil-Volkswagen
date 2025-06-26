import streamlit as st
import pandas as pd
import joblib

model_knn = joblib.load("model/knn.pkl")
scaler = joblib.load("model/scaler.pkl")
X_columns = joblib.load("model/X_train_columns.pkl")
pca = joblib.load("model/pca_model.pkl")  


st.header("Prediksi Harga Mobil Volkswagen Bekas")
st.write("Masukkan detail mobil di bawah ini:")


year = st.number_input("Tahun Registrasi", 2000, 2020, step=1)
mileage = st.number_input("Jarak Tempuh (miles)", 0, 200000, step=1000)
tax = st.number_input("Pajak (GBP)", 0, 2000, step=10)
mpg = st.number_input("Miles per Gallon", 10, 200, step=1)
engine_size = st.number_input("Ukuran Mesin (CC)", 500, 5000, step=10) / 1000
model = st.selectbox("Model", ["UP", "T-Roc", "T-Cross", "Scirocco", "Polo", "Passat", "Jetta", "Golf", "CC", "Arteon"])
fuelType = st.selectbox("Bahan Bakar", ["Petrol", "Diesel", "Hybrid"])
transmission = st.selectbox("Transmisi", ["Manual", "Automatic", "Semi-Auto"])

if st.button("Prediksi Harga"):
    input_data = pd.DataFrame({
        'model': [model],
        'year': [year],
        'transmission': [transmission],
        'mileage': [mileage],
        'fuelType': [fuelType],
        'tax': [tax],
        'mpg': [mpg],
        'engineSize': [engine_size]
    })

    # Transformasi PCA ke fitur
    input_data['fitur'] = pca.transform(input_data[['engineSize', 'tax']])
    input_data.drop(['engineSize', 'tax'], axis=1, inplace=True)


    input_data = pd.get_dummies(input_data, columns=['model', 'transmission', 'fuelType'], drop_first=True)

    for col in X_columns:
        if col not in input_data.columns:
            input_data[col] = 0


    input_data = input_data[X_columns]


    numeric_features = ['year', 'fitur']
    input_data[numeric_features] = scaler.transform(input_data[numeric_features])

    # Prediksi
    prediction = model_knn.predict(input_data)[0]
    st.success(f"Harga estimasi mobil bekas tersebut adalah ${prediction:.2f}")
