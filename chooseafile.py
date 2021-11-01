import pandas as pd
from dataclasses import dataclass
import streamlit as st



st.title("Data Explorer Tool")


uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:

          df = pd.read_csv(uploaded_file)
                  

          st.title("1. Overall Information")  
          st.write("Name of Table: ", uploaded_file.name)

          rows = str(df.shape[0])
          cols = str(df.shape[1])
          st.write("Number of Rows: " + rows)
          st.write("Number of Columns: " +cols)    
          dfdup =df[df.duplicated()]

          rowsdup = str(dfdup.shape[0])
          
          st.write('Number of Duplicated Rows: ' +rowsdup)
          st.write("Display number of rows with missing values: " +str((df.isna().sum(axis=1) > 0).sum()))
          st.write("Display top N rows (default 5 rows) of dataset:")


          st.write("List of Columns")
          st.write (str(df.columns.values))
          
          df_types = pd.DataFrame(df.dtypes, columns=['Type'])
          numerical_cols = df_types[~df_types['Type'].isin(['object',
                           'bool'])].index.values
                      
          st.write('Summary:')
          df_types = df_types.astype(str)
          st.dataframe(df_types)
          number = st.slider('Select the numbers of rows to be displayed',0,int(rows),5)
          st.write("Top Rows of Table")
          st.dataframe(df.head (number))
          st.write("Bottom Rows of Table")
          st.dataframe(df.tail (number))
          st.write("Random Sample Rows of Table")
          st.dataframe(df.sample (number))



      
 