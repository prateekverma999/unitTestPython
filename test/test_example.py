import unittest
# import sys
# import os
# # Add the src directory to the sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# export PYTHONPATH=$PYTHONPATH:/workspaces/unitTestPython/src

from src import example

class TestExample(unittest.TestCase):

    @unittest.expectedFailure
    def test_addition(self):
        
        with self.subTest("integer_test"):
            self.assertEqual(example.addtion(10, 20),"30")
            
        with self.subTest("string_test"):
            self.assertEqual(example.addtion("10",20),30)

    @unittest.skip("sking for testing ...")
    def test_alcohol(self):

        with self.subTest("age_geq_16"):
            self.assertTrue(example.alcohol(16))

        with self.subTest("age_less_16"):
            self.assertFalse(example.alcohol(15))

if __name__ == "__main__":
    unittest.main()