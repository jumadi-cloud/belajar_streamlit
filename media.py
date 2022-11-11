# import module
import streamlit as st
from PIL import Image


# Title
st.title("Kelas Awan Pintar")

# Header
st.header("Ayu Belajar Bagaimana Cara untuk menampilkan Media elements di streamlit [sumber](https://docs.streamlit.io/library/api-reference/media)")

st.markdown("""
### 

1. Image

2. Audio

3. Video

========================= Contohnya =====================================
""",True)
# Image
image = Image.open('image/foto1.png')
st.image(image)

# Audio
image1 = Image.open('image/foto2.png')
st.image(image1)

# Video
image3 = Image.open('image/foto3.png')
st.image(image3)
st.text('============menampilkan Media elements di streamlit============')
# ============***============

# Cara untuk menampilkan Media elements di streamlit 
# 1. Image
gambar1 = Image.open('image/logo.png')
gambar2 = Image.open('image/test1.png')
gambar3 = Image.open('image/test2.jpeg')
gambar4 = Image.open('image/deploy.png')
# Fungsi untuk menapilkan audio di aplikasi streamlit 
st.image(gambar1, caption='ini logo streamlit')

# Contoh untuk menampilkan gambar lebih dari 1 menggunakan colom
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Gambar 1")
   st.image(gambar2)

with col2:
   st.header("Gambar 2")
   st.image(gambar3)

with col3:
   st.header("Gambar 3")
   st.image(gambar4)

# 2. Audio
audio = open('image/audio1.oga', 'rb')
testaudio = audio.read()

# Fungsi untuk menapilkan audio di aplikasi streamlit 
st.audio(testaudio)

# 3. Video
video = open('image/star.mp4', 'rb')
testvideo = video.read()

# Fungsi untuk menapilkan video di aplikasi streamlit 
st.video(testvideo)

# Contoh untuk menampilkan video lebih dari 1 menggunakan colom
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Introduction di Aplikasi Streamlit")
   st.video('https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l')

with col2:
   st.header("Cara menampilkan teks")
   st.video('https://www.youtube.com/watch?v=tPA0x_wToXQ&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=2')

with col3:
   st.header("Cara Menampilkan Data")
   st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')


