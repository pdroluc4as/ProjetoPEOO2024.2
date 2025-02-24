import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterPedidoUI:
    def main():
        st.header("Cadastro de Pedidos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPedidoUI.listar()
        with tab2: ManterPedidoUI.inserir()
        with tab3: ManterPedidoUI.atualizar()
        with tab4: ManterPedidoUI.excluir()

    def listar():
        pedidos = View.pedido_listar()
        if len(pedidos) == 0: 
            st.write("Nenhum pedido cadastrado")
        else:    
            #for obj in items: st.write(obj)
            dic = []
            for obj in pedidos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        cliente = View.cliente_listar()
        cliente = st.selectbox("Informe o cliente do pedido", cliente, index = None)
        previsao = st.text_input("Informe a data e horário da previsão de entrega", datetime.now().strftime("%d/%m/%Y %H:%M"))
        entrega = st.text_input("Informe a data e horário da entrega", datetime.now().strftime("%d/%m/%Y %H:%M"))
        nota_fiscal = st.text_input("Informe a nota fiscal do pedido")
        status = st.text_input("Informe o status do pedido")
        if st.button("Inserir"):
            id_cliente = None
            if cliente != None: id_cliente = cliente.id
            View.pedido_inserir(id_cliente, previsao, entrega, nota_fiscal, status)
            st.success("Pedido inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        pedidos = View.pedido_listar()
        if len(pedidos) == 0: 
            st.write("Nenhum pedido cadastrado")
        else:
            clientes = View.cliente_listar()
            op = st.selectbox("Atualização do pedido", pedidos)
            id_cliente = None if op.id_cliente in [0, None] else op.id_cliente
            cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.id == id_cliente), None))
            previsao = st.text_input("Informe a nova data e horário da previsão", op.previsao.strftime("%d/%m/%Y %H:%M"))
            entrega = st.text_input("Informe a nova data e horário de quando foi entregue", op.entrega.strftime("%d/%m/%Y %H:%M"))
            nota_fiscal = st.text_input("Informe a nova nota fiscal", op.nota_fiscal)
            status = st.text_input("Informe o novo status do pedido", op.status)        
            if st.button("Atualizar"):
                id_cliente = None
                if cliente != None: id_cliente = cliente.id
                View.pedido_atualizar(op.id, id_cliente, previsao, entrega, nota_fiscal, status)
                st.success("Pedido atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        pedidos = View.pedido_listar()
        if len(pedidos) == 0: 
            st.write("Nenhum pedido cadastrado")
        else:
            op = st.selectbox("Exclusão de pedido", pedidos)
            if st.button("Excluir"):
                View.pedido_excluir(op)
                st.success("Pedido excluído com sucesso")
                time.sleep(2)
                st.rerun()