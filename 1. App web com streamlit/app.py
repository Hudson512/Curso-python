import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="App de teste", page_icon=":books:", layout="wide")
df_comentarios = pd.read_csv("datasets/customer reviews.csv")
df_livros = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_livros["book price"].max()
price_min = df_livros["book price"].min()

userPrice = st.sidebar.slider("Preço do livro", price_min, price_max, price_max)

show_df_books = df_livros[df_livros["book price"] <= userPrice]
fig1 = px.bar(show_df_books["year of publication"].value_counts())
fig2 = px.histogram(show_df_books["book price"])

#Display the data
show_df_books

col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)