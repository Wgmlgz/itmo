from typing import Callable
import numpy as np
from math import inf
from utils import input_params, runge_rule


functions = [
    ((lambda x: np.log(x + 1)), [-1], (-1, inf)),
    ((lambda x: 1 / x), [0], (-inf, inf)),
    ((lambda x: np.exp(1 / x)), [0], (-inf, inf)),
]


def calc_intervals(f_data: tuple[Callable[[float], float], list[float]], a, b, eps):
    f, break_points, defined = f_data
    min_a, max_b = defined

    if a < min_a or b > max_b:
        raise Exception('Интеграл не существует')

    points = [a, b]
    for point in break_points:
        if point >= a and point <= b:
            points.append(point)

    points = sorted(set(points))

    intervals = [(points[i], points[i + 1]) for i in range(len(points) - 1)]
    intervals = [(
        a + eps if a in break_points else a,
        b - eps if b in break_points else b
    ) for a, b in intervals]

    return intervals


def calc(f_data, a, b, n, method, accuracy):
    intervals = calc_intervals(f_data, a, b, accuracy)
    result, final_n = 0, 0
    for a, b in intervals:
        t, t_n = runge_rule(f_data[0], a, b, n, method, accuracy)
        result += t
        final_n += t_n
    return result, final_n


def main():
    try:
      choice, a, b, n, method, accuracy = input_params(functions, [
          "ln(x + 1)",
          "1 / x",
          "e^(1/x)",
      ])

      result, final_n = calc(functions[choice], a, b, n, method, accuracy)
      print(f"Значение интеграла: {result}\nЧисло разбиений: {final_n}")
    except Exception as e:
      print(e)
      


if __name__ == "__main__":
    main()
