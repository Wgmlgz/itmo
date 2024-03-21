def left_rectangles(func, a, b, n):
    h = (b - a) / n
    integral = sum(func(a + i * h) for i in range(n)) * h
    return integral


def right_rectangles(func, a, b, n):
    h = (b - a) / n
    integral = sum(func(a + (i + 1) * h) for i in range(n)) * h
    return integral


def middle_rectangles(func, a, b, n):
    h = (b - a) / n
    integral = sum(func(a + (i + 0.5) * h) for i in range(n)) * h
    return integral


def trapezoid_rule(func, a, b, n):
    h = (b - a) / n
    result = (func(a) + func(b)) / 2
    for i in range(1, n):
        result += func(a + i * h)
    result *= h
    return result


def simpson_rule(func, a, b, n):
    if n % 2 == 1:
        n += 1  # Adjust n to be even if it's odd
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)
    for i in range(2, n - 1, 2):
        result += 2 * func(a + i * h)
    result *= h / 3
    return result


def calculate_integral(func, a, b, n, method):
    if method == 'left':
        return left_rectangles(func, a, b, n)
    elif method == 'right':
        return right_rectangles(func, a, b, n)
    elif method == 'middle':
        return middle_rectangles(func, a, b, n)
    elif method == 'trapezoid':
        return trapezoid_rule(func, a, b, n)
    elif method == 'simpson':
        return simpson_rule(func, a, b, n)
    else:
        raise ValueError("Unknown method")


def runge_rule(func, a, b, n, method, accuracy):
    integral_n = calculate_integral(func, a, b, n, method)
    integral_2n = calculate_integral(func, a, b, 2 * n, method)
    
    while abs(integral_n - integral_2n) > accuracy and n < 1000000:
        n *= 2
        integral_n = integral_2n
        integral_2n = calculate_integral(func, a, b, 2 * n, method)
    return integral_2n, n


def input_params(functions, function_descriptions):
    print("Выберите функцию для интегрирования:")

    for i, description in enumerate(function_descriptions, start=1):
        print(f"{i}. f{i}(x) = {description}")

    choice = 0
    while True:
        choice = int(input()) - 1
        if 0 <= choice < len(functions):
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до", len(functions))

    print(
        f"Выбрана функция: f{choice + 1}(x) = {function_descriptions[choice]}")

    while True:
        a = float(input("Введите нижний предел интегрирования: "))
        b = float(input("Введите верхний предел интегрирования: "))
        if a < b:
            break
        else:
            print(
                "Нижний предел должен быть меньше верхнего. Пожалуйста, введите значения заново.")

    while True:
        accuracy = float(input("Введите требуемую точность: "))
        if accuracy > 0:
            break
        else:
            print("Точность должна быть больше 0. Пожалуйста, введите значение заново.")

    n = 4

    print("Выберите метод интегрирования:\n1. Левые прямоугольники\n2. Правые прямоугольники\n3. Средние прямоугольники\n4. Трапеции\n5. Симпсон")

    while True:
        method_input = int(input())
        if 1 <= method_input <= 5:
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 5.")

    methods = ['left', 'right', 'middle', 'trapezoid', 'simpson']
    method = methods[method_input - 1]
    return choice, a, b, n, method, accuracy
