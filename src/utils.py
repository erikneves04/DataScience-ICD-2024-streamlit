import streamlit as st

def PlotTitle(title: str):
  st.markdown(f"<h1 style='text-align: center; color: white'>{title}</h1>", unsafe_allow_html=True)

def PlotJustifyText(text: str):
  st.markdown(f"<p style='text-align: justify; color: white;'>{text}</p>", unsafe_allow_html=True)

def PlotMarkdown(text: str):
  st.markdown(text, unsafe_allow_html=True)

def PlotImage(image: str):
  path = f'img/{image}'
  st.image(path, use_column_width=True)