# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd




@dataclass
class Dataset():
  name: str = None
  df: pd.core.frame.DataFrame = None


  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return str(self.df.shape[0])

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return str(self.df.shape[1])

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    
    return self.df.columns.tolist() 

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return self.df.dtypes.to_dict()
   
  
    
  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return str(self.df[self.df.duplicated()].shape[0])

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return str((self.df.isna().sum(axis=1) > 0).sum())

  def get_head(self, number):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return self.df.head(n=number)

  def get_tail(self, number):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return self.df.tail(n=number)

  def get_sample(self, number):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return self.df.sample(n=number)

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
      
    """
        
    return self.df.select_dtypes('number').columns.tolist()

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    return self.df.select_dtypes('object').columns.tolist()

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    return self.df.select_dtypes('datetime').columns.tolist()

