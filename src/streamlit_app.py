import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu

import utils, Exploratory_Analysis, Hypothesis_Tests, Regression_Classification

with st.sidebar:
  selected = option_menu(
    menu_title="Menus Principal",
    options=["Análise Exploratória", "Testes de Hipótese", "Regressão e Classificação"],
    icons=["house", "book", "envelope"],
    menu_icon="book",
    default_index=0,
  )

  st.header('Introdução a Ciência de Dados(ICD-2024/01) \n Desenvolvido por: \n - Erik Neves \n - Gabriel Prudente \n - Vitor Costa \n - Philipe')

utils.PlotTitle(selected)

if selected == "Análise Exploratória":
  utils.PlotJustifyText("Nesta fase, realizamos uma análise exploratória dos dados, visualizando diferentes aspectos das informações coletadas. Utilizamos diversos gráficos para identificar padrões, tendências e possíveis relações entre variáveis. Essa etapa é crucial para obter insights preliminares e orientar as próximas fases da análise, garantindo uma compreensão mais profunda dos dados antes da aplicação de modelos mais complexos.")
  
  for topic in Exploratory_Analysis.Topics():
      with st.expander(topic[0]):
          topic[1]()

elif selected == "Testes de Hipótese":
  utils.PlotJustifyText("Nesta seção, realizamos testes de hipóteses para investigar as relações entre variáveis específicas no conjunto de dados. Utilizamos testes estatísticos para verificar se as diferenças observadas entre grupos são estatisticamente significativas ou se podem ser atribuídas ao acaso.")

elif selected == "Regressão e Classificação":
  utils.PlotJustifyText("Nesse notebook temos como objetivo aplicar modelos de regressão para prever valores numéricos contínuos e modelos de classificação para categorizar dados em classes distintas. E, apartir dessa análise, extrair informações dos conjuntos de dados e hipóteses abordados previamente.")