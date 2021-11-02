# To be filled by students   
#!/bin/env python3
# To be filled by students
import unittest
from src.numeric import NumericColumn
import pandas as pd

class TestNumeric(unittest.TestCase):  
    def test_numeric(self):
        ### test on dummy data ###
        # create series of data
        dc1 = NumericColumn()
        dc1.col_name = "my_test"
        dc1.serie = pd.to_numeric(pd.Series(["13:01:01 01/01/2021", "1:01:01 PM 01/01/2021", None, "13:01:02 01/03/2021", "2021/01/03 13:01:02", "13:01:02 13/1/2021", "13:01:02 13/1/2022", "1900/01/01", "1970/01/01"]), dayfirst=True)

        # test methods
        self.assertEqual(dc1.get_name(),"my_test")
        self.assertEqual(dc1.get_unique(),7)
        self.assertEqual(dc1.get_missing(),1)
        self.assertEqual(dc1.get_zeros(),7)
        self.assertEqual(dc1.get_negatives(),1)
        self.assertEqual(dc1.get_mean(),1)
        self.assertEqual(dc1.get_std(),1)
        self.assertEqual(dc1.get_min(),1)
        self.assertEqual(dc1.get_max(),1))
        self.assertEqual(dc1.get_median(),1))
        
        ### test on covid-19 sample csv ###
        csv_path = "01-01-2021_test.csv"
        
        if csv_path:
            # read csv
            df = pd.read_csv(csv_path)

            # init NumericColumn
            dc2 = NumericColumn()
            dc2.col_name = "Last_Update"
            dc2.serie = pd.to_numeric(df[dc2.col_name], dayfirst=True)

            # test methods
            print("Outputs using file",csv_path)
            print("get_name =",dc2.get_name())
            print("get_unique =",dc2.get_unique())
            print("get_missing =",dc2.get_missing())
            print("get_zeros =",dc2.get_zeros())
            print("get_negatives =",dc2.get_negatives())
            print("get_mean =",dc2.get_mean())
            print("get_std =",dc2.get_std())
            print("get_min = ",dc2.get_min())
            print("get_max = ",dc2.get_max())
            print("get_median =",dc2.get_median())

if __name__ == '__main__':
    unittest.main()