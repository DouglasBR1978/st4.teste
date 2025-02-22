import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Cadastro de clientes", page_icon="📔")


def gravar_dados(nome, data_nasc, tipo):
    if len(nome) == 0:
        st.session_state["sucesso"] = False
        st.session_state["msgerro"] = "É necessário informar o nome"
    elif data_nasc > date.today():
        st.session_state["sucesso"] = False
        st.session_state["msgerro"] = (
            "A data de nascimento não pode ser maior que a data atual"
        )
        # apenas para saber como é possível zerar um conteúdo do text_input
        st.session_state.nome_cliente = ""
    else:
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome};{data_nasc};{tipo} \n")
        st.session_state["sucesso"] = True


st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente", key="nome_cliente")
dt_nasc = st.date_input("Data Nascimento", format="DD/MM/YYYY")
tipo = st.selectbox("Tipode cliente", ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button(
    "Cadastrar", on_click=gravar_dados, args=[nome, dt_nasc, tipo]
)

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.warning(st.session_state["msgerro"], icon="❌")