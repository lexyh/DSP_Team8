import streamlit as st
import pandas as pd
import src.numeric as n


# read csv
csv_path = "01-01-2021.csv"
df = pd.read_csv('/Users/annahome/Documents/GitHub/DSP_Team8/test_app/01-01-2021.csv')

# init NumericColumn
dc = n.NumericColumn()
dc.col_name = "Last_Update"
dc.serie = pd.to_numeric(df[dc.col_name], dayfirst=True)

# read csv
df = pd.read_csv(csv_path)

st.title("Numeric Test")

dc.get_histogram()
dc.get_frequent()
