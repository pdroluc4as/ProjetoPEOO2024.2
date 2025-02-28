import streamlit as st
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manteritemUI import ManterItemUI
from templates.manterpedidoUI import ManterPedidoUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.manterusuarioUI import ManterUsuarioUI
from templates.meusdadosUI import MeusDadosUI
from templates.mantercarrinhoUI import ManterCarrinhoUI
from views import View

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Usuarios", "Cadastro de Categorias", "Cadastro de Itens", "Cadastro de Pedidos", "Cadastro de Produtos", "Meus Dados"])
        if op == "Cadastro de Usuarios": ManterUsuarioUI.main()
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Itens": ManterItemUI.main()
        if op == "Cadastro de Pedidos": ManterPedidoUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Produtos Disponíveis", "Meu Carrinho", "Meus Dados"])
        if op == "Produtos Disponíveis": IndexUI.produtos_disponiveis()
        if op == "Meu Carrinho": ManterCarrinhoUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def menu_vendedor():
        op = st.sidebar.selectbox("Menu", ["Meus Produtos", "Meus Dados"])
        if op == "Meus Produtos": ManterProdutoUI.main()
        if op == "Meus Dados": MeusDadosUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            st.session_state.pop("cliente_id", None)
            st.session_state.pop("cliente_nome", None)
            st.session_state.pop("tipo", None)
            st.rerun()

    def sidebar():
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()   
        else:
            admin = st.session_state["cliente_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            if admin:
                IndexUI.menu_admin()
            elif st.session_state["tipo"] == "cliente":
                IndexUI.menu_cliente()
            else:
                IndexUI.menu_vendedor()
            IndexUI.sair_do_sistema() 

    def main():
        View.usuario_admin()
        IndexUI.sidebar()

    @staticmethod
    def produtos_disponiveis():
        st.title("Produtos Disponíveis")

        # Obtém as categorias
        categorias = View.categoria_listar()
        categorias_nomes = ["Todas"] + [categoria.nome for categoria in categorias]
        
        # Campo de filtro por categoria
        categoria_selecionada = st.selectbox("Filtrar por categoria:", categorias_nomes)

        # Obtém os produtos
        produtos = View.produto_listar()

        # Filtra os produtos se uma categoria for selecionada
        if categoria_selecionada != "Todas":
            produtos = [p for p in produtos if any(c.nome == categoria_selecionada for c in categorias if c.id == p.id_categoria)]

        # Exibe os produtos filtrados
        if produtos:
            for produto in produtos:
                st.write(f"**{produto.nome}** - R${produto.preco:.2f} - Estoque: {produto.estoque}")
        else:
            st.write("Nenhum produto encontrado para esta categoria.")

IndexUI.main()