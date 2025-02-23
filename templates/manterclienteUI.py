import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Usuários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        cliente = View.cliente_listar()
        if len(cliente) == 0: 
            st.write("Nenhuma usuário cadastrada")
        else:    
            #for obj in usuarios: st.write(obj)
            dic = []
            for obj in cliente: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do usuário")
        email = st.text_input("Informe o email do usuário")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, senha)
            st.success("usuário inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        cliente = View.cliente_listar()
        if len(cliente) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:
         
            op = st.selectbox("Atualização de usuario", cliente)
            nome = st.text_input("Informe o novo nome do usuário", op.nome)
            email = st.text_input("Informe o novo email do usuário", op.email)
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            if st.button("Atualizar"):
                View.cliente_atualizar(op.id, nome, email, senha)
                st.success("Usuário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        cliente = View.cliente_listar()
        if len(cliente) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Exclusão de usuário", cliente)
            if st.button("Excluir"):
                View.cliente_excluir(op)
                st.success("Usuário excluído com sucesso")
                time.sleep(2)
                st.rerun()