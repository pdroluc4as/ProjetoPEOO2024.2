import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.usuario_autenticar(email, senha)
            v = View.vendedor_autenticar(email, senha)
            if c == None and v == None: st.write("E-mail ou senha inválidos") 
            if c != None:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.session_state["tipo"] = "cliente"
                st.rerun()

            if v != None:
                st.session_state["cliente_id"] = v["id"]
                st.session_state["cliente_nome"] = v["nome"]
                st.session_state["tipo"] = "vendedor"
                st.rerun()