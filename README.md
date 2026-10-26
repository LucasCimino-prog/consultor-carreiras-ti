# Consultor Inteligente de Carreiras em TI (Fase 1)

Sistema Especialista baseado em regras desenvolvido em Python para atuar como um consultor de carreiras. O sistema diagnostica e recomenda a trilha de tecnologia mais adequada para o usuário dentre 10 opções possíveis, utilizando um motor de inferência lógica.

Trabalho acadêmico desenvolvido para o Centro Universitário Presidente Antônio Carlos (UNIPAC Barbacena).

## Funcionalidades

* **Entrevista Dinâmica:** Coleta dados do usuário sobre afinidade matemática, preferência de atuação, ferramentas de domínio e tipo de entrega de valor.
* **Motor de Inferência (Experta):** Base de conhecimento estruturada com regras lógicas de encadeamento para frente (Forward Chaining).
* **Justificativa Transparente:** Exibe a trilha recomendada acompanhada da regra disparada que justificou a decisão.
* **Interface Web:** Aplicação interativa desenvolvida com Streamlit.

## Tecnologias Utilizadas

* Python 3.10+
* [Experta](https://pypi.org/project/experta/) (Motor de Regras)
* [Streamlit](https://streamlit.io/) (Interface Gráfica)

## Como Instalar e Executar

1. Clone este repositório:
```bash
git clone https://github.com/LucasCimino-prog/consultor-carreiras-ti.git
cd consultor-carreiras-ti