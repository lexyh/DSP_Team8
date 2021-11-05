
#!/bin/env python3
import unittest
from src.numeric import NumericColumn
import pandas as pd

class TestNumeric(unittest.TestCase):  
    def test_numeric(self):
        ### test on sample 01.01.2021.csv
        # create series of data
        nc1 = NumericColumn()
        nc1.col_name = "test"
        nc1.serie = pd.Series([None,28.0339, -11.2027, -30, -45, 0, 34.90171875, 34.90171875, 30.86747479,0])

        testdata = pd.Series([None,28.0339, -11.2027, -30, -45, 0, 34.90171875, 34.90171875, 30.86747479,0])

        # test methods
        self.assertEqual(nc1.get_name(),"test")
        self.assertEqual(nc1.get_unique(),testdata.nunique())
        self.assertEqual(nc1.get_missing(),1)
        self.assertEqual(nc1.get_zeros(),2)
        self.assertEqual(nc1.get_negatives(),3)
        self.assertEqual(nc1.get_mean(),testdata.mean())
        self.assertEqual(nc1.get_std(),testdata.std())
        self.assertEqual(nc1.get_min(),testdata.min())
        self.assertEqual(nc1.get_max(),testdata.max())
        self.assertEqual(nc1.get_median(),testdata.median())
        self.assertTrue(nc1.get_histogram() is not None)
        self.assertTrue(nc1.get_frequent() is not None)
        
        ### test on covid-19 sample csv ###
        csv_path = "01-01-2021.csv"
        
        if csv_path:
            # read csv
            df = pd.read_csv(csv_path)

            # init NumericColumn
            nc2 = NumericColumn()
            nc2.col_name = "Lat"
            nc2.serie = df["Lat"]

            # test methods
            print("Outputs using file",csv_path)
            print("get_name =",nc2.get_name())
            print("get_unique =",nc2.get_unique())
            print("get_missing =",nc2.get_missing())
            print("get_zeros =",nc2.get_zeros())
            print("get_negatives =",nc2.get_negatives())
            print("get_mean =",nc2.get_mean())
            print("get_std =",nc2.get_std())
            print("get_min = ",nc2.get_min())
            print("get_max = ",nc2.get_max())
            print("get_median =",nc2.get_median())

if __name__ == '__main__':
    unittest.main()