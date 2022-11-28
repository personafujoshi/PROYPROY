import streamlit as st
import pandas as pd
import gdown

#1nZkoRX8956K9lybIb-ARHZ3Jk4QLiDw0
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=YOURFILEID
  url="https://drive.google.com/uc?id=1nZkoRX8956K9lybIb-ARHZ3Jk4QLiDw0"
  output='data.csv'
  gdown.download(url,output,quiet=False)
  
download_data()
data=pd.read_csv('data.csv', sep=';', nrows=3000, parse_date=['FECHA'])
st.dataframe(data.head(20))
ind_nom=data["INDICE_NOMINAL"]
st.line_chart(ind_nom)
