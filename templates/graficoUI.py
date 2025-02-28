import streamlit as st
import pandas as pd
from views import View

class GraficoUI:
    @staticmethod
    def main():
        st.header("Gráfico de Variação de Preços")
        
        produtos = View.produto_listar()
        if not produtos:
            st.write("Nenhum produto disponível.")
            return
        
        # Obter nomes únicos dos produtos
        produto_nomes = list(set(p.nome for p in produtos))
        
        # Seleção do produto
        produto_nome = st.selectbox("Selecione um produto", options=produto_nomes)
        
        # Filtrar todos os produtos com o mesmo nome
        produtos_selecionados = [p for p in produtos if p.nome == produto_nome]
        
        if produtos_selecionados:
            GraficoUI.plot_price_variation(produtos_selecionados)
        else:
            st.write("Produto não encontrado.")
    
    @staticmethod
    def plot_price_variation(produtos):
        # Criar DataFrame
        data = [p.data for p in produtos]
        precos = [p.preco for p in produtos]
        df = pd.DataFrame({"Data": data, "Preço": precos})
        df["Data"] = pd.to_datetime(df["Data"])  # Converter para formato de data
        df = df.sort_values("Data")  # Ordenar por data
        
        # Criar gráfico com Streamlit
        st.line_chart(df.set_index("Data"))