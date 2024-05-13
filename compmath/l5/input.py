import numpy as np
import os
import math


def read_from_keyboard():
    x = []
    y = []
    while True:
        try:
            n = int(input("Введите количество точек: "))
            if n < 2:
                raise ValueError("Должно быть не менее двух точек.")
            break
        except ValueError as e:
            print("Ошибка:", e)
    for i in range(n):
        while True:
            try:
                xi = float(input(f"Введите x[{i}]: "))
                yi = float(input(f"Введите y[{i}]: "))
                x.append(xi)
                y.append(yi)
                break
            except ValueError:
                print("Ошибка: вводите числовые значения.")
    return np.array(x), np.array(y)


def read_from_file():
    while True:
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            try:
                data = np.loadtxt(filename, delimiter=",")
                x = data[:, 0]
                y = data[:, 1]
                return x, y
            except:
                print(
                    "Ошибка: файл должен содержать два столбца чисел, разделенных запятой."
                )
        else:
            print("Файл не найден, попробуйте еще раз.")


def generate_function_data():
    while True:
        func_str = input("Введите функцию (sin или cos): ").strip()
        if func_str in ["sin", "cos"]:
            func = np.sin if func_str == "sin" else np.cos
            break
        else:
            print("Ошибка: выберите 'sin' или 'cos'.")
    while True:
        try:
            a = float(input("Введите начальное значение интервала: "))
            b = float(input("Введите конечное значение интервала: "))
            n = int(input("Введите количество точек: "))
            if n < 2 or a >= b:
                raise ValueError
            break
        except ValueError:
            print("Ошибка: неверные значения интервала или количества точек.")
    x = np.linspace(a, b, n)
    y = func(x)
    return x, y
