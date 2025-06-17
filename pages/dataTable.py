import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Dashboard',
    layout='wide'
)

df_dados = pd.read_csv("./dados/dados_marketing.csv", sep=';')

# Tratando o ID 0
novoID = 11192
df_dados.loc[df_dados['ID'] == 0, 'ID'] = novoID

# Mostrando o df
st.dataframe(
    df_dados,
    use_container_width=True,
    hide_index=True,
    height=800
    )