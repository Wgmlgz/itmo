from typing import Callable
import numpy as np
from math import inf, log, exp, sqrt
from utils import input_params, runge_rule, simpson_rule


functions = [
    # ((lambda x: log(x + 1)), [-1], (-1, inf)),
    ((lambda x: 1 / x), [0], (-inf, inf)),
    ((lambda x: 1 / sqrt(1 - x ** 2)), [-1, 1], (-1, 1)),
    # ((lambda x: ex/p(1 / x)), [0], (-inf, inf)),
]


def check_divergent(f_data, x, eps, sign=1):
    # print()
    # print()
    n = round(1 / eps)
    # print(n)
    new_eps = eps
    last = 0
    for i in range(20):
        new_eps = new_eps / 2
        a = x + new_eps * sign
        b = x + eps * sign
        try:
            f_data[0](a)
        except:
            break
        interval = [a, b]
        interval.sort()
        t = simpson_rule(f_data[0], interval[0], interval[1], n)
        print('check', t)
        if abs(last - t) > n:
            raise ValueError('Ошибка, интеграл расходится')
        last = t
    return last
        # eps = eps / 2


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

    fin = []

    for a, b in intervals:
        n_a = a
        n_b = b
        t = 0
        if a in break_points:
            n_a += eps
            t += check_divergent(f_data, a, eps, 1)
        if b in break_points:
            n_b -= eps
            t += check_divergent(f_data, b, eps, -1)
        # print(t)
        fin.append([n_a, n_b, t])

    return fin


def calc(f_data, a, b, n, method, accuracy):
    intervals = calc_intervals(f_data, a, b, accuracy)
    result, final_n = 0, 0
    for a, b, tt in intervals:
        t, t_n = runge_rule(f_data[0], a, b, n, method, accuracy)
        result += t
        result += tt
        final_n += t_n
    return result, final_n


def main():
    try:
        choice, a, b, n, method, accuracy = input_params(functions, [
            "1 / x",
            "1 / (1-x^2)^0.5",
        ])

        result, final_n = calc(functions[choice], a, b, n, method, accuracy)
        print(f"Значение интеграла: {result}\nЧисло разбиений: {final_n}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
