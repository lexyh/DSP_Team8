# To be filled by students
import unittest
from text import TextColumn

# read in dummy data to use as a test source.
df = "text_test.csv"

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
    def colsetup(self):
    #assigning values to attributes
        self.col_name = "" 
        self.serie = {}

    
    def test_str_empty(self):
        # empty string value should return a false result
        empty_code = ''
        empty_response = check_valid_currency(empty_code)
        self.assertEqual(empty_response, False)

    def test_str_nonstrnum(self):
        # => To be filled by student
        # empty string value should return a false result
        num_code = 42
        num_response = check_valid_currency(num_code)
        self.assertEqual(num_response, False) 

    def test_str_nonstrlist(self):
        # => To be filled by student
        # empty string value should return a false result
        list_code = ['AUD',"USD"]
        list_response = check_valid_currency(list_code)
        self.assertEqual(list_response, False) 
        

    def test_str_emptylist(self):
        # => To be filled by student
        # empty string value should return a false result
        em_list_code = []
        em_list_response = check_valid_currency(em_list_code)
        self.assertEqual(em_list_response, False) 