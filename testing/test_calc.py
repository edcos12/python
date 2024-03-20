import unittest 
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_calculator_class_exists(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_add_method_accepts_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0,0), 0)

    def test_add_method_with_non_numeric_input(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: Inputs must be numeric"):
            calc.add("a", 5)
    
    def test_add_method_returns_numeric(self):
        calc = Calculator()
        self.assertIsInstance(calc.add(1, 2), (int, float))

    def test_add_method_performs_correct_calculation(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(100, 200), 300)

    def test_minus_method_performs_correct_cslculation(self):
        calc = Calculator()
        self.assertEqual(calc.minus(7, 3), 4)
        self.assertEqual(calc.minus(-3, -6), 3)
        self.assertEqual(calc.minus(0, 0), 0)
        self.assertEqual(calc.minus(1300, 900), 400)

    def test_multiply_method_performs_correct_cslculation(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(9, 3), 27)
        self.assertEqual(calc.multiply(-5, 3), -15)
        self.assertEqual(calc.multiply(16, 0), 0)
        self.assertEqual(calc.multiply(100, 600), 60000)

    def test_divide_method_performs_correct_cslculation(self):
        calc = Calculator()
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(0, 0), "cant divide by 0")
        self.assertEqual(calc.divide(-10, 2), -5)
        self.assertEqual(calc.divide(1000, 40), 25)


    @unittest.skip("skipping...")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "skippped...")
    def test_if_skip(self):
        pass



if __name__=='__main__':
    unittest.main()