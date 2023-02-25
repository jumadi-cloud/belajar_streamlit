import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Upload File",
    page_icon="👋",
)

st.title("Home")
st.sidebar.success("Pilih halaman di atas.")

st.subheader("Hai, Sahabat Kelas Awan Pintar :wave:")
    
# st.write(
#         "Saya bersemangat untuk menggunakan Streamlit lebih efisien dan efektif dalam bisnis."
#     )
st.write("[Website Kelas Awan Pintar](https://kelasawanpintar.netlify.app/)")

st.write("---")

st.header("🧑‍🎓 Topik Pembahasan ")
st.write("##")
st.write(
            """
            Di Dalam tutorial kali ini kita akan mempelajari bagaimana caranya upload file:
            - Upload file dengan _type_ Gambar _(png, jpeg, jpg)_.
            - Upload file dengan _type_ CSV.  
            - Upload file dengan _type_ TXT.
            - Upload file dengan _type_ DOC. [Library](https://pypi.org/project/docx2txt/)
            - Upload file dengan _type_ PDF. [Library](https://pypi.org/project/PyPDF2/)


            Sumber:

            Tutorial ini terinspirasi dan diadaptasi dari artikel berikut:
            [Blog](https://blog.jcharistech.com/2020/11/08/working-with-file-uploads-in-streamlit-python/)
            """
        )
st.header("Topologi Upload file dan Save data atau file dengan Streamlit")
top1 = Image.open('Documents/Topologi.png')
top2 = Image.open('Documents/Topologi Save.png')
top3 = Image.open('Documents/struktur folder.png')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Topologi Upload File")
   st.image(top1)

with col2:
   st.header("Topologi Save Data atau File")
   st.image(top2)

with col3:
   st.header("Struktur Folder")
   st.image(top3)

st.write("---")