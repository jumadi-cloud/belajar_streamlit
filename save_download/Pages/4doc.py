# Import Library
import streamlit as st
import docx2txt #library txt atau docu
from PyPDF2 import PdfFileReader #library pdf
import os

st.subheader("Halaman Document")
st.write(
            """
            Di dalam Halaman Document akan mempelajari bagaimana caranya Upload file dan Membaca File dengan _type  TXT, DOC, PDF_.
            
            Dalam tutorial kali ini menjawab dari pertanyaan temen teme 
            yang bertanya Bagaimana caranya kalau data kita berbentuk  
            **TXT, DOC, PDF** dan Keep Learning temen temen 🧑‍🎓
            """
        )

# method atau fungsi load pdf
def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()
	return all_page_text

# Method atau fungsi save file
def save_upload(uploadedfile):
    with open(os.path.join("Documents/DataPdf",uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        return st.success("File berhasil disave: {} in Documents".format(uploadedfile.name))


doc_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
if st.button("Proses"):
    if doc_file is not None:
        file_details = {"Filename":doc_file.name,
        "FileType":doc_file.type,"FileSize":doc_file.size}
        st.write(file_details)
        # Documents file type txt
        if doc_file.type == "text/plain":
            raw_text = str(doc_file.read(),"utf-8")
            # st.write(raw_text)
            st.text(raw_text)

            # Save File
            save_upload(doc_file)

            # Dowloand File
            st.download_button(label='Download File',
                               data=doc_file,
                               file_name='My Documents.txx',
                               mime='text/plain')

        
        # Documents file type pdf
        elif doc_file.type == "application/pdf":
             raw_text = read_pdf(doc_file)
             st.write(raw_text)

             # Save File
             save_upload(doc_file)

             # Download File
             st.download_button(label='Download File',
                               data=doc_file,
                               file_name='My Documents.pdf',
                               mime='application/pdf')

             
        # Documents file type docu
        else:
            raw_text = docx2txt.process(doc_file)
            st.write(raw_text)
            # st.text(raw_text)

            # Save File
            save_upload(doc_file)

            # Download File
            st.download_button(label='Download File',
                               data=doc_file,
                               file_name='My Documents.docx',
                               mime='docx')