### Imports ###
import streamlit as st
import pandas as pd
import numpy as np
import src.data as da
import src.datetime as dt
import src.numeric as nm
import src.text as tx

### Sub functions ###
def dataset_output(file_name, ds):
    # display overall Dataset information in streamlit
    st.title("1. Overall Information")
     
    # Write the name of the CSV that is uploaded in streamlit
    st.write("Name of Table: ", file_name)
    
    # Store Count number of rows and then write the number of rows
    rows = ds.get_n_rows()
    st.write("Number of Rows: " + rows)
    
    # store Count number of columns and then write in streamlit the number of columns
    cols = ds.get_n_cols()    
    st.write("Number of Columns: " + cols) 
    
    # write number of duplicate rows in streamlit
    st.write("Number of Duplicated Rows: " + ds.get_n_duplicates())
    
    # write number of  rows with missing values in any variable in streamlit
    st.write("Number of Rows with Missing Values: " + ds.get_n_missing())
    
    # write list of columns in streamlit
    st.subheader("List of Columns:")
    st.write(', '.join(ds.get_cols_list()))
    
    # Write List of column names and datatypes  in streamlit
    st.subheader("Type of Columns:")
    df_types = pd.DataFrame(ds.df.dtypes, columns=['Type'])
    df_types = df_types.astype(str)
    st.dataframe(df_types)
    
    # Create a slider in streamlit defaulting to allow user to select number of rows to be displayed in next three tables (default 5).
    number = st.slider('Select the numbers of rows to be displayed',0,int(rows),5)
    
    # Write table in Streamlit showing top rows selected in slider (default 5)
    st.subheader("Top Rows of Table")
    st.dataframe(ds.get_head(number))
    
    # Write table in Streamlit showing bottom rows selected in slider (default 5)
    st.subheader("Bottom Rows of Table")
    st.dataframe(ds.get_tail(number))
    
    # Write table in Streamlit showing random rows selected in slider (default 5)
    st.subheader("Random Sample Rows of Table")
    st.dataframe(ds.get_sample(number))

def numeric_summary(NumericColumn):

    summary = {}    #initialise empty dict
    
    # write functions to dictionary
    summary["Missing Values"] = NumericColumn.get_missing()
    summary["Unique Values"] = NumericColumn.get_unique()
    summary["Number Rows with 0"] = NumericColumn.get_zeros()
    summary["Number of Rows with Negative Values"] = NumericColumn.get_negatives()
    summary["Average Value"] = NumericColumn.get_mean()
    summary["Standard Deviation Value"] = NumericColumn.get_std()
    summary["Minimum Value"] = NumericColumn.get_min()
    summary["Maximum Value"] = NumericColumn.get_max()
    summary["Median Value"] = NumericColumn.get_median()

    df = pd.DataFrame(pd.Series(summary).reset_index()) 
    df.columns = ["Value Category", "Counts"]
    
    return df
    
def datetime_summary(DateColumn):

    summary = {}    #initialise empty dict
    
    # write functions to dictionary
    summary["Missing Values"] = DateColumn.get_missing()
    summary["Unique Values"] = DateColumn.get_unique()
    summary["Number of weekend dates"] = DateColumn.get_weekend()
    summary["Number of weekday dates"] = DateColumn.get_weekday()
    summary["Number of future dates"] = DateColumn.get_future()

    df = pd.DataFrame(pd.Series(summary).reset_index()) 
    df.columns = ["Value Category", "Counts"]
    
    return df

def text_summary(TextColumn):
    """
    Pass text column methods to column to return value counts
    Compile data into a pandas dataframe & return

    Expected parameter: TextColumn() 
    Class: defined in text.py
    """

    summary = {}    #initialise empty dict

    # write functions to dictionary
    summary["Missing Values"] = TextColumn.get_missing()
    summary["Whitespace Values"] = TextColumn.get_whitespace()
    summary["Unique Values"] = TextColumn.get_unique()
    summary["Empty Values"] = TextColumn.get_empty()
    summary["All Lowercase"] = TextColumn.get_lowercase()
    summary["All Uppercase"] = TextColumn.get_uppercase()
    summary["Only Alphabet Characters"] = TextColumn.get_alphabet()
    summary["Only (numeric) Digits"] = TextColumn.get_digit()
    
    # convert to dataframe to allow streamlit to display the dictionary
    df = pd.DataFrame(pd.Series(summary).reset_index())
    df.columns = ["Value Category", "Counts"]

    return df

def mode_caption(md):
    """
    Logic to compile a caption to present underneath the mode for the column.
    Expected Input:
     - md: list 
     - md description: List derived from get_mode() funcions in defined in text.py, numeric.py, datetime.py
    Output: 
     - int: length of list object
    """
    
    if len(md) == 1:
        caption_text = "Single mode found for this column."
    if len(md) > 1 :
        caption_text = "Note: Multiple values in this column are equally most frequent."

    return caption_text

