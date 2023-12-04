import unittest
import palin

class TestString(unittest.TestCase):

    def test_palin(self):
        self.assertTrue(palin.verifier("anilina"))
        self.assertTrue(palin.verifier("Ana"))
        self.assertFalse(palin.verifier("anná"))
        self.assertFalse(palin.verifier("pYtHon"))

if __name__ == '__main__':
    unittest.main()