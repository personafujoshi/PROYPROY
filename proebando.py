import streamlit as st
import pandas as pd
import gdown

#1nZkoRX8956K9lybIb
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=YOURFILEID
  url="https://drive.google.com/uc?id=1nZkoRX8956K9lybIb"
  output="data.csv"
  gdown.download(url,output,quiet=False)
  
download_data()
data=pd.read_csv("data.csv",sep=";",nrows=1000000,parse_dates=["INDICE_NOMINAL","INDICE_REAL"])
st.dataframe(data.head(20))
fecha=data["FECHA"]
st.line_chart(fecha)
