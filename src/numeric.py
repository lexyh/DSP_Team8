# To be filled by students

import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class NumericColumn:
  data = pd.read_csv('01-01-2021.csv')
  col_name: data['Lat']
  serie: pd.Series(col_name)
 
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
