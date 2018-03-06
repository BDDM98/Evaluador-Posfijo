#coding:utf-8
import operator

class Calculator(object):
    def parse(self, expression):
        values = expression.split()
        return self.compute_values(values)

    def compute_values(self, values):
        operations = { "+" : operator.add,
                      "-" : operator.sub,
                      "*" : operator.mul,
                      "/" : operator.div }

        if len(values) == 1:
            return values[0]
        if values[0] in operations:
            if values[1] in operations:
                return BinaryExpression(operations[values[0]], self.compute_values(values[1:-1]), values[-1]).compute()
            return BinaryExpression(operations[values[0]], values[1], values[2]).compute()

        return BinaryExpression(values[0], values[1], values[2]).compute()


class BinaryExpression(object):
    def __init__(self, operations, left_expression, right_expression):
        self.operations = operations
        self.left_expression = int(left_expression)
        self.right_expression = int(right_expression)

    def compute(self):
        return self.operations(self.left_expression, self.right_expression)
###############

#coding:utf-8
import unittest
from calculator import Calculator

class TestCalculadora(unittest.TestCase):
    def test_add_three_four(self):
        self.aider(7, "+ 3 4")

    def test_add_nine_two(self):
        self.aider(11, "+ 9 2")

    def test_add_twenty_two(self):
        self.aider(22, "+ 20 2")

    def test_substract_four_three(self):
        self.aider(1, "- 4 3")

    def test_substract_four_minus_three(self):
        self.aider(100, "- 99 -1")

    def test_multiply_four_three(self):
        self.aider(12, "* 4 3")

    def test_multiply_minus_four_thirtytwo(self):
        self.aider(-128, "* -4 32")

    def test_divide_four_three(self):
        self.aider(1, "/ 4 3")

    def test_divide_twelve_three(self):
        self.aider(4, "/ 12 3")

    def test_divide_minus_twelve_three(self):
        self.aider(-4, "/ -12 3")

    def test_add_add_four_three_four(self):
        self.aider(11, "+ + 4 3 4")

    def test_add_substract_four_three_four(self):
        self.aider(5, "+ - 4 3 4")

    def test_divide_multiply_three_four_four(self):
        self.aider(3, "/ * 3 4 4")

    def test_divide_add_four_four_four(self):
        self.aider(2, "/ + 4 4 4")

    def test_add_add_add_four_three_four_three(self):
        self.aider(14, "+ + + 4 3 4 3")

    def test_add_substract_substract_four_three_four_three(self):
        self.aider(0, "+ - - 4 3 4 3")

    def test_divide_multiply_multiply_two_two_two_eight(self):
        self.aider(1, "/ * * 2 2 2 8")

    def test_add_add_add_add_four_three_four_three_four(self):
        self.aider(18, "+ + + + 4 3 4 3 4")

    def test_divide_multiply_multiply_multiply_two_two_two_two_sixteen(self):
        self.aider(1, "/ * * * 2 2 2 2 16")

    def test_add_add_three_four_substract_four_three(self):
        self.aider(8, "+ + 3 4 - 4 3")

    def aider(self, expected, expression):
        calc = Calculator()
        actual = calc.parse(expression)
        self.assertEqual(expected, actual)

def run_tests():
    """Método para iniciar la sesión de testeo"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)
    unittest.TextTestRunner(verbosity=2).run(suite)

#corremos los tests sólo si fuimos llamados desde la consola
if __name__ == "__main__":
    run_tests()
