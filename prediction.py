# import library
import pandas as pd 
import numpy as np
import streamlit as st 

# import pickle
import pickle

# Set title
st.title("Model Prediction")
st.write('---')

# upload banner
st.image('https://img.id.my-best.com/content_section/choice_component/sub_contents/983d2cc08a9be37b1e6e352a5450b2ef.jpg?ixlib=rails-4.3.1&q=70&lossless=0&w=690&fit=max&s=7cad8e9899ab38da31f5a30ccd4012bd',
         caption = 'contoh banner')

# membuat deskripsi
st.write('Halaman ini akan lebih berfokus pada model deployment, \
         dimana user dapat melakukan prediksi terhadap data')

with st.form(key='form parameters'):
    name = st.text_input('Nama :')
    age = st.number_input('Usia :', min_value=16)
    weigth = st.number_input('Berat Badan : ', min_value=40, step=5)
    heigth = st.slider('Tinggi Bandan :', 130, 200, 180)
    price = st.number_input('Nilai Pemain :', min_value=3000)
    attack = st.selectbox('Level Attack :', ('Low', 'Medium', 'High'))
    defense = st.selectbox('Level defense :', ('Low', 'Medium', 'High'))
    pace = st.number_input('Pace', min_value=0)
    shoot = st.number_input('Shooting', min_value=0)
    dribble = st.number_input('Dribbling', min_value=0)
    defend = st.number_input('Defending', min_value=0)
    physic = st.number_input('Physicality', min_value=0)
    passing = st.number_input('Passing Ability', min_value=0)

    submit = st.form_submit_button('Predict')

data_baru = {
 'Name': name,
 'Age' : age,
 'Height': heigth,
 'Weight': weigth,
 'ValueEUR': price,
 'AttackingWorkRate': attack,
 'DefensiveWorkRate': defense,
 'PaceTotal': pace,
 'ShootingTotal': shoot,
 'PassingTotal': passing,
 'DribblingTotal': dribble,
 'DefendingTotal': defend,
 'PhysicalityTotal': physic,
}

data_inf = pd.DataFrame([data_baru])
st.dataframe(data_inf)

with open('model_fifa.pkl', 'rb') as file:
    model = pickle.load(file)

if submit:
    score = model.predict(data_inf)
    st.write('# Rating Overall Anda :', str(int(score)))