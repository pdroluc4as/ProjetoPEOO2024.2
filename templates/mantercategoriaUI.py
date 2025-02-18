import streamlit as st
import pandas as pd
from views import View
import time

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    def listar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:    
            #for obj in categorias: st.write(obj)
            dic = []
            for obj in categorias: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome da categoria")
        if st.button("Inserir"):
            View.categoria_inserir(nome)
            st.success("Categoria inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhum categoria cadastrado")
        else:
         
            op = st.selectbox("Atualização de categoria", categorias)
            nome = st.text_input("Informe o novo nome do categoria", op.nome)
            if st.button("Atualizar"):
                View.categoria_atualizar(op.id, nome)
                st.success("categoria atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrado")
        else:
            op = st.selectbox("Exclusão de categoria", categorias)
            if st.button("Excluir"):
                View.categoria_excluir(op.id)
                st.success("Categoria excluído com sucesso")
                time.sleep(2)
                st.rerun()