import streamlit as st
import pandas as pd

st.set_page_config(page_title="stores", page_icon="🏢", layout= "wide")


df_lojas = pd.read_csv(r"C:\Users\aluno\Documents\project python\database\Lojas.csv", sep=";", encoding="latin1", index_col="ID Loja", parse_dates= True)



df_vendas = pd.read_excel(r"C:\Users\aluno\Documents\project python\database\Vendas.xlsx")


lojas = df_lojas['Loja'].unique()
loja = st.sidebar.selectbox("Loja", lojas)

st.markdown(f"# {loja}")

df_lojas
df_vendas