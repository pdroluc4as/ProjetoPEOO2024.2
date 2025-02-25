import streamlit as st
import pandas as pd
from views import View
import time

class ManterUsuarioUI:
    def main():
        st.header("Cadastro de Usuários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterUsuarioUI.listar()
        with tab2: ManterUsuarioUI.inserir()
        with tab3: ManterUsuarioUI.atualizar()
        with tab4: ManterUsuarioUI.excluir()

    def listar():
        usuario = View.usuario_listar()
        if len(usuario) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:    
            #for obj in usuarios: st.write(obj)
            dic = []
            for obj in usuario: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do usuário")
        email = st.text_input("Informe o email do usuário")
        senha = st.text_input("Informe a senha", type="password")
        vendedor = st.checkbox("Confirmado")
        if st.button("Inserir"):
            View.usuario_inserir(nome, email, senha, vendedor)
            st.success("Usuário inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        usuario = View.usuario_listar()
        if len(usuario) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Atualização de usuario", usuario)
            nome = st.text_input("Informe o novo nome do usuário", op.nome)
            email = st.text_input("Informe o novo email do usuário", op.email)
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            vendedor = st.checkbox("Nova confirmação", op.vendedor)
            if st.button("Atualizar"):
                View.usuario_atualizar(op.id, nome, email, senha, vendedor)
                st.success("Usuário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        usuario = View.usuario_listar()
        if len(usuario) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Exclusão de usuário", usuario)
            if st.button("Excluir"):
                View.usuario_excluir(op)
                st.success("Usuário excluído com sucesso")
                time.sleep(2)
                st.rerun()