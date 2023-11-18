import streamlit as st
import pandas as pd
from utils import leitura_de_dados

st.set_page_config(page_title="stores", page_icon="🏢", layout= "wide")

# Leitura dos dados de utils
leitura_de_dados()

#Carregar dataframes da sessão 
df_vendas = st.session_state['dados']['df_vendas']
df_lojas = st.session_state['dados']['df_lojas']

# Lionha de codigo para realizar a junção do ID da loja 
df_vendas = pd.merge(df_vendas, df_lojas, on="ID Loja", how="left")
df_vendas = df_vendas.reset_index()

# Linha de codigo para excluir a coluna 
df_vendas = df_vendas.drop(['Código Venda', 'ID Loja'], axis=1)


lojas = df_lojas['Loja'].unique()
loja = st.sidebar.selectbox("Loja", lojas)

st.markdown(f"# {loja}")
st.divider()

# Linha de codigo para Filtro
df_vendas = df_vendas[df_vendas["Loja"] == loja]
 
df_vendas