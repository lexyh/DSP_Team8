#!/bin/env python3
# To be filled by students
import datetime
import pandas as pd

# read csv
df = pd.read_csv("01-01-2021_datetime_test.csv")

# init DateColumn
dc = datetime.DateColumn()
dc.col_name = "Last_Update"
dc.serie = df[dc.col_name]

# test methods
print("get_name =",dc.get_name())

print("get_unique =",dc.get_unique())

print("get_missing =",dc.get_missing())
