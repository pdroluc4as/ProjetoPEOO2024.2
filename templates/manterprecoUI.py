import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterPrecoUI:
    def main():
        st.header("Cadastro de Preços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPrecoUI.listar()
        with tab2: ManterPrecoUI.inserir()
        with tab3: ManterPrecoUI.atualizar()
        with tab4: ManterPrecoUI.excluir()

    def listar():
        preços = View.preco_listar()
        if len(preços) == 0: 
            st.write("Nenhum preço cadastrado")
        else:    
            #for obj in items: st.write(obj)
            dic = []
            for obj in preços: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        produtos = View.produto_listar()
        produto = st.selectbox("Informe o produto do preço", produtos, index = None)
        data = st.text_input("Informe a data e horário do preço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        if st.button("Inserir"):
            id_produto = None
            if produto != None: id_produto = produto.id
            View.preco_inserir(id_produto, data)
            st.success("Preço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        precos = View.preco_listar()
        if len(precos) == 0: 
            st.write("Nenhum preço cadastrado")
        else:
            produtos = View.produto_listar()
            op = st.selectbox("Atualização do preço", precos)
            id_produto = None if op.id_produto in [0, None] else op.id_produto
            data = st.text_input("Informe a nova data e horário do preço", op.data.strftime("%d/%m/%Y %H:%M"))
            produto = st.selectbox("Informe o novo produto do preço", produtos, next((i for i, c in enumerate(produtos) if c.id == id_produto), None))
            if st.button("Atualizar"):
                id_produto = None
                if produto != None: id_produto = produto.id
                View.preco_atualizar(op.id, id_produto, data)
                st.success("Preço atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        precos = View.preco_listar()
        if len(precos) == 0: 
            st.write("Nenhum preço cadastrado")
        else:
            op = st.selectbox("Exclusão de preço", precos)
            if st.button("Excluir"):
                View.preco_excluir(op.id)
                st.success("Preço excluído com sucesso")
                time.sleep(2)
                st.rerun()