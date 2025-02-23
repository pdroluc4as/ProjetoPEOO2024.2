from views import View
import streamlit as st
import pandas as pd
import time

class MeusDadosUI:
    def main():
        st.header("Meus Dados")
        MeusDadosUI.atualizar()

    def atualizar():
        op = View.cliente_listar_id(st.session_state["cliente_id"])
        nome = st.text_input("Informe o novo nome", op.nome)
        email = st.text_input("Informe o novo e-mail", op.email)
        senha = st.text_input("Informe a nova senha", op.senha, type="password")
        if st.button("Atualizar"):
            View.cliente_atualizar(op.id, nome, email, senha)
            st.success("Dados atualizado com sucesso")
            time.sleep(2)
            st.rerun()