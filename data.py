
# import module
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Kelas Awan Pintar")
st.markdown("""
### Pada pertemuan kali ini kita akan membahas bagaimana caranya menapilkan data di Streamlit

Jika temen temen belum Install library Pandas dan Numpy di Streamlit

Cara insatll Pandas: pip install pandas [sumber](https://pypi.org/project/pandas/)

Cara insatll Numpy: pip install numpy [sumber](https://pypi.org/project/numpy/)

### Pembahasan

- Cara Membuat Array 

- Membuat tipe data series

- Cara menampilkan dataset dari local dan dari Github

====================================================================================
""",True)

# Header
st.header("Ayu Belajar Bagaimana Menapilkan Data di streamlit [sumber](https://docs.streamlit.io/library/api-reference/data)")

#Buat data 

# Contoh Membuat Data Array
a = np.array([1,2,3,4])
b = np.array([(1.2,1,2.2),(1.1,2,2.2)],dtype=float)

# Membuat tipe data series
u = pd.Series([1,2,3,4,5,6,7])

# Cara Mengambil dataset dari Github
datset = pd.read_csv("https://raw.githubusercontent.com/jumadi-cloud/Fundamental-Python/main/Dataset/datagaji1.csv")

# Membuat data Dictionary
profil = {
    'nama': 'Ucup',
    'umur': '21',
    'pemrograman': ['Python','streamlit','JS'],
    'favorit': {
        'makanan':'Indome',
        'hobi': 'rebahan'
    }
}

# ============***============
# Cara menapilkan data 

# Dataframe
st.text("ini dataframe")
st.dataframe(b)
st.dataframe(u)
st.dataframe(datset)

# Tabel
st.text("Data tabel")
st.table(a)
st.table(datset)

# Json
st.text("Data Jsn")
st.json(profil)


# Matric
st.text("ini data matric")

st.metric(label="Gas price", value=5, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")