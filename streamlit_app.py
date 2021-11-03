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
    st.write(ds.df)
    st.write("Name of Table: ", uploaded_file.name)
    rows = ds.get_n_rows()
    cols = ds.get_n_cols()
    
    st.write("Number of Rows: " + rows)
    st.write("Number of Columns: " + cols) 
    
    number = st.slider('Select the numbers of rows to be displayed',0,int(rows),5)
    st.write("Top Rows of Table")
    st.dataframe(ds.get_head(number))
    st.write("Bottom Rows of Table")
    st.dataframe(ds.get_tail(number))
    st.write("Random Sample Rows of Table")
    st.dataframe(ds.get_sample(number))
    ### fill in other display information with data.py functions ###
    
    # get a dictionary of column data types
    dtype_dict = ds.get_cols_dtype()
    
    # create counters for writing subheading
    # used to write the relevamt subheading text to the app for each column loop

    t = 0 #counter for to track the text column instance it is. 
    d = 0
    n = 0

    # loop through each column in the Dataset and display the information for the corrosponding data type
    for column in ds.df:
        # get the column data type
        dtype = dtype_dict[column]
        
        # for numeric columns
        if dtype == "int64" or dtype == "float64":
            # initialise NumericColumn object
            nc = nm.NumericColumn()
            nc.col_name = column
            nc.serie = ds.df[column]
            ### fill in other display information with numeric.py functions ###
            
        # for text columns
        elif dtype == "object": 
            # update counter for text columns 
            t = t+1
            
            # initialise TextColumn object
            tc = tx.TextColumn()
            tc.col_name = column
            tc.serie = ds.df[column]
            
            ### display information with text.py functions ###

            def text_summary(TextColumn):
                """
                Pass text column methods to column to return value counts
                Compile data into a pandas dataframe & return
                
                Expected parameter: TextColumn() 
                Class: defined in text.py
                """
                
                summary = {}
                summary["Missing Values"] = TextColumn.get_missing()
                summary["Whitespace Values"] = TextColumn.get_whitespace()
                summary["Unique Values"] = TextColumn.get_unique()
                summary["Empty Values"] = TextColumn.get_empty()
                summary["All Lowercase"] = TextColumn.get_lowercase()
                summary["All Uppercase"] = TextColumn.get_uppercase()
                summary["Only Alphabet Characters"] = TextColumn.get_alphabet()
                summary["Only (numeric) Digits"] = TextColumn.get_digit()
                
                #convert to dataframe to allow streamlit to display the dictionary
                
                df = pd.DataFrame(pd.Series(summary).reset_index()) 
                df.columns = ["Value Category", "Counts"]
                
                return df

            def mode_caption(md):

                """
                Logic to compile a caption to present underneath the mode for the column
                """
                caption_text = None #empty string 
            
                if md is None:
                    caption_text = "No values shown as all values in the selected are unique"
                if len(md) > 1 :
                    caption_text = "Note: Multiple values in this column are equally most frequent."
                    
                return caption_text

            # load in results for mode and subheading
            subheader_text = (f'3.{t}. Field Name: {tc.col_name}') #subheading content
            md = tc.get_mode() #return mode

            # write to stremlit
            st.subheader(tc.subheader_text)

            st.write("The characteristics of this column are shown below:")
                    
            st.dataframe(text_summary(tc))

            st.write("The most frequent values in this column are: ")
            # logic to prepare caption to write under the 'mode' results. 
            if md is None:
                st.write('No Mode Found')
            if md is not None:
                st.write(md)
            st.caption(mode_caption(md))

            st.write('Frequency Table:')
            st.dataframe(tc.get_frequent().style.highlight_max(axis=0)) #highlighting included but can be toggled off. 

            st.write('Frequency Graph:')
            st.plotly_chart(tc.get_barchart())


        elif dtype == "datetime64":
            # initialise DateColumn object
            dc = dt.DateColumn()
            dc.col_name = column
            dc.serie = ds.df[column]
            ### fill in other display information with datetime.py functions ###
            dc.get_barchart()
            dc.get_frequent()    
