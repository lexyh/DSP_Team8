# To be filled by students
import streamlit as st
import pandas as pd
import src.data as da
import src.datetime as dt
import src.numeric as nm
import src.text as tx

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
    st.write(df)
    st.write("Name of Table: ", uploaded_file.name)
    rows = da.get_n_rows()
    st.write("Number of Rows: " +rows)
    ### fill in other display information with data.py functions ###
    
    # get a dictionary of column data types
    dtype_dict = ds.get_cols_dtype()
    
    # loop through each column in the Dataset and display the information for the corrosponding data type
    for column in ds.df:
        # get the column data type
        dtype = dtype_dict[column]
        
        # for numeric columns
        if dtype == "int64" or dtype == "float64":
            # initialise NumericColumn object
            nc = nm.NumericColumn()
            nc.name = column
            nc.serie = ds.df[column]
            ### fill in other display information with numeric.py functions ###
            
        # for text columns
        elif dtype == "object":
            # initialise TextColumn object
            tc = tx.TextColumn()
            tc.name = column
            tc.serie = ds.df[column]
            ### fill in other display information with text.py functions ###
            
        elif dtype == "datetime64":
            # initialise DateColumn object
            dc = dx.DateColumn()
            dc.name = column
            dc.serie = ds.df[column]
            ### fill in other display information with datetime.py functions ###
            dc.get_barchart()
            dc.get_frequent()    