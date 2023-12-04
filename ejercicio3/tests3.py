import unittest
import jumps

class TestStringMethods(unittest.TestCase):

    def test_palin(self):
        self.assertTrue(jumps.verifier("anilina"))
        self.assertTrue(jumps.verifier("Ana"))
        self.assertFalse(jumps.verifier("anná"))
        self.assertFalse(jumps.verifier("pYtHon"))

if __name__ == '__main__':
    unittest.main()