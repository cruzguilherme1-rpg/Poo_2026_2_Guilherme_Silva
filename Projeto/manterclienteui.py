import streamlit as st
import pandas as pd
import time
from services import Service

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"]) 
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = Service.listar_clientes()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("informe o nome")
        email = st.text_input("informe o email")
        fone = st.text_input("informe o fone")
        if st.button("inserir"):
            Service.inserir_cliente(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        cliente = Service.listar_clientes()
        if len(cliente) == 0: st.write("Nenhum cliente cadastro")
        else:
            op = st.selectorbox("Atualização de clientes", cliente)
            nome = st.text_input("novo nome", op.get_nome())
            email = st.text_input("novo e-mail", op.get_email())
            fone = st.text_input("novo fone", op.get_fone())
            if st.button("atualizar"):
                id = op.get_id()
                Service.atualizar_cliente(id, nome, email,fone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        clientes = Service.listar_clientes()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else: 
            op = st.selectorbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                Service.excluir_cliente(id)
                st.success("Clientes excluído com sucesso")
                time.sleep(2)
                st.rerun()