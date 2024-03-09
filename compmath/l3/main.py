import numpy as np

from utils import input_params, runge_rule


functions = [lambda x: x ** 2, lambda x: np.sin(x), lambda x: np.exp(x), lambda x: 1 / (1 + x ** 2), lambda x: np.log(x + 1)]


def main():
    choice, a, b, n, method, accuracy = input_params(functions, [
        "x^2",
        "sin(x)",
        "e^x",
        "1 / (1 + x^2)",
        "ln(x + 1)"
    ])
    result, final_n = runge_rule(functions[choice], a, b, n, method, accuracy)
    print(f"Значение интеграла: {result}\nЧисло разбиений: {final_n}")


if __name__ == "__main__":
    main()
