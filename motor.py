import collections
import collections.abc
# Patch obrigatório para o Experta rodar no Python 3.10+
collections.Mapping = collections.abc.Mapping

from experta import KnowledgeEngine, Fact, Rule, MATCH

class UserData(Fact):
    """Fatos sobre o usuário."""
    pass

class CareerExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendation = None
        self.justification = None

    @Rule(UserData(afinidade_matematica='Alta', preferencia_atuacao='analisar dados brutos', ferramenta_afinidade='Python', entrega_valor='insights e predicoes'))
    def data_science(self):
        self.recommendation = "Ciência de Dados e Machine Learning"
        self.justification = "Forte base matemática, uso de Python e foco em análise e modelagem preditiva."

    @Rule(UserData(afinidade_matematica='Média', preferencia_atuacao='lidar com servidores', ferramenta_afinidade='Python', entrega_valor='regras de negocio e apis'))
    def backend(self):
        self.recommendation = "Desenvolvimento Back-end"
        self.justification = "Interesse na lógica de servidores, APIs e processamento de regras de negócio."

    @Rule(UserData(afinidade_matematica='Baixa', preferencia_atuacao='criar layouts visuais', ferramenta_afinidade='JavaScript', entrega_valor='interface e experiencia do usuario'))
    def frontend(self):
        self.recommendation = "Desenvolvimento Front-end & UI/UX"
        self.justification = "Foco na camada visual, interatividade e experiência direta do usuário."

    @Rule(UserData(afinidade_matematica='Alta', preferencia_atuacao='construir pipelines', ferramenta_afinidade='Python', entrega_valor='infraestrutura de dados'))
    def data_engineering(self):
        self.recommendation = "Engenharia de Dados"
        self.justification = "Interesse em arquitetura de dados, fluxos de ETL e infraestrutura de big data."

    @Rule(UserData(afinidade_matematica='Média', preferencia_atuacao='garantir seguranca', ferramenta_afinidade='Linux/Redes', entrega_valor='protecao contra invasoes'))
    def cybersecurity(self):
        self.recommendation = "Cibersegurança (Security / Pentesting)"
        self.justification = "Perfil focado em redes, sistemas operacionais e defesa cibernética."

    @Rule(UserData(afinidade_matematica='Média', preferencia_atuacao='automatizar processos', ferramenta_afinidade='Linux/Redes', entrega_valor='esteiras de CI/CD e estabilidade'))
    def devops(self):
        self.recommendation = "DevOps & SRE"
        self.justification = "Foco em automação, infraestrutura como código e integração contínua."

    @Rule(UserData(afinidade_matematica='Média', preferencia_atuacao='gerenciar infraestrutura', ferramenta_afinidade='Linux/Redes', entrega_valor='alta disponibilidade e escalabilidade'))
    def cloud(self):
        self.recommendation = "Computação em Nuvem (Cloud Architecture)"
        self.justification = "Interesse em arquitetura escalável e serviços de provedores em nuvem."

    @Rule(UserData(afinidade_matematica='Baixa', preferencia_atuacao='escrever algoritmos logicos', ferramenta_afinidade='Nenhuma/Iniciante', entrega_valor='aplicativos para usuarios finais'))
    def mobile(self):
        self.recommendation = "Desenvolvimento Mobile"
        self.justification = "Foco em soluções móveis e aplicativos portáteis."

    @Rule(UserData(afinidade_matematica='Baixa', preferencia_atuacao='testar aplicacoes', ferramenta_afinidade='Python', entrega_valor='qualidade e prevencao de bugs'))
    def qa(self):
        self.recommendation = "Engenharia de Qualidade e Testes (QA)"
        self.justification = "Perfil analítico voltado para automação de testes e garantia de qualidade."

    @Rule(UserData(afinidade_matematica='Baixa', preferencia_atuacao='gerenciar projetos', ferramenta_afinidade='Nenhuma/Iniciante', entrega_valor='alinhamento entre negocio e tecnologia'))
    def product(self):
        self.recommendation = "Gestão de Produtos (Product Management)"
        self.justification = "Foco na visão de negócios, priorização e metodologias ágeis."

    @Rule(UserData(afinidade_matematica=MATCH.m, preferencia_atuacao=MATCH.p, ferramenta_afinidade=MATCH.f, entrega_valor=MATCH.e))
    def default_rule(self, m, p, f, e):
        if not self.recommendation:
            self.recommendation = "Desenvolvimento Back-end"
            self.justification = "As respostas foram muito mistas. O Back-end oferece uma excelente base geral para transição futura."