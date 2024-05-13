import numpy as np
import matplotlib.pyplot as plt


def lagrange_polynomial(x, y, x_val):
    """Вычисление значения многочлена Лагранжа в точке x_val."""
    total = 0
    n = len(x)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (x_val - x[j]) / (x[i] - x[j])
        total += term
    return total


def newton_divided_difference(x, y):
    """Построение таблицы разделенных разностей для многочлена Ньютона."""
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef[0, :]


def newton_polynomial(x, y, x_val, coef):
    """Вычисление значения многочлена Ньютона в точке x_val."""
    n = len(x)
    total = coef[0]
    product = 1
    for i in range(1, n):
        product *= x_val - x[i - 1]
        total += coef[i] * product
    return total


def plot_interpolation(x, y, interp_funcs, title, x_val, y_lagrange, y_newton, y_stirling, y_bessel):
    """Отображение графика исходной функции и интерполяционных полиномов."""
    plt.figure()
    plt.scatter(x, y, color="red", label="Data Points")
    x_vals = np.linspace(min(x), max(x), 100)
    colors = ['blue', 'green', 'orange', 'purple']  # Дополненный список цветов
    labels = ['Лагранж', 'Ньютон', 'Стирлинг', 'Бессель']  # Дополненный список меток

    for i, interp_func in enumerate(interp_funcs):
        y_vals = [interp_func(x_val) for x_val in x_vals]
        plt.plot(
            x_vals,
            y_vals,
            label=f"Interpolation Polynomial - {labels[i]}",
            color=colors[i],
        )

    # Добавляем интерполируемую точку
    plt.scatter(
        [x_val],
        [y_lagrange],
        color="black",
        label=f"Interpolated Point - Lagrange (x={x_val}, y={y_lagrange:.2f})",
    )
    plt.scatter(
        [x_val],
        [y_newton],
        color="purple",
        label=f"Interpolated Point - Newton (x={x_val}, y={y_newton:.2f})",
        marker="x",
    )
    
    plt.scatter(
        [x_val],
        [y_lagrange],
        color="black",
        label=f"Interpolated Point - Stirling (x={x_val}, y={y_stirling:.2f})",
    )
    plt.scatter(
        [x_val],
        [y_newton],
        color="purple",
        label=f"Interpolated Point - Bessel (x={x_val}, y={y_bessel:.2f})",
        marker="x",
    )


    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def central_differences(y):
    n = len(y)
    if n < 2:  # Проверяем, достаточно ли элементов для вычисления разностей
        return None  # или можно возвращать исходный массив y, зависит от задачи
    
    table = np.zeros((n, n))
    table[:, 0] = y
    for j in range(1, n):
        for i in range(1, n-j):  # Убедимся, что i и i+1 для i-1 не выходят за пределы
            table[i][j] = table[i+1][j-1] - table[i-1][j-1]
    return table



def stirling(table, n, x, x_val, h):
    mid = n // 2
    u = (x_val - x[mid]) / h
    fx = table[mid][0]
    delta_1 = (table[mid][1] + table[mid - 1][1]) / 2
    delta_2 = table[mid][2]
    delta_3 = (table[mid + 1][1] - table[mid - 2][1]) / 2
    delta_4 = table[mid - 1][2] + table[mid][2]

    # Applying the Stirling's formula
    fx += u * delta_1
    fx += ((u**2 - 1) / 2) * delta_2
    fx += ((u**3 - 3 * u) / 6) * delta_3
    fx += ((u**4 - 6 * u**2 + 3) / 24) * delta_4

    return fx


def bessel(table, n, x, x_val, h):
    mid = n // 2
    u = (x_val - x[mid]) / h
    fx = (table[mid][0] + table[mid + 1][0]) / 2
    delta_1 = (table[mid][1] + table[mid + 1][1]) / 2
    delta_2 = (table[mid][2] + table[mid + 1][2]) / 2
    delta_3 = (table[mid + 1][1] - table[mid][1]) / 2
    delta_4 = table[mid + 1][2] + table[mid][2]

    # Applying the Bessel's formula
    fx += u * delta_1
    fx += (u**2 - 1 / 4) * delta_2
    fx += ((u**3 - 3 * u / 2) / 3) * delta_3
    fx += ((u**4 - u**2 + 3 / 16) / 24) * delta_4

    return fx
