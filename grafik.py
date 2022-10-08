# import module
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import altair as alt
import plotly.figure_factory as ff
from bokeh.plotting import figure
import pydeck as pdk
import graphviz as graphviz
import plotly_express as px



# Title
st.title("Kelas Awan Pintar")
st.markdown("""
### 

Jika temen temen belum Install library Pandas dan Numpy di Streamlit

Cara insatll Pandas: pip install pandas [sumber](https://pypi.org/project/pandas/)

Cara insatll Numpy: pip install numpy [sumber](https://pypi.org/project/numpy/)

Cara Insatll Matplotlib: pip install matplotlib [sumber](https://pypi.org/project/matplotlib/)

Cara Insatll plotly-express: pip install plotly-express [sumber](https://pypi.org/project/plotly-express/)

====================================================================================
""",True)

# Header
st.header("Ayu Belajar Bagaimana Menapilkan Grafik di streamlit [sumber](https://docs.streamlit.io/library/api-reference/charts)")

# Buat data (Kumpulan dari data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
plotlychart = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

df = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

# Data studi kasus

dataset = pd.read_csv("https://raw.githubusercontent.com/jumadi-cloud/Fundamental-Python/main/Dataset/Iris.csv")

# ============***============
# Cara menapilkan grafik 
st.text("1. ini contoh grafik line charts")

st.line_chart(chart_data)

st.text("2. ini contoh grafik area charts")

st.area_chart(chart_data)

st.text("3. ini contoh grafik bar charts")

st.bar_chart(chart_data)

st.text("4. ini contoh grafik pyplot")

st.pyplot(fig)

st.text("5. ini contoh grafik altair_chart")

st.altair_chart(c, use_container_width=True)

st.text("6. ini contoh grafik vega_lite_chart")

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

st.text("7. ini contoh grafik plotly_chart")

st.plotly_chart(plotlychart, use_container_width=True)

st.text("8. ini contoh grafik bokeh_chart")

st.bokeh_chart(p, use_container_width=True)

st.text("9. ini contoh grafik pydeck_chart")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

st.text("10. ini contoh grafik graphviz_chart")

st.graphviz_chart(graph)

st.text("11. ini contoh grafik map")

st.map(df)

st.markdown ("""### Studi Kasus 
Kita akan menapilkan grafik dari data bunga iris [sumber]("https://github.com/jumadi-cloud/Fundamental-Python/blob/main/Dataset/Iris.csv")

Dan kita akan show data menggunakan Input widgets
""", True)

iris_scatterplot = px.scatter(data_frame=dataset,x='SepalLengthCm',
y='SepalWidthCm',color='Species',title="Scatterplot of Sepal Length vs Sepal Width")

show_data = st.checkbox("show dataframe")
if show_data:
    st.write(iris_scatterplot)