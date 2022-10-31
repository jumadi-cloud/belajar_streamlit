# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# Title
st.title("Kelas Awan Pintar")

# Header
st.header("Ayu Belajar Bagaimana Cara Buat widgets di streamlit [sumber](https://docs.streamlit.io/library/api-reference/widgets)")

st.markdown("""
### 

1. Button

2. Checkbox

3. radio button

4. Selectbox

5. Multiselect

6. Slider & Select-slider

7. Input Text 

8. Input Number 

9. Text area

10. Date input

11. Time input

12. File Uploader

13. Color picker

====================================================================================
""",True)

# ============***============
# Cara Buat widgets di streamlit 


# 1. Create button
if(st.button("Kelas Awan Pintar")):
	st.text("Welcome To Playlist Belajar Fundamental Streamlit")

# 2. Create Checkbox
if st.checkbox("Show/Hide"):
	st.text("Hai Sahabat Kelas Awan Pintar, Salam Keep Learning Temen temen")

# 3. Create radio button
status = st.radio("Pilih Playlist: ", ('NLP', 'Streamlit', 'Flask'))
st.write("Sahabat Kelas Awan Pintar Siap belajar:", status)

# 4. Create Selection box
domain = st.selectbox("Sahabat Kelas Awan Pintar Siap belajar: ",
					['NLP', 'Streamlit', 'Flask', 'DS'])
# print(Menapilkan)
st.write("Sahabat Kelas Awan Pintar Siap belajar: ", domain)

# 5. Create Multiselect
domain = st.multiselect("Sahabat Kelas Awan Pintar Siap belajar: ", 
	['NLP', 'Streamlit', 'Flask', 'DS'])
# print(Menapilkan)
st.write("Sahabat Kelas Awan Pintar Saat ini sedang belajar", len(domain), 'Playlist')

# 6. Create slider
lavel = st.slider("Pilih lavel",1,15)

st.text('Dipilih:{}'.format(lavel))

# 6. Create Select-slider
hari = st.select_slider('Pilih nama nama hari',
options=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu'])

st.write('Hari kesukaan kamu:',hari)

# 7. Create Input Text
test1 = st.text_input("Silahkan input text","")

st.write('kamu sudah berhasil menginput:',test1)

# 8. Create Input Number
test2 = st.number_input("Silahkan input number",1,10)

st.write('kamu sudah berhasil menginput number:',test2)

# 9. Create Input Text Area
test3 = st.text_area('Silahkan masukan text',"")

st.write('kamu sudah berhasil menginput text area',test3)

# 10. Create Input Date
st.date_input("silahkan input date")

# 11. Create Time Input
st.time_input("silahkan masukan waktu")

# 12. Create File Uploader
st.file_uploader("Upload file",type=["csv","txt"])

# 13 Create Color picker
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)