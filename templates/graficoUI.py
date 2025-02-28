import streamlit as st
from views import View
from datetime import datetime
import pandas as pd
import plotly.express as px
import time

class GraficoUI:
    def main():
        st.header("Gráfico de Preços")
        GraficoUI.exibir_grafico()
       
    def exibir_grafico():
        produto = View.produto_listar()
        op = st.selectbox("Informe o produto", produto, index = None)
        data = op.data
        preco = op.preco
        data = pd.Dataframe("X": [op.data], "Y": [op.preco])
        st.line_chart(data, x="X" y="Y", color='FFFFFF')