import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Dashboard',
    layout='wide'
)



df_dados = pd.read_csv("./dados/dados_marketing.csv", sep=';')

paises = df_dados['Pais'].unique().tolist()

paises.insert(0, 'Todos os países')

selecaoPais = st.sidebar.selectbox(
    'Selecione um País:',
    paises                 
    )   

icone = "./assets/icone.png"

if selecaoPais == 'Todos os países':
    df_filtrado = df_dados.copy()
else:
    df_filtrado = df_dados[df_dados['Pais'] == selecaoPais].copy()

totalDeClientes = df_dados.shape[0]

df_dados = df_filtrado

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

