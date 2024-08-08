import streamlit as st
import pandas as pd

def PlotTitle(title: str):
  st.markdown(f"<h1 style='text-align: center; color: white'>{title}</h1>", unsafe_allow_html=True)

def PlotJustifyText(text: str):
  st.markdown(f"<p style='text-align: justify; color: white;'>{text}</p>", unsafe_allow_html=True)


def PlotGraph(plt):
    st.pyplot(plt)

def LoadDatabases():
    kindle_data = pd.read_csv('databases/kindle_data_clean.csv')
    books = pd.read_csv('databases/goodreads_basic_info_2.csv')
    return kindle_data, books