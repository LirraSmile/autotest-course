import unittest #import unittest

#Create class TestAbs, which inherit from TestCase class
class TestAbs(unittest.TestCase):
    #transorm test functions into methods
    def test_abs1(self):
        #change Assert on self.assertEqual()
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()