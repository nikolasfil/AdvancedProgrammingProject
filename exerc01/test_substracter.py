import unittest
from subtracter import sub


class TestClass(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(sub(2,1),"POSITIVE")

    def test_positive2(self):
        self.assertEqual(sub(1,-2),"POSITIVE")


    def test_negative(self):
        self.assertEqual(sub(1,2),"NEGATIVE")

    def test_negative2(self):
        self.assertEqual(sub(-2,-1),"NEGATIVE")

    
    def test_a_nonnumber(self):
        with self.assertRaises(TypeError):
            sub("a",1)

    def test_b_nonnumber(self):
        with self.assertRaises(TypeError):
            sub(1,"b")
            


if __name__ == "__main__":
    unittest.main()