# To be filled by students
# Unit Testing for the TextColumn script. 
import unittest
from src.text import TextColumn
import pandas as pd

# read in dummy data to use as a test source.
#df = "text_test.csv"

# TextColumn() class defined with the following functions. 
# get_name
# get_unique
# get_missing
# get_empty
# get_whitespace
# get_lowercase
# get_uppercase
# get_alphabet
# get_digit
# get_mode
# get_frequent
# get_barchart

class TestTextColumn(unittest.TestCase):
    def test_attributes(self):
        
        #test variables
        col_empty_input = TextColumn()
        col_empty_input.col_name = ""
        col_empty_input.serie = pd.Series({})
        col_test_unnamed = TextColumn()
        
        #Assignment as Expected where empty
        self.assertEqual(col_empty_input.col_name, "") #object created even where empty data input
        self.assertEqual(col_empty_input.serie, {}) # series attribute created even when no values
        
    def test_functions(self):
            
            #instantiate
            col = TextColumn()
            #create test object
            col.serie = pd.Series(['IT WOULD','BE SO GOOD','BE SO GOOD','BE SO GOOD','be so good','true','false',0.65,0.58,'n/a','howierlkn',765765876, '%^&^%&^','',345,None,None,98,'   ',13434645])
            col.col_name = "Column1"
            
            #expected values
            n = 20
            n_unique = 16
            n_missing = 2 #note: raw csv seems to read in "n/a" as null. But writing it directly returns a string value.
            n_empty = 1
            n_whitespace = 1
            n_lowercase = 4
            n_uppercase = 4
            n_alphabet = 8
            n_digit = 4 #note only reads in full integers as numeric by the looks of it
                            
            #logic checks
        
            self.assertEqual(col.get_name(), "Column1")
            self.assertEqual(col.get_unique(), n_unique)
            self.assertEqual(col.get_missing(), n_missing)
            self.assertEqual(col.get_empty(), n_empty)
            self.assertEqual(col.get_whitespace(), n_whitespace)
            self.assertEqual(col.get_lowercase(), n_lowercase)
            self.assertEqual(col.get_uppercase(), n_uppercase)
            self.assertEqual(col.get_alphabet(), n_alphabet)
            self.assertEqual(col.get_digit(), n_digit)
            self.assertTrue(isinstance(col.get_mode), list) #returned mode should be a list object
            self.assertTrue(col.get_barchart() is not None)
            self.assertTrue(col.get_frequent() is not None)
            #get_frequent()

if __name__ == '__main__':
    unittest.main()