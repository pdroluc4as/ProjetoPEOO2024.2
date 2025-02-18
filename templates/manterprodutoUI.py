import streamlit as st
import pandas as pd
from views import View
import time

'''
class ManterItemUI:
    def main():
        st.header("Cadastro de Itens")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterItemUI.listar()
        with tab2: ManterItemUI.inserir()
        with tab3: ManterItemUI.atualizar()
        with tab4: ManterItemUI.excluir()

    def listar():
        itens = View.item_listar()
        if len(itens) == 0: 
            st.write("Nenhum item cadastrado")
        else:    
            #for obj in items: st.write(obj)
            dic = []
            for obj in itens: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        pedidos = View.pedido_listar()
        produtos = View.produto_listar()
        pedido = st.selectbox("Informe o pedido do item", pedidos, index = None)
        produto = st.selectbox("Informe o produto do item", produtos, index = None)
        preco = st.text_input("Informe o preço do item")
        unidade = st.text_input("Informe a unidade")
        presente = st.checkbox("Confirmado")
     
        if st.button("Inserir"):
            id_pedido = None
            id_produto = None
            if pedido != None: id_pedido = pedido.id
            if produto != None: id_produto = produto.id
            View.item_inserir(id_produto, id_pedido, preco, unidade, presente)
            st.success("Item inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        itens = View.item_listar()
        if len(itens) == 0: 
            st.write("Nenhum item cadastrado")
        else:
            pedidos = View.pedido_listar()
            produtos = View.produto_listar()
            op = st.selectbox("Atualização de cliente", itens)
            id_pedido = None if op.id_pedido in [0, None] else op.id_pedido
            id_produto = None if op.id_produto in [0, None] else op.id_produto
            pedido = st.selectbox("Informe o novo pedido", pedidos, next((i for i, c in enumerate(pedidos) if c.id == id_pedido), None))
            produto = st.selectbox("Informe o novo serviço", produtos, next((i for i, s in enumerate(produtos) if s.id == id_produto), None))
            preco = st.text_input("Informe o novo nome do cliente", op.preco)
            unidade = st.text_input("Informe o novo e-mail", op.unidade)
            presente = st.checkbox("Nova confirmação", op.presente)
        
            if st.button("Atualizar"):
                id_pedido = None
                id_produto = None
                if pedido != None: id_pedido = pedido.id
                if produto != None: id_produto = produto.id
                View.item_atualizar(op.id, id_pedido, id_produto, preco, unidade, presente)
                st.success("item atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        itens = View.item_listar()
        if len(itens) == 0: 
            st.write("Nenhum item cadastrado")
        else:
            op = st.selectbox("Exclusão de item", itens)
            if st.button("Excluir"):
                View.item_excluir(op.id)
                st.success("Item excluído com sucesso")
                time.sleep(2)
                st.rerun()
                '''