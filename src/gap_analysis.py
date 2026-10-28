class GapAnalyzer:
    @staticmethod
    def gerar_plano_acao(trilha_recomendada, conhecimentos_usuario):
        """
        Cruza os conhecimentos atuais do usuário com as exigências da trilha
        para identificar lacunas (gaps) e estruturar o plano de ação.
        """
        techs_necessarias = set(trilha_recomendada["roadmap"]["tecnologias"])
        techs_conhecidas = set(conhecimentos_usuario)

        gaps = techs_necessarias - techs_conhecidas

        if not gaps:
            gaps_formatados = ["Conhecimento base atingido. Foco em projetos complexos."]
        else:
            gaps_formatados = list(gaps)

        return {
            "trilha": trilha_recomendada["nome"],
            "gaps_identificados": gaps_formatados,
            "certificacoes_sugeridas": trilha_recomendada["roadmap"]["certificacoes"],
            "projeto_portfolio": trilha_recomendada["roadmap"]["portfolio"]
        }