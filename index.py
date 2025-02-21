from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manteritemUI import ManterItemUI
from templates.manterpedidoUI import ManterPedidoUI
from templates.manterprecoUI import ManterPrecoUI
from templates.manterprodutoUI import ManterPordutoUI
from templates.meusdadosUI import MeusDadosUI
from templates.meusdadosvendedorUI import MeusDadosVendedorUI
import streamlit as st
from views import View

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Usuários", "Cadastro de Categorias", "Cadastro de Itens", "Cadastro de Pedidos", "Cadastro de Preços", "Cadastro de Produtos", "Meus Dados"])
        if op == "Cadastro de Usuários": ManterCategoriaUI.main()
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Itens": ManterItemUI.main()
        if op == "Cadastro de Pedidos": ManterPedidoUI.main()
        if op == "Cadastro de Preços": ManterPrecoUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Horários Disponíveis", "Meus Dados"])
        if op == "Horários Disponíveis": pass
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_vendedor():
        op = st.sidebar.selectbox("Menu", ["Minha Agenda", "Meus Dados"])
        if op == "Minha Agenda": pass
        if op == "Meus Dados": MeusDadosVendedorUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["usuario_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            # menu do usuário
            if st.session_state["tipo"] == "usuario":
                if admin: IndexUI.menu_admin()
                else: IndexUI.menu_usuario() 
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 

    def main():
        # verifica a existe o usuário admin
        View.usuario_admin()
        # monta o sidebar
        IndexUI.sidebar()


IndexUI.main()