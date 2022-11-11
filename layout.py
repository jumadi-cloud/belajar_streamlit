# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image



# Cara untuk membuat sidebar dan Navigation di streamlit 

# Contoh sidebar dan Navigation

# # Sidebar Radio
# test = st.sidebar.radio("Navigation", ['Home', 'About us', 'Contact us'])

# # Sidebar Selectbox
# st.sidebar.selectbox("Navigation", ['NLP', 'Streamlit', 'Flask', 'DS'])

# # Sidebar Multiselect
# st.sidebar.multiselect("Navigation", ['NLP', 'Streamlit', 'Flask', 'DS'])

# # Sidebar Input Number
# st.sidebar.number_input("Pilih Number:", 1,10)

# # Sidebar Radio Number
# st.sidebar.radio(label="Navigation", options=[10,20,30])

# # Sidebar File Uploader
# st.sidebar.file_uploader("Upload file", type=['Cv', 'txt'])

test = st.sidebar.radio("Navigation", ['Home', 'About us', 'Contact us'])

if test == "Home":
    st.subheader("Hai, saya Jumadi :wave:")
    st.title("Saya Seorang coach artificial intelligence dari Indonesia")
    st.write(
        "Saya bersemang untuk menggunakan Streamlit lebih efisien dan efektif dalam bisnis."
    )
    st.write("[Pelajari Lebih Lanjut](https://kelasawanpintar.netlify.app/)")

    st.write("---")

    st.header("Apa yang saya lakukan")
    st.write("##")
    st.write(
            """
            Di Channel YouTube saya, saya membuat tutorial untuk orang-orang yang:
            - sedang mencari cara untuk belajar Python.
            - sedang mencari cara untuk belajar Streamlit.
            - ingin belajar Analisis Data & Ilmu Data untuk melakukan analisis.
            - ingin belajar Artificial Intelligence, Data Science, Machine Learning, Natural Language Processing.
            - ingin belajar dunia IT
            - Jika ingin terhubung di [Linkedin](https://www.linkedin.com/in/jumadi-01/)


            Jika Channel YouTube saya menarik bagi Anda, jangan lupa untuk berlangganan dan menyalakan notifikasi, agar Anda tidak ketinggalan konten apa pun.
            
            [Channel YouTube](https://www.youtube.com/channel/UC7rCdlKnMTt26Q3np3rW1Iw)
            """
        )
    st.header("Playlist Fundamental Streamlit")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Introduction di Aplikasi Streamlit")
        st.video('https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l')

    with col2:
        st.subheader("Cara menampilkan teks")
        st.video('https://www.youtube.com/watch?v=tPA0x_wToXQ&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=2')

    with col3:
        st.subheader("Cara Menampilkan Data")
        st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')
    
    st.write("---")