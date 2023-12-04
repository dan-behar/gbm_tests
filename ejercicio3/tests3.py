import unittest
import jumps

class TestInts(unittest.TestCase):

    def test_jumps(self):
        self.assertAlmostEqual(jumps.jump(2),3)
        self.assertAlmostEqual(jumps.jump(5),4)
        self.assertAlmostEqual(jumps.jump(3),2)
        self.assertAlmostEqual(jumps.jump(1,-4),5)
        self.assertAlmostEqual(jumps.jump(2,-1),4)

if __name__ == '__main__':
    unittest.main()