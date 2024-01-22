import streamlit as st
import eda
import prediction

navigasi = st.sidebar.selectbox('Pilih Halaman :', 
                                ('Model Prediksi', 'EDA'))

if navigasi == 'Model Prediksi':
    prediction.run()
else :
    eda.run()