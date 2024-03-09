import unittest
import numpy as np
from main import left_rectangles, middle_rectangles, right_rectangles, simpson_rule, trapezoid_rule


class TestNumericalIntegrationMethods(unittest.TestCase):
    def test_left_rectangles(self):
        self.assertAlmostEqual(left_rectangles(
            lambda x: x**2, 0, 1, 400), 1/3, places=2)

    def test_right_rectangles(self):
        self.assertAlmostEqual(right_rectangles(
            lambda x: x**2, 0, 1, 400), 1/3, places=2)

    def test_middle_rectangles(self):
        self.assertAlmostEqual(middle_rectangles(
            lambda x: x**2, 0, 1, 400), 1/3, places=2)

    def test_trapezoid_rule(self):
        self.assertAlmostEqual(trapezoid_rule(
            lambda x: x**2, 0, 1, 400), 1/3, places=2)

    def test_simpson_rule(self):
        self.assertAlmostEqual(simpson_rule(
            lambda x: x**2, 0, 1, 400), 1/3, places=2)

    def test_exponential_function(self):
        # Тестирование интегрирования e^x на интервале от 0 до 1
        self.assertAlmostEqual(left_rectangles(
            lambda x: np.exp(x), 0, 1, 400), np.exp(1) - 1, places=2)
        self.assertAlmostEqual(right_rectangles(
            lambda x: np.exp(x), 0, 1, 400), np.exp(1) - 1, places=2)
        self.assertAlmostEqual(middle_rectangles(
            lambda x: np.exp(x), 0, 1, 400), np.exp(1) - 1, places=2)
        self.assertAlmostEqual(trapezoid_rule(
            lambda x: np.exp(x), 0, 1, 400), np.exp(1) - 1, places=2)
        self.assertAlmostEqual(simpson_rule(
            lambda x: np.exp(x), 0, 1, 400), np.exp(1) - 1, places=2)

    def test_sine_function(self):
        # Тестирование интегрирования sin(x) на интервале от 0 до pi
        self.assertAlmostEqual(left_rectangles(
            np.sin, 0, np.pi, 400), 2, places=2)
        self.assertAlmostEqual(right_rectangles(
            np.sin, 0, np.pi, 400), 2, places=2)
        self.assertAlmostEqual(middle_rectangles(
            np.sin, 0, np.pi, 400), 2, places=2)
        self.assertAlmostEqual(trapezoid_rule(
            np.sin, 0, np.pi, 400), 2, places=2)
        self.assertAlmostEqual(simpson_rule(
            np.sin, 0, np.pi, 400), 2, places=2)

    def test_polynomial_function(self):
        # Тестирование интегрирования x^3 + x^2 на интервале от 0 до 1
        self.assertAlmostEqual(left_rectangles(
            lambda x: x**3 + x**2, 0, 1, 400), 0.25 + 1/3, places=2)
        self.assertAlmostEqual(right_rectangles(
            lambda x: x**3 + x**2, 0, 1, 400), 0.25 + 1/3, places=2)
        self.assertAlmostEqual(middle_rectangles(
            lambda x: x**3 + x**2, 0, 1, 400), 0.25 + 1/3, places=2)
        self.assertAlmostEqual(trapezoid_rule(
            lambda x: x**3 + x**2, 0, 1, 400), 0.25 + 1/3, places=2)
        self.assertAlmostEqual(simpson_rule(
            lambda x: x**3 + x**2, 0, 1, 400), 0.25 + 1/3, places=2)


if __name__ == '__main__':
    unittest.main()
