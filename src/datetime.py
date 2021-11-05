
# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
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
    # missing values are not included in the count of unique values
    return self.serie.dropna().unique().size

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    # missing values are None or numpy.NaN
    return self.serie.isna().sum()

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    # convert to a series of integers denoting weekday number, 0=Monday, 6=Sunday 
    day_nums = self.serie.dt.weekday
    
    return sum((day_nums == 5) | (day_nums == 6))

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    # convert to a series of integers denoting weekday number, 0=Monday, 6=Sunday 
    day_nums = self.serie.dt.weekday
    
    return sum((day_nums >= 0) & (day_nums <= 4))
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    # convert to a series of dates
    dates = self.serie.apply(lambda x: x.date())
    # get today's date
    today_date = pd.Timestamp.today().date()
    
    return sum(dates > today_date)

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    return sum(self.serie == pd.Timestamp(1900, 1, 1))

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    return sum(self.serie == pd.Timestamp(1970, 1, 1))

  def get_min(self):
    """
    Return the minimum date
    """
    return min(self.serie)

  def get_max(self):
    """
    Return the maximum date 
    """
    return max(self.serie)

  def get_barchart(self):
    """ 
    Return the generated bar chart for selected column
    """
    # get series of frequency value counts
    df = self.serie.value_counts()
    # return dataframe to be plotted as bar chart using st.bar_chart()
    return df

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    # get series of frequency value counts and convert to a dataframe
    df = pd.DataFrame(self.serie.value_counts()).reset_index()
    # name the columns
    df.columns = ["value", "occurrence"]
    # get grand total of counts
    total = df["occurrence"].sum()
    # calculate percentage column as a decimal number
    df["percentage"] = df["occurrence"] / total
    # return dataframe to be displayed using st.dataframe()
    return df
