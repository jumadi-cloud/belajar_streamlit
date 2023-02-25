# Import Library
import streamlit as st
from PIL import Image
import os

st.subheader("Halaman Image")
st.write(
            """
            Di dalam Halaman Image akan mempelajari bagaimana caranya Upload file dan Membaca File dengan _type_ Gambar _(png, jpeg, jpg)_.
            
            Dalam tutorial ini sebenernya sudah pernah kita bahas 
            di [video](https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8) 
            dan ini adalah materi lanjutannya
            """
        )

# method atau fungsi load image
def load_image(image_file):
    img = Image.open(image_file)
    return img
    
image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
if image_file is not None:
    st.write(type(image_file))
    file_details = {"Filename":image_file.name,
    "FileType":image_file.type,"FileSize":image_file.size}
    st.write(file_details)

    # Menampilkan Image 
    img = load_image(image_file)
    st.image(img, width=350)
    
    # Save File
    with open(os.path.join("Documents/Image",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())

    st.success("File berhasil disave")

    # Download
    st.download_button(label='Download File',
                       data=image_file,
                       file_name='My Documents.png')



