# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import plotly_express as px

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

test = st.sidebar.radio("Navigation", ['Home', 'Columns', 'Tabs', 'expander & container'])

if test == "Home":
    st.subheader("Hai, Sahabat Kelas Awan Pintar :wave:")
    
    st.write(
        "Saya bersemangat untuk menggunakan Streamlit lebih efisien dan efektif dalam bisnis."
    )
    st.write("[Website Kelas Awan Pintar](https://kelasawanpintar.netlify.app/)")

    st.write("---")

    st.header("Apa yang saya lakukan")
    st.write("##")
    st.write(
            """
            Di Channel YouTube Kelas Awan Pintar, kita akan membuat tutorial untuk orang-orang yang:
            - sedang mencari cara untuk belajar Python.
            - sedang mencari cara untuk belajar Streamlit.
            - ingin belajar Analisis Data & Ilmu Data untuk melakukan analisis.
            - ingin belajar Artificial Intelligence, Data Science, Machine Learning, Natural Language Processing.
            - ingin belajar dunia IT
            - Jika ingin terhubung di [Linkedin](https://www.linkedin.com/in/jumadi-01/)
            - Jika ingin gabung di group telegram [Kelas Awan Pintar](https://t.me/+CdyAL5WlRVNjOGM1)


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

# Halaman Columns

# Contoh (data berupa dataset)
if test == "Columns":
    st.subheader("Hai, Sahabat Kelas Awan Pintar :wave:")
    st.write("Kita akan belajar di halaman ini menngunakan fungsi Coloum")

    col1, col2 = st.columns([3, 1])
    data = pd.read_csv("dataset/datagaji1.csv") # Pengambilan data


    col1.subheader("Menapilkan data dengan grafik")
    col1.line_chart(data)

    col2.subheader("Menapilkan data dengan tabel")
    col2.write(data)

# Halaman Tabs

if test == "Tabs":
    st.subheader("Hai, Sahabat Kelas Awan Pintar :wave:")
    st.write("Kita akan belajar di halaman ini menngunakan fungsi tabs")

    # Contoh yang pertama (data berupa gambar)
    tab1, tab2, tab3 = st.tabs(["Gambar 1", "Gambar 2", "Gambar 3"])

    # Pengambilan data
    gambar2 = Image.open('image/logo.png')
    gambar3 = Image.open('image/test1.jpeg')
    gambar4 = Image.open('image/deploy.png')

    with tab1:
        st.header("Gambar 1")
        st.image(gambar2, width=200)
    with tab2:
        st.header("Gambar 2")
        st.image(gambar3, width=200)

    with tab3:
        st.header("Gambar 3")
        st.image(gambar4, width=200)

    
    st.write("---")
    
    # Contoh yang kedua (data berupa dataset)
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = pd.read_csv("dataset/datagaji1.csv") # Pengambilan data

    tab1.subheader("Menapilkan data dengan chart")
    tab1.line_chart(data)

    tab2.subheader("Menapilkan data dengan tabel")
    tab2.write(data)

# Halaman expander & container

if test == "expander & container":
    st.subheader("Hai, Sahabat Kelas Awan Pintar :wave:")
    st.write("Kita akan belajar di halaman ini menngunakan fungsi expander & container")

    # Pemngambilan data
    data = pd.read_csv("dataset/datagaji1.csv")
    gambar = Image.open('image/logo.png')

    # Contoh Expander
    st.bar_chart(data)
    with st.expander("Ini adalah expander"):
        st.write("""
        Ini contoh dari expander dan
        kita akan mencoba visualisasikan data gaji
        """)
        st.image(gambar)

    # Contoh Container
    with st.container():
        st.write("Ini contoh dari container")
        st.bar_chart(data)

    st.write("ini Bukan container")

    