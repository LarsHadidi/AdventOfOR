import streamlit as st
import pandas as pd

def objective(n, a, l ,g, w, max_n, max_a):
    return (- w[0] * n / max_n) + (w[1] * a / max_a) + w[2]*l + w[3]+g

st.title("Optimal Estate")
st.write('Editable source data')
df = pd.read_csv('estate.csv', sep=';', index_col='ID')
edited_df = st.data_editor(df)

max_neighbours = df['Neighbours'].max()
max_area = df['Area'].max()

st.latex(r'''-w_1\frac{n}{''' + str(max_neighbours) + r'''}+w_2\frac{a}{''' + str(max_area) + r'''} + w_3l + w_4g''')

w = [1,1,1,1]
w[0] = number = st.number_input("Neighbours Weight", min_value=0, max_value=1, value=1)
w[1] = number = st.number_input("Area Weight", min_value=0, max_value=1, value=1)
w[2] = number = st.number_input("Long Edge Weight", min_value=0, max_value=1, value=1)
w[3] = number = st.number_input("South Garden Weight", min_value=0, max_value=1, value=1)

y = df.apply(lambda row: objective(row['Neighbours'], row['Area'], row['LongEdge'], row['SouthGarden'], w, max_neighbours, max_area), axis=1)

st.write(f'Optimal value for ID {y.idxmax()}')
st.write('Ranking')
st.write(y.sort_values(ascending=False))