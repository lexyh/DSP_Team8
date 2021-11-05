#!/bin/env python3
# To be filled by students
import unittest
import src.data as da
import pandas as pd



class TestData(unittest.TestCase):  
    def test_data(self):

        ## Create a test data frame with a mixture of datetime,number and text columns. With a duplicate row and missing values
       
        
        # initialise Dataset object - this includes all data in the CSV
        ds = da.Dataset()
        ds.name = "my_dataset"

        ## Create a dict
        mydict = {'text_column':  ['first_value', 'second_value', 'third_value','third_value','fifth_value',None,None],
        'number_column': [1,None,3,4,5,6,6],
        'date_column1': [None, None, '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        'date_column2': ['1-7-2020', '2-7-2020', '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        }
        ##convert dictionary for testing
        ds.df = pd.DataFrame.from_dict(mydict)


        ##List of Expected Results used in test
        ExpRows='7'
        ExpCol='4'
        ExpDup='1'
        ExpMissing='4'
        ExpNumCols =str(['number_column'])
        ExpTextCols = str(['text_column', 'date_column1', 'date_column2'])

        ExpColNames = str(['text_column', 'number_column', 'date_column1', 'date_column2'])
        ExpColDataTypes = str("{'text_column': dtype('O'), 'number_column': dtype('float64'), 'date_column1': dtype('O'), 'date_column2': dtype('O')}")


        ## number for the slider to test gethead,tail and sample
        
        number = 5

        ds.df1 = pd.DataFrame({
            'name': ['Anna', 'Lex', 'Hayden','Suellen'],
            'date_of_birth': ['27/05/2001', '16/02/1999', '25/09/1998','11/11/2011']
        })

        ds.df1['date_of_birth'] = pd.to_datetime(ds.df1['date_of_birth'], format='%d/%m/%Y')

        ##List of Expected Results used in test
        ExpRows = '7'

        ## test methods for functions
        self.assertEqual(ds.get_n_rows(), ExpRows)
        self.assertEqual(ds.get_n_cols(), ExpCol)
        self.assertEqual(str(ds.get_cols_list()), ExpColNames)
        self.assertEqual(str(ds.get_cols_dtype()),ExpColDataTypes)
        self.assertEqual(ds.get_n_duplicates(), ExpDup)
        self.assertEqual(ds.get_n_missing(), ExpMissing)
        self.assertEqual(str(ds.get_numeric_columns()), ExpNumCols)
        self.assertEqual(str(ds.get_text_columns()), ExpTextCols)



    def test_data_date(self):

            # initialise Dataset object - this includes all data in the CSV
            ds = da.Dataset()
            ds.name = "my_dataset"

            ds.df = pd.DataFrame({
                'name': ['Anna', 'Lex', 'Hayden', 'Suellen'],
                'date_of_birth': ['27/05/2001', '16/02/1999', '25/09/1998', '11/11/2011']
            })

            ds.df['date_of_birth'] = pd.to_datetime(ds.df['date_of_birth'], format='%d/%m/%Y')
            print(ds.df)

            ExpDateCols = str(['date_of_birth'])
            self.assertEqual(str(ds.get_date_columns()),ExpDateCols)

if __name__ == '__main__':
    unittest.main()