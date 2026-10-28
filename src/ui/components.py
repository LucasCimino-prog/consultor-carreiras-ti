import streamlit as st


def exibir_ranking(resultados):
    st.subheader("Top 3 Trilhas Compatíveis")
    for i, res in enumerate(resultados):
        st.markdown(f"### {i + 1}º {res['nome']} ({res['compatibilidade']}%)")
        st.progress(res['compatibilidade'] / 100.0)


def exibir_plano_acao(plano):
    st.subheader("Plano de Ação Personalizado")
    st.write(f"**Trilha Recomendada:** {plano['trilha']}")

    st.markdown("#### Skill Gaps (O que falta estudar)")
    if plano['gaps_identificados'] and plano['gaps_identificados'][
        0] == "Conhecimento base atingido. Foco em projetos complexos.":
        st.success(plano['gaps_identificados'][0])
    else:
        for gap in plano['gaps_identificados']:
            st.markdown(f"- {gap}")

    st.markdown("#### Certificações Sugeridas")
    for cert in plano['certificacoes_sugeridas']:
        st.markdown(f"- {cert}")

    st.markdown("#### Projeto para Portfólio")
    st.info(plano['projeto_portfolio'])