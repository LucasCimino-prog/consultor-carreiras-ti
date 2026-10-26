import streamlit as st
from motor import CareerExpert, UserData

st.title("Consultor Inteligente de Carreiras em TI")
st.write("Responda ao questionário abaixo para descobrir sua trilha ideal.")

afinidade_matematica = st.selectbox(
    "1. Qual sua afinidade com matemática e estatística?",
    ("Baixa", "Média", "Alta")
)

preferencia_atuacao = st.selectbox(
    "2. Qual sua preferência de atuação diária?",
    (
        "analisar dados brutos",
        "lidar com servidores",
        "criar layouts visuais",
        "construir pipelines",
        "garantir seguranca",
        "automatizar processos",
        "gerenciar infraestrutura",
        "escrever algoritmos logicos",
        "testar aplicacoes",
        "gerenciar projetos"
    )
)

ferramenta_afinidade = st.selectbox(
    "3. Qual sua linguagem/ferramenta de maior afinidade atual?",
    ("Python", "JavaScript", "Linux/Redes", "Nenhuma/Iniciante")
)

entrega_valor = st.selectbox(
    "4. Qual o tipo de entrega de valor preferida?",
    (
        "insights e predicoes",
        "regras de negocio e apis",
        "interface e experiencia do usuario",
        "infraestrutura de dados",
        "protecao contra invasoes",
        "esteiras de CI/CD e estabilidade",
        "alta disponibilidade e escalabilidade",
        "aplicativos para usuarios finais",
        "qualidade e prevencao de bugs",
        "alinhamento entre negocio e tecnologia"
    )
)

if st.button("Diagnosticar Trilha"):
    engine = CareerExpert()
    engine.reset()
    engine.declare(UserData(
        afinidade_matematica=afinidade_matematica,
        preferencia_atuacao=preferencia_atuacao,
        ferramenta_afinidade=ferramenta_afinidade,
        entrega_valor=entrega_valor
    ))
    engine.run()

    st.subheader("Resultado da Análise")
    st.success(f"**Trilha Recomendada:** {engine.recommendation}")
    st.info(f"**Justificativa:** {engine.justification}")