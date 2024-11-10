import unittest
from math_quiz import get_random_integer, get_random_operator, calculate_problem

class TestMathQuizFunctions(unittest.TestCase):

    def test_get_random_integer(self):
        """Test if get_random_integer returns an integer within the specified range ."""
        min_value = 1
        max_value = 10
        for _ in range(100):
            result = get_random_integer(min_value, max_value)
            self.assertTrue(min_value <= result <= max_value, 
                            f"Result {result} is not within the range {min_value}-{max_value}")

    def test_get_random_operator(self):
        """Test if get_random_operator returns one of the valid operators ."""
        valid_operators = ['+', '-', '*']
        for _ in range(100):
            operator = get_random_operator()
            self.assertIn(operator, valid_operators, 
                          f"Operator {operator} is not in the list of valid operators {valid_operators}")

    def test_calculate_problem(self):
        """Test if calculate_problem correctly computes the answer based on the operator."""
        # Test addition
        problem, answer = calculate_problem(3, 2, '+')
        self.assertEqual(answer, 5, f"Expected 5, got {answer} for addition")
        
        # Test subtraction
        problem, answer = calculate_problem(3, 2, '-')
        self.assertEqual(answer, 1, f"Expected 1, got {answer} for subtraction")
        
        # Test multiplication
        problem, answer = calculate_problem(3, 2, '*')
        self.assertEqual(answer, 6, f"Expected 6, got {answer} for multiplication")

if __name__ == "__main__":
    unittest.main()
