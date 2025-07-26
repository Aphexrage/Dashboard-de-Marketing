import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout="wide",
    page_icon="./assets/favicon.png",
    page_title=" Visão PDV"
)

src = "./dados/dados_tratados.csv"
df_dados = pd.read_csv(src, sep=";")

pais_ingles = {
    'Brasil': 'Brazil',
    'Espanha': 'Spain',
    'Argentina': 'Argentina',
    'Chile': 'Chile',
    'México': 'Mexico',
    'Estados Unidos': 'United States',
    'Alemanha': 'Germany',
    'França': 'France',
    'Itália': 'Italy',
    'Portugal': 'Portugal',
}

df_dados['Pais'] = df_dados['Pais'].map(pais_ingles).fillna(df_dados['Pais'])

colunas_gasto = [
    'Gasto com Eletronicos',
    'Gasto com Brinquedos',
    'Gasto com Moveis',
    'Gasto com Utilidades',
    'Gasto com Alimentos',
    'Gasto com Vestuario'
]

df_dados['Gasto Total'] = df_dados[colunas_gasto].sum(axis=1)

df_dados['Data Cadastro'] = pd.to_datetime(df_dados['Data Cadastro'], dayfirst=True, errors='coerce')
df_dados['Ano Cadastro'] = df_dados['Data Cadastro'].dt.year

gasto_pais_ano = df_dados.groupby(['Pais', 'Ano Cadastro'])['Gasto Total'].sum().reset_index()

grafico_linha_paises = px.line(
    gasto_pais_ano,
    x='Ano Cadastro',
    y='Gasto Total',
    color='Pais',
    markers=True,
    title='Evolução dos Gastos por País ao Longo dos Anos',
    labels={
        'Ano Cadastro': 'Ano',
        'Gasto Total': 'Total Gasto (R$)',
        'Pais': 'País'
    }
)

gastos_por_categoria = df_dados.groupby('Pais')[colunas_gasto].sum().reset_index()

gastos_melted = gastos_por_categoria.melt(
    id_vars='Pais',
    value_vars=colunas_gasto,
    var_name='Categoria de Gasto',
    value_name='Valor Gasto'
)

grafico_clusterizado = px.bar(
    gastos_melted,
    x='Pais',
    y='Valor Gasto',
    color='Categoria de Gasto',
    barmode='group',
    title='Gastos por País e Categoria',
    labels={
        'Pais': 'País',
        'Valor Gasto': 'Total Gasto (R$)',
        'Categoria de Gasto': 'Categoria'
    },
    color_discrete_sequence=px.colors.qualitative.Set3
)

st.plotly_chart(grafico_clusterizado, use_container_width=True)
st.plotly_chart(grafico_linha_paises, use_container_width=True)
