import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

def PlotTitle(title: str):
  st.markdown(f"<h1 style='text-align: center; color: white'>{title}</h1>", unsafe_allow_html=True)

def PlotJustifyText(text: str):
  st.markdown(f"<p style='text-align: justify; color: white;'>{text}</p>", unsafe_allow_html=True)

with st.sidebar:
  selected = option_menu(
    menu_title="Menus Principal",
    options=["Análise Exploratória", "Testes de Hipótese", "Regressão e Classificação"],
    icons=["house", "book", "envelope"],
    menu_icon="book",
    default_index=0,
  )

  st.header('Introdução a Ciência de Dados(ICD-2024/01) \n Desenvolvido por: \n - Erik Neves \n - Gabriel Prudente \n - Vitor Costa \n - Philipe')

PlotTitle(selected)

if selected == "Análise Exploratória":
  PlotJustifyText("Nesta fase, realizamos uma análise exploratória dos dados, visualizando diferentes aspectos das informações coletadas. Utilizamos diversos gráficos para identificar padrões, tendências e possíveis relações entre variáveis. Essa etapa é crucial para obter insights preliminares e orientar as próximas fases da análise, garantindo uma compreensão mais profunda dos dados antes da aplicação de modelos mais complexos.")
  
  with st.expander("Análise 1: Distribuição dos Dados"):
    st.write("Aqui você pode incluir gráficos e análises relacionados à distribuição dos dados.")
    # Exemplos de visualizações
    st.line_chart([1, 2, 3, 4])
    st.bar_chart([1, 2, 3, 4])

  with st.expander("Análise 2: Correlações"):
      st.write("Aqui você pode incluir gráficos e análises relacionadas às correlações entre variáveis.")
      # Exemplo de visualização
      st.area_chart([1, 2, 3, 4])

  with st.expander("Análise 3: Análise de Outliers"):
      st.write("Aqui você pode incluir gráficos e análises relacionadas à identificação e tratamento de outliers.")
      # Exemplo de visualização
      st.dataframe({
          'Coluna 1': [1, 2, 3, 4],
          'Coluna 2': [4, 3, 2, 1]
      })

elif selected == "Testes de Hipótese":
  PlotJustifyText("Nesta seção, realizamos testes de hipóteses para investigar as relações entre variáveis específicas no conjunto de dados. Utilizamos testes estatísticos para verificar se as diferenças observadas entre grupos são estatisticamente significativas ou se podem ser atribuídas ao acaso.")

elif selected == "Regressão e Classificação":
  PlotJustifyText("Nesse notebook temos como objetivo aplicar modelos de regressão para prever valores numéricos contínuos e modelos de classificação para categorizar dados em classes distintas. E, apartir dessa análise, extrair informações dos conjuntos de dados e hipóteses abordados previamente.")