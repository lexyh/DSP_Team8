# To be filled by students
import streamlit as st
import pandas as pd
import src.data1 as da
import src.datetime as dt

st.title("Data Explorer Tool")
# read data
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    df =da.Dataset()
    df = pd.read_csv(uploaded_file)
    st.title("1. Overall Information")
    st.write(df)
    st.write("Name of Table: ", uploaded_file.name)
   # rows = da.get_n_rows()
    
    # st.write("Number of Rows: " +rows)
    

    

# init DateColumn
    dc = dt.DateColumn()
    dc.col_name = "Last_Update"
    dc.serie = pd.to_datetime(df[dc.col_name], dayfirst=True)

    # read csv
    ##df = pd.read_csv(csv_path)

    st.title("Datetime Test")

    dc.get_barchart()
    dc.get_frequent()    