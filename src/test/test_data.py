# To be filled by students
import unittest
from src.data import Dataset
import pandas as pd


class TestData(unittest.TestCase):  
    def test_datetime(self):

        ## Create a test data frame with a mixture of datetime,number and text columns. With a duplicate row and missing values
       
        
        # initialise Dataset object - this includes all data in the CSV
        ds1 = da.Dataset()
        ds1.name = "my_test"
        
        ds1.df = {'text_column':  ['first_value', 'second_value', 'third_value','third_value','fifth_value',None,None],
        'number_column': [1,None,3,4,5,6,6],
        'date_column1': [None, '2/7/2020', '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        'date_column2': ['1-7-2020', '2-7-2020', '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        }
        
        ds1.df = pd.DataFrame(data)
        
        ##Expected Results
        ExpRows=7
        ExpCol=4
        ExpDup=1
        ExpMissing=3
        ExpHead =  {'text_column':  ['first_value', 'second_value', 'third_value','third_value','fifth_value'],
        'number_column': [1,None,3,4,5,6,6],
        'date_column1': [None, '2/7/2020', '3/7/2020','4/7/2020','5/7/2020'],
        'date_column2': ['1-7-2020', '2-7-2020', '3/7/2020','4/7/2020','5/7/2020'],
        }
        
        ExpTail == {'text_column':  [ 'third_value','third_value','fifth_value',None,None],
        'number_column': [3,4,5,6,6],
        'date_column1': [ '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        'date_column2': [ '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        }
        
       
        ExpSample = ds1.df.sample(5)
        ExpNumCols
        ExpTextCols
        ExpDateCols
        
        
        ## number for the slider to test gethead,tail and sample
        
        number = 5
        
      

        ## test methods
        self.assertEqual(ds1.get_n_rows(),ExpRows)
        self.assertEqual(ds1.get_n_cols(),ExpCol)
        #self.assertEqual(ds1.get_cols_list(),1)
        #self.assertEqual(ds1.get_cols_dtype(),7)
        self.assertEqual(ds1.get_n_duplicates(),ExpDup)
        self.assertEqual(ds1.get_n_missing(),ExpMissing)
        self.assertEqual(ds1.get_head(),ExpHead)
        # self.assertEqual(ds1.get_tail(),)
        # self.assertEqual(ds1.get_sample(),)
        # self.assertEqual(ds1.get_numeric_columns(),)
        # self.assertEqual(ds1.get_text_columns(),)
        # self.assertEqual(ds1.get_date_columns(),)
        
if __name__ == '__main__':
    unittest.main()
