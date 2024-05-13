import numpy as np
import os
import math

from inter import (
    bessel,
    central_differences,
    lagrange_polynomial,
    newton_divided_difference,
    newton_polynomial,
    plot_interpolation,
    stirling,
)
from input import read_from_keyboard, read_from_file, generate_function_data


def main():
    while True:
        print("\nВыберите способ ввода данных:")
        print("1 - Ввод с клавиатуры")
        print("2 - Чтение из файла")
        print("3 - Генерация данных функции")
        print("0 - Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            x, y = read_from_keyboard()
        elif choice == "2":
            x, y = read_from_file()
        elif choice == "3":
            x, y = generate_function_data()
        elif choice == "0":
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")
            continue
        print()
        print("x:", x)
        print("y:", y)

        x_val = float(input("Введите значение аргумента для интерполяции: "))

        h = (x[-1] - x[0]) / (len(x) - 1)  # Расчет шага между точками

        # Вычисление таблицы центральных разностей
        difference_table = central_differences(y)

        # Лагранж
        y_lagrange = lagrange_polynomial(x, y, x_val)
        print(f"Лагранж: y({x_val}) = {y_lagrange}")

        # Ньютон
        newton_coeffs = newton_divided_difference(x, y)
        y_newton = newton_polynomial(x, y, x_val, newton_coeffs)
        print(f"Ньютон: y({x_val}) = {y_newton}")

        # Стирлинг
        y_stirling = stirling(difference_table, len(x), x, x_val, h)
        print(f"Стирлинг: y({x_val}) = {y_stirling}")

        # Бессель
        y_bessel = bessel(difference_table, len(x), x, x_val, h)
        print(f"Бессель: y({x_val}) = {y_bessel}")
        # Построение графиков
        plot_interpolation(
            x,
            y,
            [
                lambda xv: lagrange_polynomial(x, y, xv),
                lambda xv: newton_polynomial(x, y, xv, newton_coeffs),
                lambda xv: stirling(difference_table, len(x), x, xv, h),
                lambda xv: bessel(difference_table, len(x), x, xv, h),
            ],
            "Интерполяция: Лагранж, Ньютон, Стирлинг, Бессель",
            x_val,
            y_lagrange,
            y_newton,
            y_stirling,
            y_bessel,
        )

        break


if __name__ == "__main__":
    main()
