import streamlit as st
import pandas as pd
from views import View

class ListarProdutoUI:
    def main():
        st.header("Produtos Disponíveis")
        ListarProdutoUI.listar()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto disponível")
        else:
            dic = []
            for obj in produtos: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)