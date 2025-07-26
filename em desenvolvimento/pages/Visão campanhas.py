import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout="wide",
    page_icon="./assets/favicon.png",
    page_title=" Visão Campannha"
)

def aplicar_estilo_moderno(fig, titulo=None):
    fig.update_layout(
        font=dict(color="#333"),
        title=dict(
            text=titulo,
            x=0.5,
            xanchor='center',
            font=dict(size=18, color="#FFFFFF")
        ) if titulo else None,
        xaxis=dict(
            showgrid=False,
            linecolor="#06162E",
            title=dict(font=dict(size=14))
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            linecolor="#06162E",
            title=dict(font=dict(size=14))
        ),
        margin=dict(l=20, r=20, t=60 if titulo else 30, b=20),
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        ),
        bargap=0.4,
        bargroupgap=0.1
    )
    return fig

def esconderHeader():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

esconderHeader()

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

st.logo("./assets/icone.png")

st.markdown( 
    f"""
    <div style='
        font-size: 30px;
        text-align: center;
        font-weight: bold;
        margin-top: -50px;
        margin-bottom: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
    '>
        Análise de Campanhas de Marketing
    </div>

    <div style='
        font-size: 16px;
        text-align: center;
        font-weight: normal;
        margin-bottom: 30px;
        margin-top: -10px;
    '>
        Visão da Performance das Campanhas
    </div>
    """,
    unsafe_allow_html=True
)

src = "./dados/dados_tratados.csv"
df_dados = pd.read_csv(src, sep=";")

contagemFilhos = df_dados.groupby('Filhos em Casa').size().reset_index(name='Contagem de Clientes')
contagemFilhos.rename(columns={'Filhos em Casa': 'Número de Filhos em Casa'}, inplace=True)

contagemCompra = df_dados.groupby(['Filhos em Casa', 'Comprou']).size().reset_index(name='Contagem de Clientes')
contagemCompra.rename(columns={'Filhos em Casa': 'Número de Filhos em Casa'}, inplace=True)
contagemCompra['Comprou_Status'] = contagemCompra['Comprou'].map({0: 'Não Comprou', 1: 'Comprou'})

media_salarial = df_dados.groupby('Comprou')['Salario Anual'].mean().reset_index()
media_salarial['Comprou_Status'] = media_salarial['Comprou'].map({0: 'Não Comprou', 1: 'Comprou'})

contagemCompraTotal = df_dados['Comprou'].value_counts().reset_index()
contagemCompraTotal.columns = ['Comprou', 'Contagem']
contagemCompraTotal['Comprou_Status'] = contagemCompraTotal['Comprou'].map({0: 'Não Comprou', 1: 'Comprou'})

grafico_media_salarial = px.bar(
    media_salarial,
    x='Comprou_Status',
    y='Salario Anual',
    labels={'Comprou_Status': 'Status de Compra', 'Salario Anual': 'Média Salarial (R$)'}, 
    color='Comprou_Status',
    color_discrete_map={"Não Comprou": "#001737", "Comprou": "#4a90e2"} 
)

grafico_media_salarial.update_traces(
    marker_line_color='#001737',
    marker_line_width=1.5,
    opacity=0.85,
    width=0.55,
    marker=dict(
        line=dict(width=1.5, color="#0D3C6B"),
        cornerradius=8
    ),
    hovertemplate="<b>%{x}</b><br>Média Salarial: R$%{y:,.0f}<extra></extra>"
)
grafico_media_salarial.update_layout(height=250)


# --- Gráfico de Pizza ---
graficoPizza = px.pie(
    contagemCompraTotal,
    names='Comprou_Status',
    values='Contagem',
    labels={'Comprou_Status': 'Status de Compra', 'Contagem': 'Número de Clientes'},
    color_discrete_map={"Não Comprou": "#001737", "Comprou": "#4a90e2"}
)

graficoPizza.update_traces(
    marker=dict(line=dict(color='#FFFFFF', width=2)), 
    pull=[0, 0.05], 
    textinfo='percent+label',
    hoverinfo='label+percent+value', 
    textfont_color="#FFFFFF"
)
graficoPizza.update_layout(showlegend=True) 
graficoPizza.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    uniformtext_minsize=12, uniformtext_mode='hide'
)
graficoPizza.update_layout(height=250) 


col1, col2 = st.columns(2)

with col1:
    st.markdown( 
        f"""
        <div style='
            font-size: 17px;
            text-align: center;
            font-weight: bold;
            margin-bottom: -8px;
            display: flex;
            justify-content: center;
            align-items: center;
        '>
            Média Salário Anual x Resultado das Campanhas
        </div>
        """,
        unsafe_allow_html=True
    )
    st.plotly_chart(grafico_media_salarial, use_container_width=True)
with col2:
    st.markdown( 
        f"""
        <div style='
            font-size: 17px;
            text-align: center;
            font-weight: bold;
            margin-bottom: -8px;
            display: flex;
            justify-content: center;
            align-items: center;
        '>
            Resultado das Campanhas de Marketing  
        </div>
        """,
        unsafe_allow_html=True
    )
    st.plotly_chart(graficoPizza, use_container_width=True)
    
st.markdown( 
        f"""
        <div style='
            font-size: 17px;
            text-align: center;
            font-weight: bold;
            margin-bottom: -8px;
            display: flex;
            justify-content: center;
            align-items: center;
        '>
            Efetividade da Campanha x Número de Filhos
        </div>
        """,
        unsafe_allow_html=True
    )

graficoColunasClusterizado = px.bar(
    contagemCompra,
    x='Número de Filhos em Casa',
    y='Contagem de Clientes',
    color='Comprou_Status', 
    barmode='group', 
    labels={
        'Número de Filhos em Casa': 'Número de Filhos',
        'Contagem de Clientes': 'Número de Clientes',
        'Comprou_Status': 'Status de Compra'
    },
    category_orders={"Comprou_Status": ["Não Comprou", "Comprou"]},
    color_discrete_map={"Não Comprou": "#001737", "Comprou": "#4a90e2"}
)

graficoColunasClusterizado.update_traces(
    marker_line_color='#001737',
    marker_line_width=1.5,
    opacity=0.85,
    width=0.3,
    marker=dict(
        line=dict(width=1.5, color="#0D3C6B"),
        cornerradius=8
    ),
    hovertemplate="<b>Filhos: %{x}</b><br>Status: %{color}<br>Clientes: %{y}<extra></extra>"
)
graficoColunasClusterizado.update_layout(height=400)

st.plotly_chart(graficoColunasClusterizado, use_container_width=True)