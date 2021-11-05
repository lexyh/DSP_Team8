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
    
    # display overall Dataset information in streamlit
    st.title("1. Overall Information")
    
    ## Write DF for testing app but remove in final submission
    st.write(ds.df)
    
    ## Write the name of the CSV that is uploaded in streamlit
    st.write("Name of Table: ", uploaded_file.name)
    
    ## Store Count number of rows and then write the number of rows
    rows = ds.get_n_rows()
    st.write("Number of Rows: " + rows)
    
    ## store Count number of columns and then write in streamlit the number of columns
    cols = ds.get_n_cols() 
   ## Needs to be finished    
    st.write("Number of Columns: " + cols) 
    
    ## write number of duplicate rows in streamlit
    
    st.write("Number of Duplicated Rows: " + ds.get_n_duplicates())
    
    ## Needs to be finished
    ##st.write("Number of Rows with Missing Values: " + ds.get_n_missing())
    
    
    ##Write List of column names and datatypes  in streamlit
    st.write("List of Columns")
    ## Needs to be finished
    st.write("Type of Columns")
    ## Needs to be in table format
    st.write(ds.get_cols_dtype())
    
    ## Create a slider in streamlit defaulting to allow user to select number of rows to be displayed in next three tables (default 5).
    number = st.slider('Select the numbers of rows to be displayed',0,int(rows),5)
    
    ## Write table in Streamlit showing top rows selected in slider (default 5)
    st.write("Top Rows of Table")
    st.dataframe(ds.get_head(number))
    
    ## Write table in Streamlit showing bottom rows selected in slider (default 5)
    st.write("Bottom Rows of Table")
    st.dataframe(ds.get_tail(number))
    
    ## Write table in Streamlit showing random rows selected in slider (default 5)
    st.write("Random Sample Rows of Table")
    st.dataframe(ds.get_sample(number))
    
    ## Multi select box which will only show text fields where the user can select to change them to datetime fields --Needs to finalised
    datecolumns = st.multiselect ("Which columns do you want to convert to dates?", ds.get_text_columns())
    if datecolumns is not None:
        st.write(datecolumns)
       ## ds.df[datecolumns] = pd.to_datetime(ds.df[datecolumns])
        

    st.write(ds.get_numeric_columns())
    st.write(ds.get_text_columns())
    st.write(ds.get_date_columns())
        
        
        