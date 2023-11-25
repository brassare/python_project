import streamlit as st
import pandas as pd
from utils import leitura_de_dados
from datetime import datetime
import plotly.express as px


st.set_page_config(page_title="Produtos", page_icon="🛒", layout="wide")

#Leitura dos dados de utils
leitura_de_dados()


#Carregar dataframes da sessão 
df_vendas = st.session_state['dados']['df_vendas']
df_lojas = st.session_state['dados']['df_lojas']

# Lionha de codigo para realizar a junção do ID da loja 
df_data = pd.merge(df_vendas, df_lojas, on="ID Loja", how="left")
df_data = df_data.reset_index()

#Selecionar as colunas relevantes e formar a coluna de data 
df_data = df_data[['Data', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Final', 'Loja']]
df_data['Data'] = df_data['Data'].dt.strftime('%d%m%Y')

st.markdown("# Detalhamento dos Produtos")

#criação para selecionar a opção do selectbox da aba produtos 
produtos = df_data['Produto'].unique()
produto = st.sidebar.selectbox("Produtos", produtos)


st.divider()


#converter e formatar dados temporarios para criar um grafico em linhas
df_data['Data'] = pd.to_datetime(df_data['Data'],format='%d%m%Y')
df_data['Mês/Ano'] = df_data['Data'].dt.to_period('M')
df_data['Mês/Ano'] = df_data['Mês/Ano'].dt.strftime('%Y-%m')


#ticket medio 
df_data = df_data.drop(columns= ['Data','Valor Unitário'], axis=1)
df_data_agrupado = df_data.groupby(['Mês/Ano', 'Loja','Produto'])[['Quantidade', 'Valor Final']].sum().reset_index()
df_data_agrupado.set_index('Mês/Ano')

df_data_agrupado['Ticket_Medio'] = df_data_agrupado["Valor Final"] / df_data_agrupado["Quantidade"]


#Encontrar o produto com o maior ticket medio 
produto_maior_ticket_medio = df_data_agrupado.loc[df_data_agrupado['Ticket_Medio'].idxmax()]['Produto']
maior_tkt = df_data_agrupado.loc[df_data_agrupado['Ticket_Medio'].idxmax()]['Ticket_Medio']

st.markdown(f"#### O Produto com maior tkt é o/a: {produto_maior_ticket_medio} no valor de R$: {maior_tkt}")

st.divider()

df_data_agrupado = df_data_agrupado[df_data_agrupado['Produto'] == produto]

df_data_agrupado
