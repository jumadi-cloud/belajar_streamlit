# import module
import streamlit as st

# Title
st.title("Kelas Awan Pintar")

# Header
st.header("Belajar fungsi dasar streamlit")
 
# Subheader
st.subheader("Ayu gaes kita belajar Streamlit dari dasar")

# Text
st.text("Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque, sint atque veritatis suscipit minima, dolor laudantium molestias quo, est corrupti illum officiis dolorem explicabo quaerat aspernatur iusto magnam. Laborum, ullam?")

# Markdown
st.markdown("# Markdown1")
st.markdown("## Markdown1")
st.markdown("### Markdown1")
st.markdown("#### Markdown1")

# Markdown multibaris
st.markdown("""
# test1

## test2

### test3
""",True)

#Code block
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


#LaTeX
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')