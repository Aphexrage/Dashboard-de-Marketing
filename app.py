import pandas as pd
import streamlit as st

st.set_page_config(
    layout="wide"
)

src = "./dados/dados_marketing.csv"

df_dados = pd.read_csv(src, sep=';')

totalDeClientes = df_dados.shape[0]

mediaSalario = df_dados['Salario Anual']
mediaSalario = mediaSalario.mean()

totalComprasLoja = df_dados['Numero de Compras na Loja']
totalComprasLoja = totalComprasLoja.sum()

totalComprasWeb = df_dados['Numero de Compras na Web']
totalComprasWeb = totalComprasWeb.sum()

totalComprasCatalogo = df_dados['Numero de Compras via Catalogo']
totalComprasCatalogo = totalComprasCatalogo.sum()

totalComprasDesconto = df_dados['Numero de Compras com Desconto']
totalComprasDesconto = totalComprasDesconto.sum()

icone = "./assets/icone.png"

st.sidebar.image(icone, width=200)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.write(totalDeClientes)
with col2:
    st.write(mediaSalario)
with col3:
    st.write(totalComprasLoja)
with col4:
    st.write(totalComprasWeb)
with col5:
    st.write(totalComprasCatalogo)
with col6:
    st.write(totalComprasDesconto)