import streamlit as st
import pandas as pd

st.set_page_config(page_title="stores", page_icon="🏢", layout= "wide")


df_lojas = pd.read_csv(r"C:\Users\aluno\Documents\project python\database\Lojas.csv", sep=";", encoding="latin1", index_col="ID Loja", parse_dates= True)



df_vendas = pd.read_excel(r"C:\Users\aluno\Documents\project python\database\Vendas.xlsx")

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