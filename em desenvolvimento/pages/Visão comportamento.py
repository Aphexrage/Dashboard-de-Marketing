import streamlit as st
import plotly.express as px 
import pandas as pd

st.set_page_config(
    layout="wide",
    page_icon="./assets/favicon.png",
    page_title=" Visão Comportamento"
)

def modificarSideBar():
    sidebar = """
        <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #001737 0%, #003366 100%) !important;
            color: white !important;
        }
        
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: white !important;
        }
        
        [data-testid="stSidebar"] .stSelectbox div {
            border-color: rgba(255,255,255,0.3) !important;
            color: white !important;
        }
        
        [data-testid="stSidebar"] .stDownloadButton button {
            background: rgba(255,255,255,0.1) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
        }
        
        [data-testid="stSidebar"] .stDownloadButton button:hover {
            background: rgba(255,255,255,0.2) !important;
        }
        
        [data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.2) !important;
            margin: 1.5rem 0 !important;
        }
        
        .plotly-graph-div {
            border-radius: 16px !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1) !important;
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%) !important;
            padding: 16px !important;
            border: 1px solid rgba(0,0,0,0.05) !important;
        }
        
        .metric-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.15) !important;
        }
        </style>
    """
    st.markdown(sidebar, unsafe_allow_html=True)
    
modificarSideBar()

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

col1, col2= st.columns(2)

graficoDispersao = px.scatter(
    df_dados,       
    x='Salario Anual',
    y='Total Gasto',
    title='Salário Anual vs. Total de Gastos dos Clientes', 
    hover_name='ID'
) 

arvore = px.treemap(
    df_dados,
    path= ['Estado Civil', 'Escolaridade'],
    values='Total Gasto',
    title='Olha a porra do milho'
)

with col1:
    st.plotly_chart(graficoDispersao)
with col2:
    st.plotly_chart(arvore)

graficoColunas = px.bar(
    df_dados,
    x= df_dados['Filhos em Casa'],
    y= df_dados['Total Gasto'],
    title="EU QUERO GOZA"
)

graficoColunas2 = px.bar(
    df_dados,
    x= df_dados['Adolescentes em Casa'],
    y= df_dados['Total Gasto'],
    title="EU QUERO GOZA"
)

col1, col2= st.columns(2)

with col1:
    st.plotly_chart(graficoColunas)
with col2:
    st.plotly_chart(graficoColunas2)