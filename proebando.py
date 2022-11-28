import streamlit as st
import pandas as pd
import gdown

#1nZkoRX8956K9lybIb
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=YOURFILEID
  url="https://drive.google.com/uc?id=1nZkoRX8956K9lybIb"
  output='data.csv'
  gdown.download(url,output,quiet=False)
  
download_data()
data=pd.read_csv('data.csv', sep=';', nrows=1000000, parse_dates=['FECHA'])
st.dataframe(data.head(20))
fec=data["INDICE_NOMINAL"]
st.line_chart(fec)