### Main program ###
st.title("Data Explorer Tool")

# select CSV data file
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    file_name = uploaded_file.name
    st.write(f'Your file {file_name} was uploaded sucessfully.')

    # initialise Dataset object - this includes all data in the CSV
    ds = da.Dataset()
    ds.name = file_name
    # pandas is used to read the uploaded binary file as a CSV, then stored to the df attribute of Dataset object ds
    ds.df = pd.read_csv(uploaded_file)
    
    # display overall Dataset information
    dataset_output(file_name, ds)
    
    # get a dictionary of column data types
    dtype_dict = ds.get_cols_dtype()
    
    # Multi select box which will only show text fields where the user can select to change them to datetime fields --I NEED HELP PLEASE
    date_cols = st.multiselect ("Which columns do you want to convert to dates?", ds.get_text_columns())
    if date_cols is not None:
        for key in dtype_dict:
            if key in date_cols:
                dtype_dict[key] = np.dtype("datetime64")
    
    # create counters for writing subheading
    # used to write the relevant subheading text to the app for each column loop
    t = 1   #counter to track the text column instance it is, used to format the display subtitle
    d = 1   #date
    n = 1   #numeric
    
    # loop through each column in the Dataset and display the information for the corrosponding data type
    # for numeric columns
    for column in ds.df:
        # get the column data type
        dtype = dtype_dict[column]
        
        if dtype == np.int64 or dtype == np.float64:
            # initialise NumericColumn object
            nc = nm.NumericColumn()
            nc.col_name = column
            nc.serie = ds.df[column]
            
            # display heading and increment numbering
            subheader_text = (f'1.{n}. Field Name: {nc.col_name}') #subheading content
            st.subheader(subheader_text)
            st.write('Numerical Column')
            n += 1
            
            # display results
            st.write(numeric_summary(nc).assign(hack="").set_index("hack"))    # hack to remove the index numbers
            nc.get_histogram()
            st.write("Most Frequent Values")
            nc.get_frequent()
            
    # for datetime columns
    for column in ds.df:
        # get the column data type
        dtype = dtype_dict[column]    
        
        if dtype == np.datetime64:
            # initialise DateColumn object
            dc = dt.DateColumn()
            dc.col_name = column
            dc.serie = pd.to_datetime(ds.df[column], dayfirst=True)
            
            # display heading and increment numbering
            subheader_text = (f'2.{d}. Field Name: {dc.col_name}') #subheading content
            st.subheader(subheader_text)
            st.write('Date-Time Column')
            d += 1
            
            # display results
            st.write("The characteristics of this column are shown below:") 
            st.write(datetime_summary(dc).assign(hack="").set_index("hack"))    # hack to remove the index numbers
            st.write(f"Minimum value = {dc.get_min()}")
            st.write(f"Maximum value = {dc.get_max()}")
            
            st.write('Frequency Graph:')
            st.bar_chart(dc.get_barchart())
            st.write('Frequency Table:')
            st.dataframe(dc.get_frequent())  
            
    # for text columns
    for column in ds.df:
        # get the column data type
        dtype = dtype_dict[column]
        
        if dtype == "object":
            # initialise TextColumn object
            tc = tx.TextColumn()
            tc.col_name = column
            tc.serie = ds.df[column]            
       
            # return specific results for column before writing
            subheader_text = (f'3.{t}. Field Name: {tc.col_name}') #subheading content
            md = tc.get_mode() #return mode (dataframe object)
            mds = md.style.hide_index() #hide the index before printing

            # write heading to streamlit and increment heading number
            st.subheader(subheader_text)
            st.write('Text Column')
            t += 1
            
            # write summary
            st.write("The characteristics of this column are shown below:")                  
            st.dataframe(text_summary(tc).assign(hack="").set_index("hack"))    # hack to remove the index numbers

            # write mode
            st.write("The most frequent values in this column are: ")
            # Check mode and write values and calculated caption
            if md is None:
                st.write('No Mode Found')
            if md is not None:
                st.write(mds)
            st.caption(mode_caption(md))

            # write frequency table & graph
            st.write('Frequency Table:')
            st.table(tc.get_frequent()) #style.highlight_max(axis=0)) #highlighting included but can be toggled off. 
            st.write('Frequency Graph:')
            st.write("The graph below plots the frequency of values in thhe column from most frequent to least frequent.")
            st.write("Hover over a bar to see specific details. Use the arrows to open the chart in a larger window.")
            st.plotly_chart(tc.get_barchart())  
