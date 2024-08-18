import streamlit as st
import pandas as pd

def PlotTitle(title: str):
  st.markdown(f"<h1 style='text-align: center; color: white'>{title}</h1>", unsafe_allow_html=True)

def PlotJustifyText(text: str):
  st.markdown(f"<p style='text-align: justify; color: white;'>{text}</p>", unsafe_allow_html=True)

def PlotGraph(plt):
  st.pyplot(plt)

def PlotMarkdown(text: str):
  st.markdown(text, unsafe_allow_html=True)

def LoadDatabases():
  kindle_data = pd.read_csv('databases/kindle_data_clean.csv')
  books = pd.read_csv('databases/goodreads_basic_info_2.csv')
  return kindle_data, books

def PlotImage(image: str):
  path = f'img/{image}'
  st.image(path, use_column_width=True)

def PlotImages(image1, image2):
    path1 = f'img/{image1}'
    path2 = f'img/{image2}'

    col1, col2 = st.columns(2)

    with col1:
        st.image(path1, use_column_width=True)
    
    with col2:
        st.image(path2, use_column_width=True)