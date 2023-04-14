import streamlit as st
import pandas as pd

st.title("Emotion Analyzer")
data = pd.read_csv("empdata.csv") #path folder of the data file
st.write(data)