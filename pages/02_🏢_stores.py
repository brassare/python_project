import streamlit as st
import pandas as pd
from utils import leitura_de_dados
from datetime import datetime
import plotly.express as px

st.set_page_config(page_title="stores", page_icon="🏢", layout= "wide")

# Leitura dos dados de utils
leitura_de_dados()

#Carregar dataframes da sessão 
df_vendas = st.session_state['dados']['df_vendas']
df_lojas = st.session_state['dados']['df_lojas']

# Lionha de codigo para realizar a junção do ID da loja 
df_data = pd.merge(df_vendas, df_lojas, on="ID Loja", how="left")
df_data = df_data.reset_index()

# Linha de codigo para excluir a coluna 
df_data = df_data.drop(['Código Venda', 'ID Loja'], axis=1)


lojas = df_lojas['Loja'].unique()
loja = st.sidebar.selectbox("Loja", lojas)

st.markdown(f"# {loja}")
st.divider()

# Linha de codigo para Filtro
df_data_filtered = df_data[df_data["Loja"] == loja]

#calculo de faturamento total e medio para todas as lojas selecionadas
faturamento_total = df_vendas['Valor Final'].sum()
quantidade_total = df_vendas['Quantidade'].sum()
tkt_medio_total = faturamento_total / quantidade_total

faturament_loja = df_data_filtered['Valor Final'].sum()
quantidade_loja = df_data_filtered['Quantidade'].sum()
tkt_medio_loja = faturamento_total / quantidade_total
 
col1, col2 = st.columns(2) 
col1.markdown(f"#### Faturamento Grupo R$: {faturamento_total/1000:.2f} milhões")
col2.markdown(f"#### Ticket Médio R$: {tkt_medio_total:.2f}")
 
col3,col4 = st.columns(2)
col3.markdown(f"#### Faturamento Loja R$: {faturament_loja/1000:.2f} milhões")
col4.markdown(f"#### Ticket Médio R$: {tkt_medio_loja:.2f}")

st.divider()

#Converter e formatar dados temporais 
df_data_filtered['Data'] = pd.to_datetime(df_data_filtered['Data'],format='%d%m%Y')
df_data_filtered['Mês/Ano'] = df_data_filtered['Data'].dt.to_period('M')
df_data_filtered['Mês/Ano'] = df_data_filtered['Mês/Ano'].dt.strftime('%Y-%m')

#Agrupo dados por mês/ano e calcula faturamento mensal
df_faturamento_mensal = df_data_filtered.groupby('Mês/Ano')['Valor Final'].sum().reset_index()

#Criar o grafico de linha utilizando o plotly.express
fig = px.line(df_faturamento_mensal, x= 'Mês/Ano', y='Valor Final', title=f'Faturamento mensal da loja {loja}')
fig.update_xaxes(title_text='Mês/Ano')
fig.update_yaxes(title_text='Faturamento')

#Exibir o grafico 
st.plotly_chart(fig)

st.divider()
 
st.dataframe(df_data_filtered)

