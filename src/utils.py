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

def PlotImages(image1, image2):
    path1 = f'img/{image1}'
    path2 = f'img/{image2}'

    col1, col2 = st.columns(2)

    with col1:
        st.image(path1, use_column_width=True)
    
    with col2:
        st.image(path2, use_column_width=True)