import numpy as np
import os
import math
import matplotlib.pyplot as plt

from input import read_from_keyboard, read_from_file, generate_function_data


def divided_differences(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def newton_interpolation(x, y, x_val):
    coef = divided_differences(x, y)
    n = len(x) - 1
    result = coef[n]
    for k in range(1, n+1):
        result = coef[n-k] + (x_val - x[n-k]) * result
    return result

def lagrange_interpolation(x, y, x_val):
    result = 0.0
    n = len(x)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result

def finite_differences(y):
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:,0] = y
    for j in range(1, n):
        for i in range(n-j):
            delta_y[i,j] = delta_y[i+1,j-1] - delta_y[i,j-1]
    return delta_y

def gauss_interpolation(x, y, x_val):
    n = len(x)
    h = x[1] - x[0]  # Assuming uniform spacing

    # Find the position of x_val in the x array
    mid = n // 2
    if x_val >= x[mid]:
        # Forward interpolation
        q = (x_val - x[mid]) / h
        start = mid
    else:
        # Backward interpolation
        q = (x_val - x[mid]) / h
        start = mid
    # print(q)
    # print(y[start])
    delta_y = finite_differences(y)
    result = y[start]

    temp_q = 1
    fact = 1

    if x_val >= x[mid]:  # Forward interpolation
        # print('forward')
        for i in range(1, n):
            # print(fact)
            if i % 2 != 0:
                temp_q *= (q + (i // 2))
                t = (temp_q * delta_y[start - (i // 2), i]) / fact
                result += t
                # print('delta', delta_y[start - (i // 2) , i])
            else:
                temp_q *= (q - (i // 2))
                t = (temp_q * delta_y[start - (i // 2)  - i % 2, i]) / fact
                # print('delta', delta_y[start - (i // 2) - i % 2, i])
                result += t
            fact *= (i + 1)
    else:  # Backward interpolation
        # print('backward')
        for i in range(1, n):
            if i % 2 != 0:
                temp_q *= (q - (i // 2))
                result += (temp_q * delta_y[start - (i // 2)  - i % 2, i]) / fact
                # print('delta', delta_y[start - (i // 2)  - i % 2, i])
                
            else:
                temp_q *= (q + (i // 2))
                result += (temp_q * delta_y[start - (i // 2), i]) / fact
                # print('delta', delta_y[start - (i // 2), i])
                
            fact *= (i + 1)
    return result

def plot_graphs(x, y, interpolated_points, methods, x_val, interpolated_values):
    plt.figure(figsize=(12, 8))
    x_plot = np.linspace(min(x), max(x), 500)
    plt.plot(x, y, 'o', label='Nodes')

    for method, y_interp in interpolated_points.items():
        plt.plot(x_plot, y_interp(x_plot), label=method)
        plt.plot(x_val, interpolated_values[method], 'o', label=f'{method} Interpolated Point')

    plt.legend()
    plt.title('Interpolation Methods')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def finite_differences_table(y):
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:,0] = y
    for j in range(1, n):
        for i in range(n-j):
            delta_y[i,j] = delta_y[i+1,j-1] - delta_y[i,j-1]
    return delta_y

def print_finite_differences_table(delta_y):
    n = delta_y.shape[0]
    print("Таблица конечных разностей:")
    for i in range(n):
        row = [f"{delta_y[i, j]:.4f}" if i + j < n else "" for j in range(n)]
        print("\t".join(row))

def stirling_interpolation(x, y, x_val):
    n = len(x)
    h = x[1] - x[0]  # Assuming uniform spacing
    mid = n // 2
    delta_y = finite_differences(y)
    q = (x_val - x[mid]) / h

    result = y[mid]
    temp_q = q
    fact = 1
    for i in range(1, n):
        if i % 2 != 0:
            result += temp_q * (delta_y[mid - i//2, i] + delta_y[mid - (i//2) - 1, i]) / 2
            temp_q *= (q**2 - (i//2)**2)
        else:
            result += temp_q * delta_y[mid - i//2, i] / fact
            temp_q *= (q**2 - (i//2)**2)
        fact *= i
    return result

def bessel_interpolation(x, y, x_val):
    n = len(x)
    h = x[1] - x[0]  # Assuming uniform spacing
    mid = n // 2
    delta_y = finite_differences(y)
    q = (x_val - (x[mid] + x[mid - 1]) / 2) / h

    result = (y[mid] + y[mid - 1]) / 2
    temp_q = q
    fact = 1
    for i in range(1, n):
        if i % 2 != 0:
            result += temp_q * (delta_y[mid - i//2, i] + delta_y[mid - (i//2) - 1, i]) / 2
            temp_q *= (q**2 - (i//2)**2)
        else:
            result += temp_q * delta_y[mid - i//2, i] / fact
            temp_q *= (q**2 - (i//2)**2)
        fact *= i
    return result

        
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

        # Form and print the finite differences table
        delta_y = finite_differences_table(y)
        print_finite_differences_table(delta_y)
      
        # Interpolation methods
        methods = {
            "Lagrange": lagrange_interpolation,
            "Newton Divided": newton_interpolation,
            "Gauss": gauss_interpolation,
            # "Stirling": stirling_interpolation,
            # "Bessel": bessel_interpolation
        }

        interpolated_values = {}
        for method_name, method in methods.items():
            interpolated_values[method_name] = method(x, y, x_val)
            print(f"{method_name} interpolation at x = {x_val}: {interpolated_values[method_name]}")
        # 1/0
        # Plotting the results
        interpolated_points = {
            "Lagrange": lambda x_plot: [lagrange_interpolation(x, y, x_i) for x_i in x_plot],
            "Newton Divided": lambda x_plot: [newton_interpolation(x, y, x_i) for x_i in x_plot],
            "Gauss": lambda x_plot: [gauss_interpolation(x, y, x_i) for x_i in x_plot],
            # "Stirling": lambda x_plot: [stirling_interpolation(x, y, x_i) for x_i in x_plot],
            # "Bessel": lambda x_plot: [bessel_interpolation(x, y, x_i) for x_i in x_plot]
        }

        plot_graphs(x, y, interpolated_points, methods, x_val, interpolated_values)

        break


if __name__ == "__main__":
    main()
