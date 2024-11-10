import unittest
from math_quiz import number,math_operator,problem_answer

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 20
        for _ in range(1000):  # Test a large number of random values
            rand_num = number(min_val, max_val) # generate random numbers between 1-20
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the generated operator is one of '+', '-', '*'
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = math_operator() # generates random operators
            self.assertIn(rand_operator, operators)

    def test_function_C(self):
        test_cases = [
            (5, 2, '+','5 + 2',7),
            (10, 3, '*', '10 * 3',30),
            (10,5,'-',"10-5",5),
            (2,3,"*","2*3",6),
            (8,1,"+","8+1",9)
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem,result = problem_answer(num1, num2, operator)
            self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()

