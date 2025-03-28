import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = "https://blxwoqiaarfjnxodbftr.supabase.co"  
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJseHdvcWlhYXJmam54b2RiZnRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDMxOTQ5ODcsImV4cCI6MjA1ODc3MDk4N30.NEiyQZkVK7z1E8bjFTzDdSjwCQS2tP9FNfsWzJClypU"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def carregar_perguntas():
    response = supabase.table("perguntas").select("*").execute()
    return response.data

def adicionar_pergunta(enunciado, opcoes, resposta):
    response = supabase.table("perguntas").insert({
        "enunciado": enunciado,
        "opcoes": opcoes,
        "resposta": resposta
    }).execute()
    st.success("Pergunta adicionada com sucesso!")

def excluir_pergunta(id):
    response = supabase.table("perguntas").delete().eq("id", id).execute()
    st.success("Pergunta excluída com sucesso!")

def atualizar_pergunta(id, enunciado, opcoes, resposta):
    response = supabase.table("perguntas").update({
        "enunciado": enunciado,
        "opcoes": opcoes,
        "resposta": resposta
    }).eq("id", id).execute()
    st.success("Pergunta atualizada com sucesso!")

st.title("Painel Administrativo - Perguntas do Quiz")

st.header("Lista de Perguntas")
perguntas = carregar_perguntas()
for pergunta in perguntas:
    with st.expander(f"Pergunta {pergunta['id']}: {pergunta['enunciado']}"):
        st.write("Opções:", pergunta["opcoes"])
        st.write("Resposta correta:", pergunta["opcoes"][pergunta["resposta"]])

        # Botão para excluir a pergunta
        if st.button(f"Excluir Pergunta {pergunta['id']}"):
            excluir_pergunta(pergunta['id'])
      

        # Formulário para editar a pergunta
        with st.form(f"Editar Pergunta {pergunta['id']}"):
            novo_enunciado = st.text_input("Novo Enunciado", value=pergunta["enunciado"])
            novas_opcoes = [
                st.text_input("Nova Opção 1", value=pergunta["opcoes"][0]),
                st.text_input("Nova Opção 2", value=pergunta["opcoes"][1]),
                st.text_input("Nova Opção 3", value=pergunta["opcoes"][2]),
                st.text_input("Nova Opção 4", value=pergunta["opcoes"][3]),
            ]
            nova_resposta = st.number_input(
                "Nova Resposta Correta (índice da opção)",
                min_value=0,
                max_value=3,
                step=1,
                value=pergunta["resposta"],
            )
            submit_editar = st.form_submit_button("Salvar Alterações")
            if submit_editar:
                atualizar_pergunta(pergunta["id"], novo_enunciado, novas_opcoes, nova_resposta)
                 
# Seção para adicionar uma nova pergunta
st.header("Adicionar Nova Pergunta")
with st.form("nova_pergunta"):
    enunciado = st.text_input("Enunciado")
    opcoes = [
        st.text_input("Opção 1"),
        st.text_input("Opção 2"),
        st.text_input("Opção 3"),
        st.text_input("Opção 4"),
    ]
    resposta = st.number_input("Resposta correta (índice da opção)", min_value=0, max_value=3, step=1)
    submit = st.form_submit_button("Adicionar Pergunta")
    if submit:
        adicionar_pergunta(enunciado, opcoes, resposta)