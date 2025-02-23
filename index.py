from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manteritemUI import ManterItemUI
from templates.manterpedidoUI import ManterPedidoUI
from templates.manterprecoUI import ManterPrecoUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.manterclienteUI import ManterClienteUI
from templates.mantervendedorUI import ManterVendedorUI
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
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Vendedores", "Cadastro de Categorias", "Cadastro de Itens", "Cadastro de Pedidos", "Cadastro de Preços", "Cadastro de Produtos", "Meus Dados"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Vendedores": ManterVendedorUI.main()
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Itens": ManterItemUI.main()
        if op == "Cadastro de Pedidos": ManterPedidoUI.main()
        if op == "Cadastro de Preços": ManterPrecoUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Produtos Disponíveis", "Meus Dados"])
        if op == "Produtos Disponíveis": pass
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_vendedor():
        op = st.sidebar.selectbox("Menu", ["Meus Produtos", "Meus Dados"])
        if op == "Meus Produtos": pass
        if op == "Meus Dados": MeusDadosVendedorUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if st.session_state["tipo"] == "cliente":
                if admin: IndexUI.menu_admin()
                else: IndexUI.menu_cliente() 
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 

    def main():
        # verifica a existe o usuário admin
        View.usuario_admin()
        # monta o sidebar
        IndexUI.sidebar()


IndexUI.main()