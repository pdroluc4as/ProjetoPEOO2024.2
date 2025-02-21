from views import View
import streamlit as st
import pandas as pd
from views import View
import time

class MeusDadosVendedorUI:
    def main():
        st.header("Meus Dados")
        MeusDadosVendedorUI.atualizar()

    def atualizar():
        op = View.vendedor_listar_id(st.session_state["vendedor_id"])
        nome = st.text_input("Informe o novo nome", op.nome)
        email = st.text_input("Informe o novo e-mail", op.email)
        senha = st.text_input("Informe a nova senha", op.senha, type="password")
        if st.button("Atualizar"):
            View.vendedor_atualizar(op.id, nome, email, senha)
            st.success("Dados atualizado com sucesso")
            time.sleep(2)
            st.rerun()