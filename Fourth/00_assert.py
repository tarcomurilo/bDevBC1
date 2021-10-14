import unittest

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 5, "Need to be six")
       

if __name__ == "__main__":
    unittest.main()