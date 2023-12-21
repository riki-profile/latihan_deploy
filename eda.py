# import library
import pandas as pd 
import numpy as np
import streamlit as st 

# library for visualization
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

# Set the title
st.title('FIFA 2022 Player Rating')

# Set subheader
st.subheader('Halaman ini menampilkan hasil EDA')

# Upload gambar
st.image('https://static.zawya.com/view/acePublic/alias/contentid/MzEzYmU0NjgtMTdhMC00/2/fbl-wc-2022-match58-cro-bra.webp?f=3%3A2&q=0.75&w=828',
         caption='test gambar')

# garis horizontal
st.write('---')

# Subjudul
st.write('## Dataframe')

# loading dataset
df = pd.read_csv('dataset.csv')

# menampilkan dataframe
st.dataframe(df)
st.write('---')

# Bab Visualisasi
st.write('## EDA')

# Judul visualisasi
st.write('### Histogram Attacking Work Rate')

# Buat Canvasnya
fig = plt.figure(figsize=(15,10))

# Visualisasinya
sns.countplot(x='AttackingWorkRate', data= df)

# syntax streamlit untuk menampilkan grafik
st.pyplot(fig)


# Visualisasi ke-dua
st.write('### Grafik Distribusi')
opsi = st.selectbox('Pilih Kolom : ', ('Age', 'Height', 'Weight', 'ValueEUR'))

fig = plt.figure(figsize=(15,10))
sns.histplot(df[opsi], bins=20, kde=True)
st.pyplot(fig)

# Visualisasi ke-tiga
st.write('### Plotly Plot')
# fig = plt.figure(figsize=(10,10))
gambar = px.scatter(df, x='ValueEUR', y='Overall', hover_data=['Age', "Height"])
st.plotly_chart(gambar) # khusus plotly
