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
        dc1.serie = pd.to_datetime(pd.Series(["13:01:01 01/01/2021", "1:01:01 PM 01/01/2021", None, "13:01:02 01/03/2021", "2021/01/03 13:01:02", "13:01:02 13/1/2021" ]))

        # test methods
        self.assertEqual(dc1.get_name(),"my_test")
        self.assertEqual(dc1.get_unique(),3)
        self.assertEqual(dc1.get_missing(),1)
        
        ### test on covid-19 sample csv ###
        csv_path = "01-01-2021_test.csv"
        
        if csv_path:
            # read csv
            df = pd.read_csv(csv_path)

            # init DateColumn
            dc2 = DateColumn()
            dc2.col_name = "Last_Update"
            dc2.serie = pd.to_datetime(df[dc2.col_name])

            # test methods
            print("Outputs using file",csv_path)
            print("get_name =",dc2.get_name())
            print("get_unique =",dc2.get_unique())
            print("get_missing =",dc2.get_missing())

if __name__ == '__main__':
    unittest.main()