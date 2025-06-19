import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    layout="wide"
)

src = "./dados/dados_marketing.csv"

df_dados = pd.read_csv(src, sep=';')

paises = df_dados['Pais'].unique().tolist()

paises.insert(0, 'Todos os países')

selecaoPais = st.sidebar.selectbox(
    'Selecione um País:',
    paises                 
    )   

icone = "./assets/icone.png"

st.logo(icone)

st.sidebar.divider()

st.sidebar.download_button(
    label= "Baixar dados",
    data = src,
    file_name= "Dados Marketing",
    mime="text/csv",
    icon=":material/download:"
)

if selecaoPais == 'Todos os países':
    df_filtrado = df_dados.copy()
else:
    df_filtrado = df_dados[df_dados['Pais'] == selecaoPais].copy()

totalDeClientes = df_filtrado.shape[0]

mediaSalario = df_filtrado['Salario Anual'].mean()
mediaSalario = f"R$ {mediaSalario/1000:.0f} mil"

totalComprasLoja = df_filtrado['Numero de Compras na Loja'].sum()

totalComprasWeb = df_filtrado['Numero de Compras na Web'].sum()

totalComprasCatalogo = df_filtrado['Numero de Compras via Catalogo'].sum()

totalComprasDesconto = df_filtrado['Numero de Compras com Desconto'].sum()

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Total de Clientes", totalDeClientes)
with col2:
    st.metric('Media de Salario', mediaSalario)
with col3:
    st.metric('Total de Compras em Lojas', totalComprasLoja)
with col4:
    st.metric('Total de Compras no site', totalComprasWeb)
with col5:
    st.metric('Total de Compras em catalogo', totalComprasCatalogo)
with col6:
    st.metric('Total de Compras com desconto', totalComprasDesconto)
    
col1, col2 = st.columns(2)

df_grupo = df_filtrado.groupby('Escolaridade')['ID'].count().reset_index()

with col1:
    grafico1 = px.bar(
        df_grupo,
        x='Escolaridade',
        y = 'ID',
        title='Clientes por Escolaridade',
        labels={'Escolaridade': 'Nivel de Escolaridade', 'ID': 'Colaboradores'}
    )
    st.plotly_chart(grafico1)
    
df_grupo2 = df_filtrado.groupby('Estado Civil')['ID'].count().reset_index()
with col2:
    grafico2 = px.bar(
        df_grupo2,
        x='Estado Civil',
        y='ID',
        title='Clientes por Estado Civil',
        labels={'ID': 'Colaboradores'}
    )
    st.plotly_chart(grafico2)

