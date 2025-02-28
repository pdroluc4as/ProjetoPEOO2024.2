import streamlit as st
import pandas as pd
from views import View
import time

class ManterCarrinhoUI:
    @staticmethod
    def main():
        st.header("Produtos no Carrinho")

        if "carrinho" not in st.session_state:
            st.session_state.carrinho = View.carrinho

        produtos = View.produto_listar()
        produtos_dict = {produto.id: produto for produto in produtos}

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Adicionar Produto")
            produto_id = st.selectbox("Selecione um produto", options=[p.id for p in produtos], format_func=lambda id: produtos_dict[id].nome)
            
            if produto_id:
                estoque_disponivel = produtos_dict[produto_id].estoque  # Obtém o estoque do produto selecionado
                quantidade = st.number_input("Quantidade", min_value=1, max_value=estoque_disponivel, value=1, step=1)
            
                if st.button("Adicionar ao Carrinho"):
                    sucesso = View.adicionar_ao_carrinho(produto_id, quantidade)
                    if sucesso:
                        st.session_state.carrinho = View.carrinho
                        st.success("Produto adicionado ao carrinho!")
                    else:
                        st.error("Quantidade excede o estoque disponível!")
        
        with col2:
            st.subheader("Remover Produto")
            if st.session_state.carrinho:
                produto_remover = st.selectbox("Selecione um produto para remover", options=list(st.session_state.carrinho.keys()))
                if st.button("Remover do Carrinho"):
                    for prod in produtos:
                        if prod.nome == produto_remover:
                            View.remover_do_carrinho(prod.id)
                            st.session_state.carrinho = View.carrinho  # Atualiza o estado do carrinho
                            st.success("Produto removido do carrinho!")
                            break


        st.subheader("Carrinho Atual")
        if st.session_state.carrinho:
            df = pd.DataFrame.from_dict(st.session_state.carrinho, orient='index')
            df["Total"] = df["preco"] * df["quantidade"]
            st.dataframe(df)
        else:
            st.write("Carrinho vazio.")

        if st.button("Finalizar Compra"):
            total = View.total_carrinho()
            st.success(f"Compra finalizada! Total: R${total}")
            View.carrinho.clear()
            st.session_state.carrinho = {}  # Atualiza corretamente o estado de sessão
            time.sleep(2)
            st.rerun()

if __name__ == "__main__":
    ManterCarrinhoUI.main()
