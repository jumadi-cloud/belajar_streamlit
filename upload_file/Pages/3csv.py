# Import Library
import streamlit as st
import pandas as pd


st.subheader("Halaman CSV")
st.write(
            """
            Di dalam Halaman CSV akan mempelajari bagaimana caranya Upload file dan Membaca File dengan _type CSV_.
            
            Dalam tutorial ini sebenernya sudah pernah kita bahas 
            di [video](https://www.youtube.com/watch?v=SX-4STwpFQA&lc=Ugw6TKYhoPmV0bVyHFl4AaABAg) 
            dan ini adalah materi lanjutannya 
            """
        )

data_file = st.file_uploader("Upload CSV",type=["csv"])
if data_file is not None:
    st.write(type(data_file))
    file_details = {"Filename":data_file.name,
    "FileType":data_file.type,"FileSize":data_file.size}
    st.write(file_details)
    df = pd.read_csv(data_file)
    st.dataframe(df)