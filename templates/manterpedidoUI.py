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
        pedidos = View.item_listar()
        if len(pedidos) == 0: 
            st.write("Nenhum pedido cadastrado")
        else:    
            #for obj in items: st.write(obj)
            dic = []
            for obj in pedidos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        usuarios = View.usuario_listar()
        usuario = st.selectbox("Informe o usuario do item", usuarios, index = None)
        previsao = st.text_input("Informe a data e horário da previsão de entrega", datetime.now().strftime("%d/%m/%Y %H:%M"))
        entrega = st.text_input("Informe a data e horário da entrega", datetime.now().strftime("%d/%m/%Y %H:%M"))
        nota_fiscal = st.text_input("Informe a nota fiscal do pedido")
        status = st.text_input("Informe o status do pedido")
        if st.button("Inserir"):
            id_usuario = None
            if usuario != None: id_usuario = usuario.id
            View.pedido_inserir(id_usuario, previsao, entrega, nota_fiscal, status)
            st.success("Pedido inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        pedidos = View.pedido_listar()
        if len(pedidos) == 0: 
            st.write("Nenhum item cadastrado")
        else:
            usuarios = View.usuario_listar()
            op = st.selectbox("Atualização de cliente", pedidos)
            id_usuario = None if op.id_usuario in [0, None] else op.id_usuario
            usuario = st.selectbox("Informe o novo usuario", usuarios, next((i for i, c in enumerate(usuarios) if c.id == id_usuario), None))
            previsao = st.text_input("Informe a nova data e horário do serviço", op.previsao.strftime("%d/%m/%Y %H:%M"))
            entrega = st.text_input("Informe a nova data e horário do serviço", op.entrega.strftime("%d/%m/%Y %H:%M"))
            nota_fiscal = st.text_input("Informe o novo nome do cliente", op.nota_fiscal)
            status = st.text_input("Informe o novo e-mail", op.status)        
            if st.button("Atualizar"):
                id_usuario = None
                if usuario != None: id_usuario = usuario.id
                View.pedido_atualizar(op.id, id_usuario, previsao, entrega, nota_fiscal, status)
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
                View.item_excluir(op.id)
                st.success("Pedido excluído com sucesso")
                time.sleep(2)
                st.rerun()