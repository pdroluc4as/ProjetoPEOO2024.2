from templates.loginUI import LoginUI
from templates.AbrirContaUI import AbrirContaUI
import streamlit as st
from view import View

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()