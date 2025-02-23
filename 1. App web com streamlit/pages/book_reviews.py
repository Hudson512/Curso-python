import streamlit as st
import pandas as pd

st.set_page_config(page_title="App - book reviews", page_icon=":books:", layout="wide")

df_comentarios = pd.read_csv("datasets/customer reviews.csv")
df_livros = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_livros["book title"].unique()
book = st.sidebar.selectbox("Escolha um livro", books)


df_livro_select = df_livros[df_livros["book title"] == book]
df_coment_select = df_comentarios[df_comentarios["book name"] == book]

#df_livro_select
book_title = df_livro_select["book title"].iloc[0]
book_gen = df_livro_select["genre"].iloc[0]
book_price = df_livro_select["book price"].iloc[0]
book_rating = df_livro_select["rating"].iloc[0]
book_year = df_livro_select["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_gen)
col1, col2, col3 = st.columns(3)
col1.metric("Preço", f"$ {book_price}")
col2.metric("Avaliação", book_rating)
col3.metric("Ano de publicação", book_year)

st.divider()
for row in df_coment_select.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])