import streamlit as st
import pandas as pd

def objective(n, a, l ,g, w, max_n, max_a):
    n_obj = w[0] * n / max_n
    a_obj = (w[1] * a / max_a)
    l_obj =  w[2]*l
    g_obj = w[3]*g
    
    return (n_obj + a_obj + l_obj + g_obj)

st.title("Optimal Estate")

st.header('Input Data', divider=True)
col1, col2 = st.columns(2)
with col1:
    source_df = pd.read_csv('estate.csv', sep=';', index_col='ID')
    df = st.data_editor(source_df)
with col2:
    w = [0,0,0,0]
    w[0] = number = st.number_input("Neighbours Weight", min_value=-1.0, max_value=1.0, value=-1.0)
    w[1] = number = st.number_input("Area Weight", min_value=-1.0, max_value=1.0, value=1.0)
    w[2] = number = st.number_input("Long Edge Weight", min_value=-1.0, max_value=1.0, value=1.0)
    w[3] = number = st.number_input("South Garden Weight", min_value=-1.0, max_value=1.0, value=1.0)

max_neighbours = df['Neighbours'].max()
max_area = df['Area'].max()
y = df.apply(lambda row: objective(row['Neighbours'], row['Area'], row['LongEdge'], row['SouthGarden'], w, max_neighbours, max_area), axis=1)
y.name = 'Score'


st.header('Results', divider=True)
col1, col2 = st.columns(2)
with col1:
    st.write(y.sort_values(ascending=False))
with col2:
    w1 = format(w[0], '+.2')
    w2 = format(w[1], '+.2')
    w3 = format(w[2], '+.2')
    w4 = format(w[3], '+.2')
    y1 = r'''\frac{n}{''' + str(max_neighbours) + r'''}'''
    y2 = r'''\frac{a}{''' + str(max_area) + r'''}'''
    y3 = r'''\cdot l'''
    y4 = r'''\cdot g'''
    st.latex(w1 + y1 + w2 + y2 + w3 + y3 + w4 + y4)
