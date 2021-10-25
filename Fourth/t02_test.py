#Create a unit testing to extensively 
# test all possibilities of the function created in the regex exercise above.

import unittest
import os

os.chdir('.\\Fourth\\')

from t01_regex import searchRegex

class testRegex(unittest.TestCase):
    
    def testRegx0(self):
        self.assertEqual(searchRegex('a_a'), ["a_a"], 'Need to match')
        self.assertTrue(searchRegex('a_a'), 'Need to match')
        self.assertEqual(searchRegex('abc_def'), ["abc_def"], 'Need to match')
        self.assertEqual(searchRegex('Abc_dEf'), ['bc_d'], 'Need to match')
        self.assertEqual(searchRegex('Abc_dEf_j_k_l'), ['bc_d', 'f_j', 'k_l'], 'Need to match')

    def testRegx1(self):
        self.assertListEqual(searchRegex('A_b'), [], 'Need to be nothing')
        self.assertCountEqual(searchRegex('a_Bgj_gj'), ['gj_gj'], 'Need to be nothing')
        self.assertFalse(searchRegex('3_a'), 'Need to be nothing')
        self.assertEqual(searchRegex('3_B'), [], 'Need to be nothing')
        self.assertIsNot(searchRegex('a_a'), ['a_a'], 'Need to be nothing')
        self.assertEqual(searchRegex('B_3'), [], 'Need to be nothing')

if __name__ == '__main__':
    unittest.main()
