import pandas as pd
import streamlit as st
import plotly.express as px
import base64

st.set_page_config(
    layout="wide",
    page_icon="./assets/favicon.png",
    page_title="Visão Cliente"
)

def imagemDeFundo(image_path):
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
imagemDeFundo("./assets/fundo.png")

def aplicar_estilo_moderno(fig, titulo=None):
    fig.update_layout(showlegend=False)
    fig.update_layout(
        font=dict(color="#333", family="Arial"),
        title=dict(
            text=titulo,
            x=0.5,
            xanchor='center',
            font=dict(size=18, color="white")
        ) if titulo else None,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            linecolor="#06162E",
            title=dict(font=dict(size=14, color="white")),
            tickfont=dict(color="white")
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            linecolor="#06162E",
            title=dict(font=dict(size=14, color="white")),
            tickfont=dict(color="white")
        ),
        margin=dict(l=50, r=50, t=80 if titulo else 50, b=50),
        hoverlabel=dict(
            bgcolor="white",
            font_size=9,
            font_family="Arial",
            font_color="#333"
        ),
        bargap=0.4,
        bargroupgap=0.1,
        autosize=True,
        height=450
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
        /* Reset de margens e padding */
        .stPlotlyChart {
            border-radius: 16px !important;
            overflow: hidden !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
            height: 100% !important;
        }
        
        /* Container principal */
        div[data-testid="stPlotlyChart"] {
            width: 100% !important;
            height: 470px !important;
        }
        
        /* Div do gráfico */
        div[data-testid="stPlotlyChart"] > div {
            width: 100% !important;
            height: 100% !important;
            min-height: 450px !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1) !important;
            background: rgba(0, 23, 55, 0.7) !important;
            padding: 15px !important;
        }
        
        /* Ajuste das colunas */
        [data-testid="column"] {
            padding: 0 10px !important;
            width: calc(50% - 20px) !important;
        }
        
        /* Espaçamento entre gráficos */
        .element-container:has(div[data-testid="stPlotlyChart"]) {
            padding: 10px 0 !important;
        }
        
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
    </style>
    """
    st.markdown(sidebar, unsafe_allow_html=True)
    
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
        color: white;
    '>
        Análise de Campanhas de Marketing
    </div>

    <div style='
        font-size: 16px;
        text-align: center;
        font-weight: normal;
        margin-bottom: 30px;
        margin-top: -10px;
        color: white;
    '>
        Visão Cliente
    </div>
    """,
    unsafe_allow_html=True
)

def card_metric(titulo, valor):
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #001737 0%, #003366 100%);
            margin: 10px 0;
            padding: 25px; 
            text-align: center; 
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            border-left: 4px solid #4a90e2;
            color: white;
            height: 120px;
            margin-bottom: 50px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            border-radius: 8px;
        ">
            <p style="font-size: 14px; color: #c9d6ea; margin: 0; margin-bottom: 8px;">{titulo}</p>
            <p style="font-size: 28px; margin: 0; font-weight: 700; color: white;">{valor}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

modificarSideBar()

src = "./dados/dados_tratados.csv"

df_dados = pd.read_csv(src, sep=';')

# Filtros
paises = df_dados['Pais'].unique().tolist()

paises.insert(0, 'Todos os países')

selecaoPais = st.sidebar.selectbox(
    'Selecione um País:',
    paises                 
) 

st.sidebar.divider()

st.sidebar.download_button(
    label="Baixar dados",
    data=src,
    file_name="Dados Marketing.csv",
    mime="text/csv",
    icon=":material/download:"
)

if selecaoPais == 'Todos os países':
    df_filtrado = df_dados.copy()
else:
    df_filtrado = df_dados[df_dados['Pais'] == selecaoPais].copy()

# Métricas
totalDeClientes = df_filtrado.shape[0]

mediaSalario = df_filtrado['Salario Anual'].mean()

mediaSalario = f"R$ {mediaSalario/1000:.0f} mil"

totalComprasLoja = df_filtrado['Numero de Compras na Loja'].sum()

totalComprasWeb = df_filtrado['Numero de Compras na Web'].sum()

totalComprasCatalogo = df_filtrado['Numero de Compras via Catalogo'].sum()

totalComprasDesconto = df_filtrado['Numero de Compras com Desconto'].sum()

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    card_metric("Total de Clientes", totalDeClientes)
with col2:
    card_metric("Média de Salário", mediaSalario)
with col3:
    card_metric("Compras em Lojas", totalComprasLoja)
with col4:
    card_metric("Compras no site", totalComprasWeb)
with col5:
    card_metric("Compras em Catálogo", totalComprasCatalogo)
with col6:
    card_metric("Compras com Desconto", totalComprasDesconto)

col1, col2 = st.columns(2)

with col1:
    df_grupo = df_filtrado.groupby('Escolaridade')['ID'].count().reset_index()
    df_grupo = df_grupo.sort_values(by='ID', ascending=False)
    
    grafico1 = px.bar(
        df_grupo,
        x='Escolaridade',
        y='ID',
        labels={'Escolaridade': 'Nível de Escolaridade', 'ID': 'Nº de Colaboradores'},
        color='Escolaridade',
        color_discrete_sequence=px.colors.sequential.Blues_r,
    )
    
    grafico1 = aplicar_estilo_moderno(grafico1, "Clientes por Nível de Escolaridade")
    
    grafico1.update_traces(
        marker_line_color='#001737',
        marker_line_width=1.5,
        opacity=0.9,
        width=0.7,
        marker=dict(
            line=dict(width=1.5, color="#0D3C6B"),
            cornerradius=6
        ),
        hovertemplate="<b>%{x}</b><br>Clientes: %{y}<extra></extra>"
    )
    
    st.plotly_chart(grafico1, use_container_width=True)

with col2:
    df_grupo2 = df_filtrado.groupby('Estado Civil')['ID'].count().reset_index()
    df_grupo2 = df_grupo2.sort_values(by='ID', ascending=False)
    
    grafico2 = px.bar(
        df_grupo2,
        x='Estado Civil',
        y='ID',
        labels={'ID': 'Nº de Clientes'},
        color='Estado Civil',
        color_discrete_sequence=px.colors.sequential.Teal_r,
    )
    
    grafico2 = aplicar_estilo_moderno(grafico2, "Clientes por Estado Civil")
    
    grafico2.update_traces(
        marker_line_color='#006d75',
        marker_line_width=1.5,
        opacity=0.9,
        width=0.7,
        marker=dict(
            line=dict(width=1.5, color="#0D3C6B"),
            cornerradius=6
        ),
        hovertemplate="<b>%{x}</b><br>Clientes: %{y}<extra></extra>"
    )
    
    st.plotly_chart(grafico2, use_container_width=True)
