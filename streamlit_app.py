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
            
class NumericColumn:
  data = pd.read_csv('01-01-2021.csv')
  col_name = data['Lat']
  serie = pd.Series(col_name)

  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.dropna().unique.size

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    return ((self.series==0).sum())

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return ((self.series>=0).sum())

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return self.series.mean()

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return self.series.std()
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return self.series.min()

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return self.series.max()

  def get_median(self):
    """
    Return the median value for selected column
    """
    return self.series.median()

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    return self.series.hist()

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return self.series.value_counts().nlargets(20)
