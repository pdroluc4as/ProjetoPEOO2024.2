import streamlit as st
import pandas as pd
from views import View
import time

class ManterVendedorUI:
    def main():
        st.header("Cadastro de Vendedor")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterVendedorUI.listar()
        with tab2: ManterVendedorUI.inserir()
        with tab3: ManterVendedorUI.atualizar()
        with tab4: ManterVendedorUI.excluir()

    def listar():
        vendedores = View.vendedor_listar()
        if len(vendedores) == 0: 
            st.write("Nenhuma vendedor cadastrada")
        else:    
            #for obj in vendedores: st.write(obj)
            dic = []
            for obj in vendedores: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do vendedor")
        email = st.text_input("Informe o email do vendedor")
        senha = st.text_input("Informe a senha do vendedor", type="password")
        if st.button("Inserir"):
            View.vendedor_inserir(nome, email, senha)
            st.success("Vendedor inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        vendedores = View.vendedor_listar()
        if len(vendedores) == 0: 
            st.write("Nenhum vendedor cadastrado")
        else:
         
            op = st.selectbox("Atualização de vendedor", vendedores)
            nome = st.text_input("Informe o novo nome do vendedor", op.nome)
            email = st.text_input("Informe o novo email do vendedor", op.email)
            senha = st.text_input("Informe a nova senha do vendedor", op.senha, type="password")
            if st.button("Atualizar"):
                View.vendedor_atualizar(op.id, nome, email, senha)
                st.success("Vendedor atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        vendedores = View.vendedor_listar()
        if len(vendedores) == 0: 
            st.write("Nenhum vendedor cadastrado")
        else:
            op = st.selectbox("Exclusão de vendedor", vendedores)
            if st.button("Excluir"):
                View.vendedor_excluir(op.id)
                st.success("Vendedir excluído com sucesso")
                time.sleep(2)
                st.rerun()