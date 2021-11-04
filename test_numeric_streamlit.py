import streamlit as st
import pandas as pd
import src.numeric as n



# read csv
csv_path = "01-01-2021.csv"
df = pd.read_csv(csv_path)

# init NumericColumn
dc = n.NumericColumn()
dc.col_name = "Lat"
dc.serie = pd.to_numeric(df[dc.col_name])

# read csv
df = pd.read_csv(csv_path)

st.title("Numeric Test")


dc.get_histogram()
dc.get_frequent()
