import streamlit as st
import plotly.express as px 
import pandas as pd

st.set_page_config(
    layout="wide"
)

src = "./dados/dados_tratados.csv"

df_dados = pd.read_csv(src, sep=';')

df_dados['Total Gasto'] = (
    df_dados['Gasto com Eletronicos']
    + df_dados['Gasto com Brinquedos']
    + df_dados['Gasto com Moveis']
    + df_dados['Gasto com Utilidades']
    + df_dados['Gasto com Alimentos']
    + df_dados['Gasto com Vestuario']

)

salarioAnual = df_dados['Salario Anual']

col1, col2, col3, col4 = st.columns(4)

fig = px.scatter(
    df_dados,       
    x='Salario Anual',
    y='Total Gasto',
    title='Salário Anual vs. Total de Gastos dos Clientes', 
    hover_name='ID'
)   
st.plotly_chart(fig)