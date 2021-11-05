#test the text functions on a single column.

import streamlit as st
from dataclasses import dataclass
import pandas as pd
import plotly as py
import plotly.graph_objs as go
### TEXT SPECIFIC SCRIPTS READ IN ###
import text as txt
from text import TextColumn

### TESTING DATA SET ###
#file = r'C:\Users\lexyh\OneDrive\Documents\GitHub\DSP_Team8\src\Test_File.csv'
file = r'C:\Users\lexyh\Documents\Data Science\Data Science Practice\assignment3_template\Text_Data.csv'

### MANUALLY SPECIFIED VARIABLES ###
include_list = ['object', 'category', 'boolean']
exclude_list = ['datetime', 'datetime64', 'timedelta', 'timedelta64', 'datetimetz']
x = 5 # subheading number: calculated with a ticker in the app


### READ IN TEST DATA SET ###
data = pd.read_csv(file)

### SLICE DATA BY COLUMN TYPE -- TEXT ONLY###
text_cols = data.select_dtypes(include = include_list, exclude = exclude_list)
other_cols = data.drop(columns = text_cols.columns)

# DRAFT - INTRODUCTIONARY VARIABLES TO WRITE (prior to loop)
l1 = len(text_cols) #number of text columns
l2 = len(other_cols) #number of other columns
comment = (f'{l1} text columns exist in the loaded file')


### SPECIFY TEXT COLUMN : NO LOOP TESTING HERE ###
test = data[text_cols.columns[2]]

### MANUALLY CREATE OBJECT : NO LOOP ###
col = TextColumn()
col.col_name = test.name
col.serie = test

### DEFINE FUNCTIONS TO PRESENT RESULTS ###

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
    
def caption(md):

    """
    Logic to compile a caption to present underneath the mode for the column
    """
    if len(md) == 1:
        caption_text = "Note: A single mode found for this column."
    if len(md) > 1 :
        caption_text = "Note: Multiple modes found, some values are equally most frequent."
        
    return caption_text


### GET SPECIFIC RESULTS FOR COLUMN BEFORE WRITING ###
md = col.get_mode()
subheader_text = (f'3.{x}. Field Name: {col.col_name}')

  
### WRITE RESULTS TO STREAMLIT ###
st.subheader(subheader_text)

## WRITE SUMMARY ##
st.write("The characteristics of this column are shown below:")
st.dataframe(text_summary(col))

## WRITE MODE ##
st.write("The most frequent values in this column are: ")
# only print a caption if a value exists. 
if md is None:
    st.write('No Mode Found')
if md is not None:
    st.write(md)
st.caption(caption(md))

## WRITE FREQUENCY TABLE & GRAPH
st.write('Frequency Table:')
st.table(col.get_frequent()) #style.highlight_max(axis=0))
st.write('Frequency Graph:')
st.plotly_chart(col.get_barchart())