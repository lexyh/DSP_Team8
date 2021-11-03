#!/bin/env python3
# To be filled by students
import unittest
from src.datetime import DateColumn
import pandas as pd

class TestDateTime(unittest.TestCase):  
    def test_datetime(self):
        ### test on dummy data ###
        # create series of data
        dc1 = DateColumn()
        dc1.col_name = "my_test"
        dc1.serie = pd.to_datetime(pd.Series(["13:01:01 01/01/2021", "1:01:01 PM 01/01/2021", None, "13:01:02 01/03/2021", "2021/01/03 13:01:02", "13:01:02 13/1/2021", "13:01:02 13/1/2022", "1900/01/01", "1970/01/01"]), dayfirst=True)

        # test methods
        self.assertEqual(dc1.get_name(),"my_test")
        self.assertEqual(dc1.get_unique(),7)
        self.assertEqual(dc1.get_missing(),1)
        self.assertEqual(dc1.get_weekday(),7)
        self.assertEqual(dc1.get_weekend(),1)
        self.assertEqual(dc1.get_future(),1)
        self.assertEqual(dc1.get_empty_1900(),1)
        self.assertEqual(dc1.get_empty_1970(),1)
        self.assertEqual(dc1.get_min(),pd.Timestamp("1900/01/01 00:00:00"))
        self.assertEqual(dc1.get_max(),pd.Timestamp("2022/01/13 13:01:02"))
        
        ### test on covid-19 sample csv ###
        csv_path = "01-01-2021_test.csv"
        
        if csv_path:
            # read csv
            df = pd.read_csv(csv_path)

            # init DateColumn
            dc2 = DateColumn()
            dc2.col_name = "Last_Update"
            dc2.serie = pd.to_datetime(df[dc2.col_name], dayfirst=True)

            # test methods
            print("Outputs using file",csv_path)
            print("get_name =",dc2.get_name())
            print("get_unique =",dc2.get_unique())
            print("get_missing =",dc2.get_missing())
            print("get_weekend =",dc2.get_weekend())
            print("get_weekday =",dc2.get_weekday())
            print("get_future =",dc2.get_future())
            print("get_empty_1900 =",dc2.get_empty_1900())
            print("get_empty_1970 =",dc2.get_empty_1970())
            print("get_min = ",dc2.get_min())
            print("get_max = ",dc2.get_max())

if __name__ == '__main__':
    unittest.main()