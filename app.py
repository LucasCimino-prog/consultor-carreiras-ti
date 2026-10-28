import streamlit as st
from src.engine import CareerEngineV2
from src.gap_analysis import GapAnalyzer
from src.ui.components import exibir_ranking, exibir_plano_acao

st.set_page_config(page_title="Consultor de Carreiras TI", layout="centered")


@st.cache_resource
def load_engine():
    return CareerEngineV2()


engine = load_engine()

# Controle de estado para o fluxo de telas (Wizard)
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1


def next_step():
    st.session_state.etapa += 1


def prev_step():
    st.session_state.etapa -= 1


def restart():
    st.session_state.clear()
    st.session_state.etapa = 1


st.title("Consultor Avançado de Carreiras em TI")

if st.session_state.etapa == 1:
    st.header("Passo 1: Seus Conhecimentos Atuais")
    st.write("Quais tecnologias você já possui algum nível de conhecimento prático?")

    techs_disponiveis = [
        "Python/Java/C#", "SQL e NoSQL", "Git", "HTML/CSS/JS",
        "React, Vue ou Angular", "Linux/Bash", "Docker básico",
        "Estatística Aplicada", "Testes de Software", "Scrum/Kanban",
        "Redes (TCP/IP)"
    ]

    st.session_state.conhecimentos = st.multiselect(
        "Selecione as tecnologias:",
        options=techs_disponiveis,
        default=st.session_state.get('conhecimentos', [])
    )

    st.button("Proximo Passo", on_click=next_step)

elif st.session_state.etapa == 2:
    st.header("Passo 2: Suas Afinidades")
    st.write("Avalie seu interesse de 1 (Muito Baixo) a 5 (Muito Alto) para cada área.")

    if 'respostas' not in st.session_state:
        st.session_state.respostas = {}

    for dim in engine.dimensoes:
        st.session_state.respostas[dim['id']] = st.slider(
            dim['pergunta'],
            min_value=1, max_value=5,
            value=st.session_state.respostas.get(dim['id'], 3)
        )

    col1, col2 = st.columns(2)
    with col1:
        st.button("Voltar", on_click=prev_step)
    with col2:
        st.button("Diagnosticar Trilha", on_click=next_step)

elif st.session_state.etapa == 3:
    st.header("Passo 3: Seu Diagnóstico e Roadmap")

    resultados = engine.calcular_compatibilidade(st.session_state.respostas)
    exibir_ranking(resultados)

    st.divider()

    trilha_vencedora = resultados[0]
    plano = GapAnalyzer.gerar_plano_acao(trilha_vencedora, st.session_state.conhecimentos)
    exibir_plano_acao(plano)

    st.divider()
    st.button("Refazer Teste", on_click=restart)