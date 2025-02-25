import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        vendedor = st.checkbox("Vendedor")
        if st.button("Inserir"):
            View.usuario_inserir(nome, email, senha, vendedor)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()
        