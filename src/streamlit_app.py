import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

with st.sidebar:
  selected = option_menu(
    menu_title="Menus Principal",
    options=["Análise Exploratória", "Testes de Hipótese", "Regressão e Classificação"],
    icons=["house", "book", "envelope"],
    menu_icon="book",
    default_index=0,
  )

  st.header('Introdução a Ciência de Dados(ICD-2024). \n Desenvolvido por: \n - Erik Neves \n - Gabriel Prudente \n - Vitor Costa \n - Philipe')

# Conteúdo do lado direito
if selected == "Análise Exploratória":
  st.title(selected)
  st.write("Nesta fase, realizamos uma análise exploratória dos dados, visualizando diferentes aspectos das informações coletadas. Utilizamos diversos gráficos para identificar padrões, tendências e possíveis relações entre variáveis. Essa etapa é crucial para obter insights preliminares e orientar as próximas fases da análise, garantindo uma compreensão mais profunda dos dados antes da aplicação de modelos mais complexos.")
  
elif selected == "Testes de Hipótese":
  st.title(f"Testes de Hipótese {selected}")
  
  col1, col2 = st.columns([2, 3])
  
  with col1:
    st.write("Conteúdo na coluna da esquerda para testes de hipótese...")
  
  with col2:
    st.write("Conteúdo na coluna da direita para testes de hipótese...")

elif selected == "Regressão e Classificação":
  st.title(f"Regressão e classificação {selected}")
  
  col1, col2 = st.columns([2, 3])
  
  with col1:
    st.write("Conteúdo na coluna da esquerda para regressão e classificação...")
  
  with col2:
    st.write("Conteúdo na coluna da direita para regressão e classificação...")
