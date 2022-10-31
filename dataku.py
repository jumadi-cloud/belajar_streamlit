# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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


# 2. Audio


# 3. Video

