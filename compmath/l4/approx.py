import numpy as np


class Approximation:
    def __init__(self, x, y, p0):
        self.x = x
        self.y = y
        self.p0 = p0
        self.params = None
        self.rms = None
        self.fitted_values = None

    def prepare(self):
        self.x = self.x
        self.y = self.y
        self.y_transformed = self.y
        self.x_transformed = self.x

    def post_process(self):
        self.fitted_values = self.function(self.x, *self.params)
        self.e = self.y - self.fitted_values
        self.rms = np.sqrt(np.mean(self.e ** 2))

    def fit(self):
        pass

    def to_json(self):
        return {
            'params': self.params.tolist(),
            'x_i': self.x.tolist(),
            'y_i': self.y.tolist(),
            'f_i': self.fitted_values.tolist(),
            'e_i': self.e.tolist(),
            'rms': self.rms,
        }

    def function(self, x):
        raise NotImplementedError("Subclasses should implement this method")


def least_squares(A, b):
    # Solve the system using a stable method like SVD
    u, s, vt = np.linalg.svd(A.T @ A)
    return vt.T @ np.diag(1 / s) @ u.T @ A.T @ b


class LinearApproximation(Approximation):
    name = 'Линейная'

    def function(self, x, a, b):
        return a * x + b

    def fit(self):
        A = np.vstack([self.x, np.ones(len(self.x))]).T
        self.params = least_squares(A, self.y)


class QuadraticApproximation(Approximation):
    name = "Квадратичная"

    def function(self, x, a, b, c):
        return a * x**2 + b * x + c

    def fit(self):
        A = np.vstack([self.x**2, self.x, np.ones(len(self.x))]).T
        self.params = least_squares(A, self.y)


class CubicApproximation(Approximation):
    name = "Кубическая"

    def function(self, x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    def fit(self):
        A = np.vstack([self.x**3, self.x**2, self.x, np.ones(len(self.x))]).T
        self.params = least_squares(A, self.y)


class ExponentialApproximation(Approximation):
    name = "Экспоненциальная"

    def function(self, x, a, b):
        return a * np.exp(b * x)

    def prepare(self):
        positive_indices = self.y > 0
        self.x = self.x[positive_indices]
        self.y = self.y[positive_indices]
        self.y_transformed = np.log(self.y)
        self.x_transformed = self.x

    def fit(self):
        A = np.vstack([self.x_transformed, np.ones(len(self.x_transformed))]).T
        params = least_squares(A, self.y_transformed)

        a = np.exp(params[1])
        b = params[0]
        self.params = np.array([a, b])


class LogarithmicApproximation(Approximation):
    name = "Логарифмическая"

    def function(self, x, a, b):
        return a * np.log(x) + b

    def prepare(self):
        positive_indices = self.x > 0
        self.x = self.x[positive_indices]
        self.y = self.y[positive_indices]
        self.x_transformed = np.log(self.x)
        self.y_transformed = self.y

    def fit(self):
        A = np.vstack([self.x_transformed, np.ones(len(self.x_transformed))]).T
        self.params = least_squares(A, self.y_transformed)


class PowerApproximation(Approximation):
    name = "Степенная"

    def function(self, x, a, b):
        return a * x**b

    def prepare(self):
        positive_indices = (self.x > 0) & (self.y > 0)
        self.x = self.x[positive_indices]
        self.y = self.y[positive_indices]
        self.y_transformed = np.log(self.y)
        self.x_transformed = np.log(self.x)

    def fit(self):
        A = np.vstack([self.x_transformed, np.ones(len(self.x_transformed))]).T
        params = least_squares(A, self.y_transformed)

        a = np.exp(params[1])
        b = params[0]
        self.params = np.array([a, b])
