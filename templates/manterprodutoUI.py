import streamlit as st
import pandas as pd
from views import View
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produto")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:    
            #for obj in produtos: st.write(obj)
            dic = []
            for obj in produtos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        categoria = View.categoria_listar()
        vendedor = View.vendedor_listar()
        
        vendedor = st.selectbox("Informe o Vendedor a qual o produto pertence", vendedor, index = None)
        categoria = st.selectbox("Informe a categoria do produto", categoria, index = None)
        estado_de_uso = st.text_input("Informe o estado de uso do produto")
        nome = st.text_input("Informe o nome do produto")
        preco = st.text_input("Informe o preço do produto")
        estoque = st.text_input("Informe a quantidade em estoque")
     
        if st.button("Inserir"):
            id_categoria = None
            if categoria != None: id_categoria = categoria.id
            View.produto_inserir(id_categoria, vendedor, estado_de_uso, nome, preco, estoque)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            categorias = View.categoria_listar()
            vendedores = View.vendedor_listar() # Adicionado para buscar vendedores
            op = st.selectbox("Atualização do produto", produtos)
            id_categoria = None if op.id_categoria in [0, None] else op.id_categoria
            categoria = st.selectbox("Informe a nova categoria", categorias, next((i for i, c in enumerate(categorias) if c.id == id_categoria), None))
            
            # Correção: Buscar o vendedor correto
            vendedor_atual = View.vendedor_listar_id(op.id_vendedor)
            vendedor = st.selectbox("Informe o novo vendedor", vendedores, next((i for i, v in enumerate(vendedores) if v.id == vendedor_atual.id), None))
            
            estado_de_uso = st.text_input("Informe o novo estado de uso do produto", op.estado_de_uso)
            nome = st.text_input("Informe o novo nome do produto", op.nome)
            preco = st.text_input("Informe o novo do produto", op.preco)
            estoque = st.text_input("Informe a nova quantidade em estoque", op.estoque)
        
            if st.button("Atualizar"):
                id_categoria = None
                if categoria != None: id_categoria = categoria.id
                View.produto_atualizar(op.id, id_categoria, vendedor, estado_de_uso, nome, preco, estoque) # Vendedor correto passado
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                View.produto_excluir(op)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()