import chardet
import pandas as pd
import pygwalker as pyg
import streamlit as st
import streamlit.components.v1 as components

# ワイド表示
st.set_page_config(layout="wide")

# タイトル
st.title("Data Analysis with PyGWalker.")

# データフレームの用意
df = pd.DataFrame()

# ファイル選択
with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file")
    if uploaded_files is not None:
        result = chardet.detect(uploaded_files.getvalue())
        if result['encoding'] == 'shift_jis':
            encoding = 'cp932'
        elif result['encoding'] == None:
            encoding = 'cp932'
        else:
            encoding = result['encoding']
        df = pd.read_csv(uploaded_files, encoding=encoding)
        df

# Pygwalkerを使用してHTMLを生成する
pyg_html = pyg.to_html(df)
 
# HTMLをStreamlitアプリケーションに埋め込む
components.html(pyg_html, height=1000, scrolling=True)
