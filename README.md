# Sistema Especialista Inteligente para Mapeamento e Trilha de Carreira em TI

Sistema Especialista Baseado em Regras com Tratamento de Incerteza e Pontuação Ponderada desenvolvido em Python. O sistema atua como um consultor avançado, analisando o perfil multifacetado do usuário, calculando compatibilidade percentual, identificando lacunas de competências (skill gaps) e gerando um roadmap de estudos.

Trabalho acadêmico desenvolvido para o Centro Universitário Presidente Antônio Carlos (UNIPAC Barbacena).

## Arquitetura e Funcionalidades

O projeto foi refatorado para uma arquitetura modular, separando a base de conhecimento do motor de inferência:

* **Base de Conhecimento Desacoplada (JSON):** Regras, pesos e características das 10 trilhas de TI armazenados externamente em `data/regras_carreiras.json`.
* **Mecanismo de Ponderação:** Respostas capturadas em escala (1 a 5). O motor (`src/engine.py`) calcula a distância entre o perfil do usuário e o peso ideal de cada trilha.
* **Skill Gap Analysis:** Módulo (`src/gap_analysis.py`) que cruza as tecnologias já conhecidas pelo usuário com as exigidas pela trilha recomendada.
* **Interface Wizard (Streamlit):** Navegação multi-etapas guiando o usuário desde os conhecimentos prévios até a visualização de gráficos de barras (gerados via Pandas) com a compatibilidade final.

## Tecnologias Utilizadas

* Python 3.10+
* Pandas (Estruturação de dados e plotagem gráfica)
* Streamlit (Interface Web interativa)

## Como Instalar e Executar

1. Clone este repositório:
```bash
git clone https://github.com/LucasCimino-prog/consultor-carreiras-ti.git
cd consultor-carreiras-ti