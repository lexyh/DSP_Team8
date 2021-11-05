# Author: A Ly
# defining the Numeric data class, imported as nm in the streamlit_app.py  

import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@dataclass
class NumericColumn():
  col_name: str = None
  serie: pd.Series = None

  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.nunique()

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    return ((self.serie==0).sum())

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return (self.serie < 0).sum()

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return self.serie.mean()

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return self.serie.std()
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return self.serie.max()

  def get_median(self):
    """
    Return the median value for selected column
    """
    return self.serie.median()
  
  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    data=self.serie
    fig, ax = plt.subplots()
    #set theme
    sns.set_style("whitegrid")
    #create histogram
    sns.histplot(data, x=self.serie, alpha=1, color = 'navy',  bins=50).set_title("Histogram")
    st.pyplot(fig)
  
  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    #create dataframe
    df = pd.DataFrame(self.serie.value_counts()).reset_index()
    # name columns
    df.columns = ["value", "occurrence"]
    # get grand total of counts
    total = df["occurrence"].sum()
    # calculate percentage column as a decimal number
    df["percentage"] = df["occurrence"] / total
    # display dataframe as table
    return st.dataframe(df)
