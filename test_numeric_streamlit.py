import streamlit as st
import pandas as pd
import src.numeric as n
from src.numeric import NumericColumn



# read csv
csv_path = "01-01-2021.csv"
df = pd.read_csv(csv_path)

# init NumericColumn
nc = n.NumericColumn()
nc.col_name = "Lat"
nc.serie = pd.to_numeric(df[nc.col_name])
col = NumericColumn()

# read csv
df = pd.read_csv(csv_path)

st.title("Numeric Test")


def numeric_summary(NumericColumn):

    summary = {}

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

st.dataframe(numeric_summary(col))


nc.get_histogram()
nc.get_frequent()