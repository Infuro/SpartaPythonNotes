from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_sub(self):
        self.assertEqual(self.calc.sub(4, 2), 2)

    def test_mult(self):
        self.assertEqual(self.calc.mult(2, 2), 4)
        self.assertEqual(self.calc.mult(3, 5), 15)
#this needs to be run in terminal