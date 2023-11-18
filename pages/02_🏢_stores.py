import streamlit as st
import pandas as pd

st.set_page_config(page_title="stores", page_icon="🏢", layout= "wide")


df_lojas = pd.read_csv(r"C:\Users\aluno\Documents\project python\database\Lojas.csv", sep=";", encoding="latin1", index_col="ID Loja", parse_dates= True)



df_vendas = pd.read_excel(r"C:\Users\aluno\Documents\project python\database\Vendas.xlsx")


df_vendas = pd.merge(df_vendas, df_lojas, on="ID Loja", how="left")
df_vendas = df_vendas.reset_index()

df_vendas = df_vendas.drop(['Código Venda', 'ID Loja'], axis=1)


lojas = df_lojas['Loja'].unique()
loja = st.sidebar.selectbox("Loja", lojas)

st.markdown(f"# {loja}")
st.divider()

df_vendas = df_vendas[df_vendas["Loja"] == loja]
#df_lojas 
df_vendas