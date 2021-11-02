import streamlit as st
import pandas as pd

# read csv
csv_path = "01-01-2021_test.csv"
df = pd.read_csv(csv_path)

# init DateColumn
dc = dt.DateColumn()
dc.col_name = "Last_Update"
dc.serie = pd.to_datetime(df[dc.col_name], dayfirst=True)

# read csv
df = pd.read_csv(csv_path)

st.title("Datetime Test")

dc.get_barchart()
dc.get_frequent()