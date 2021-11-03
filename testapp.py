# To be filled by students
import streamlit as st
import pandas as pd
import src.data as da
import src.datetime as dt
#import src.numeric as nm
#import src.text as tx

st.title("Data Explorer Tool")
# read data
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    # initialise Dataset object - this includes all data in the CSV
    ds = da.Dataset()
    ds.name = "my_dataset"
    # pandas is used to read the uploaded binary file as a CSV, then stored to the df attribute of Dataset object ds
    ds.df = pd.read_csv(uploaded_file)
    
    # display overall Dataset information
    st.title("1. Overall Information")
    st.write(ds.df)
    st.write("Name of Table: ", uploaded_file.name)
    rows = ds.get_n_rows()
    cols = ds.get_n_cols()
    
    st.write("Number of Rows: " + rows)
    st.write("Number of Columns: " + cols) 
    st.write("Number of Duplicated Rows: " + ds.get_n_duplicates())
    ##st.write("Number of Rows with Missing Values: " + ds.get_n_missing())
    
    st.write("List of Columns")
  
    st.write(ds.get_cols_dtype())
    st.write("Type of Columns")
    number = st.slider('Select the numbers of rows to be displayed',0,int(rows),5)
    st.write("Top Rows of Table")
    st.dataframe(ds.get_head(number))
    st.write("Bottom Rows of Table")
    st.dataframe(ds.get_tail(number))
    st.write("Random Sample Rows of Table")
    st.dataframe(ds.get_sample(number))