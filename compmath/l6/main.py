import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy


class ODEMethods:
    def __init__(self, func, y0, t0, tn, h, exact_solution=None, epsilon=1e-6):
        self.func = func
        self.y0 = y0
        self.t0 = t0
        self.tn = tn
        self.h = h
        self.steps = int((tn - t0) / h)  + 1
        # self.h = (tn - t0) / self.steps
        print(self.h)
        self.exact_solution = exact_solution
        self.epsilon = epsilon

    def euler_improved(self):
        t = np.linspace(self.t0, self.tn, self.steps)
        y = np.zeros((self.steps, len(self.y0)))
        y[0] = self.y0
        step = 0
        
        ii = 0
        while step < self.steps - 1 and ii < 100000:
            ii += 1
            t_current = t[step]
            y_current = y[step]
            h_half = self.h / 2

            # One full step
            y_pred_full = y_current + self.h * self.func(t_current, y_current)
            y_full = y_current + self.h / 2 * (
                self.func(t_current, y_current)
                + self.func(t_current + self.h, y_pred_full)
            )

            # Two half steps
            t_half = t_current + h_half
            y_pred_half1 = y_current + h_half * self.func(t_current, y_current)
            y_half = y_current + h_half / 2 * (
                self.func(t_current, y_current) + self.func(t_half, y_pred_half1)
            )

            y_pred_half2 = y_half + h_half * self.func(t_half, y_half)
            y_half_final = y_half + h_half / 2 * (
                self.func(t_half, y_half) + self.func(t_current + self.h, y_pred_half2)
            )

            # Runge rule for error estimation
            error = np.abs(y_full - y_half_final)
            if np.max(error) < self.epsilon:
                step += 1
                t[step] = t_current + self.h
                y[step] = y_full
            else:
                self.h /= 2
                self.steps = int((self.tn - self.t0) / self.h) + 1
                t = np.linspace(self.t0, self.tn, self.steps)
                y = np.zeros((self.steps, len(self.y0)))
                y[0] = self.y0
                step = 0
        return t[: step + 1], y[: step + 1]

    def get_t(self):
        t = np.linspace(self.t0, self.tn, self.steps)
        return t

    def runge_kutta_4(self):
        t = np.linspace(self.t0, self.tn, self.steps)
        y = np.zeros((self.steps, len(self.y0)))
        y[0] = self.y0
        step = 0
        ii = 0
        
        while step < self.steps - 1 and ii < 100000:
            ii += 1
            
            t_current = t[step]
            y_current = y[step]
            h_half = self.h / 2

            # One full step
            k1_full = self.h * self.func(t_current, y_current)
            k2_full = self.h * self.func(
                t_current + self.h / 2, y_current + k1_full / 2
            )
            k3_full = self.h * self.func(
                t_current + self.h / 2, y_current + k2_full / 2
            )
            k4_full = self.h * self.func(t_current + self.h, y_current + k3_full)
            y_full = y_current + (k1_full + 2 * k2_full + 2 * k3_full + k4_full) / 6

            # Two half steps
            k1_half1 = h_half * self.func(t_current, y_current)
            k2_half1 = h_half * self.func(
                t_current + h_half / 2, y_current + k1_half1 / 2
            )
            k3_half1 = h_half * self.func(
                t_current + h_half / 2, y_current + k2_half1 / 2
            )
            k4_half1 = h_half * self.func(t_current + h_half, y_current + k3_half1)
            y_half1 = (
                y_current + (k1_half1 + 2 * k2_half1 + 2 * k3_half1 + k4_half1) / 6
            )

            k1_half2 = h_half * self.func(t_current + h_half, y_half1)
            k2_half2 = h_half * self.func(
                t_current + h_half + h_half / 2, y_half1 + k1_half2 / 2
            )
            k3_half2 = h_half * self.func(
                t_current + h_half + h_half / 2, y_half1 + k2_half2 / 2
            )
            k4_half2 = h_half * self.func(t_current + self.h, y_half1 + k3_half2)
            y_half2 = y_half1 + (k1_half2 + 2 * k2_half2 + 2 * k3_half2 + k4_half2) / 6

            # Runge rule for error estimation
            error = np.abs(y_full - y_half2)
            if np.max(error) < self.epsilon:
                step += 1
                t[step] = t_current + self.h
                y[step] = y_full
            else:
                self.h /= 2
                self.steps = int((self.tn - self.t0) / self.h) + 1
                t = np.linspace(self.t0, self.tn, self.steps)
                y = np.zeros((self.steps, len(self.y0)))
                y[0] = self.y0
                step = 0
        return t[: step + 1], y[: step + 1]

    def milne(self):
        t = self.get_t()
        y = np.zeros((self.steps, len(self.y0)))
        self.exact_solution = [[x] for x in self.get_exact_solution(t)]
        y[:4] = self.exact_solution[:4]

        for i in range(4, self.steps):
            y_pred = y[i - 4] + 4 * self.h / 3 * (
                2 * self.func(t[i - 3], y[i - 3])
                - self.func(t[i - 2], y[i - 2])
                + 2 * self.func(t[i - 1], y[i - 1])
            )

            f_pred = self.func(t[i], y_pred)
            ii = 0
            print('begin')
            while True and ii < 10000:
                ii += 1
                
                y_corr = y[i - 2] + self.h / 3 * (
                    self.func(t[i - 2], y[i - 2])
                    + 4 * self.func(t[i - 1], y[i - 1])
                    + f_pred
                )
                print(y_pred, y_corr)
                # if (y_pred > 1000 ):
                #     # y[i] =  None
                #     break
                error = np.abs(y_corr - y_pred)
                if np.max(error) < self.epsilon:
                    y[i] = y_corr
                    break
                else:
                    y_pred = y_corr
                    f_pred = self.func(t[i], y_pred)
            print('end')

        return t, y[: i + 1]

    def adams(self):
        t = self.get_t()
        y = np.zeros((self.steps, len(self.y0)))
        self.exact_solution = [[x] for x in self.get_exact_solution(t)]
        y[:4] = self.exact_solution[:4]
        
        
        for i in range(3, self.steps - 1):
            ii = 0
            while True and ii < 100000:
                ii += 1
                f_i = self.func(t[i], y[i])
                f_i_minus_1 = self.func(t[i - 1], y[i - 1])
                f_i_minus_2 = self.func(t[i - 2], y[i - 2])
                f_i_minus_3 = self.func(t[i - 3], y[i - 3])

                delta_f_i = f_i - f_i_minus_1
                delta_2_f_i = f_i - 2 * f_i_minus_1 + f_i_minus_2
                delta_3_f_i = f_i - 3 * f_i_minus_1 + 3 * f_i_minus_2 - f_i_minus_3

                y[i + 1] = y[i] + self.h * f_i + (self.h**2 / 2) * delta_f_i + (5 * self.h**3 / 12) * delta_2_f_i + (3 * self.h**4 / 8) * delta_3_f_i
                err = np.max(y[i + 1] - self.exact_solution[i + 1])
                if err < self.epsilon:
                    break
                # print()
            # if self.exact_solution[i + i]
            print(ii)
        return t, y
    def check_error(self, t, y, i):
        if self.exact_solution is not None:
            y_exact = self.exact_solution[i - 1]
            error = np.abs(y_exact - y[i])
            max_error = np.max(error)
            if max_error < self.epsilon:
                return True
        return False

    def get_exact_solution(self, x):
        f = wrap(self.func)
        arr = scipy.integrate.odeint(f, self.y0, x)
        res = np.array([t[0] for t in arr])
        return res


def func1(x, y):
    return y + (1 + x) * y**2


def func2(x, y):
    return -y + (1 + x) * y**2


def func3(x, y):
    return y - (1 + x) * y**2


def func4(x, y):
    return -y - (1 + x) * y**2


def wrap(f):
    def swapped(y, x):
        return f(x, y)

    return swapped


def main():
    print("Выберите уравнение:")
    print("1. y' = y + (1 + x)y^2")
    print("2. y' = -y + (1 + x)y^2")
    print("3. y' = y - (1 + x)y^2")
    print("4. y' = -y - (1 + x)y^2")
    choice = int(input("Введите номер уравнения (1, 2, 3 или 4): "))

    if choice == 1:
        func = func1
    elif choice == 2:
        func = func2
    elif choice == 3:
        func = func3
    elif choice == 4:
        func = func4
    else:
        print("Неверный выбор")
        return

    y0 = [float(input("Введите начальное условие y0: "))]  # начальное условие y0
    t0 = float(input("Введите начальное значение времени t0: "))
    tn = float(input("Введите конечное значение времени tn: "))
    h = float(input("Введите шаг h: "))
    epsilon = float(input("Введите точность epsilon: "))

    # Create an instance of ODEMethods for Euler method
    ode_methods_euler = ODEMethods(func, y0, t0, tn, h, None, epsilon)
    t_euler, y_euler = ode_methods_euler.euler_improved()
    ode_methods_euler.exact_solution = ode_methods_euler.get_exact_solution(t_euler)

    # Create an instance of ODEMethods for runge_kutta_4 method
    ode_methods_rk4 = ODEMethods(func, y0, t0, tn, h, None, epsilon)
    t_rk4, y_rk4 = ode_methods_rk4.runge_kutta_4()
    ode_methods_rk4.exact_solution = ode_methods_rk4.get_exact_solution(t_rk4)

    # Create an instance of ODEMethods for Milne method
    ode_methods_milne = ODEMethods(func, y0, t0, tn, h, None, epsilon)
    t_milne, y_milne = ode_methods_milne.milne()
    ode_methods_milne.exact_solution = ode_methods_milne.get_exact_solution(t_milne)

    # Create an instance of ODEMethods for Adams method
    ode_methods_adams = ODEMethods(func, y0, t0, tn, h, None, epsilon)
    t_adams, y_adams = ode_methods_adams.adams()
    ode_methods_adams.exact_solution = ode_methods_adams.get_exact_solution(t_adams)
  
    # Create tables
    data_euler = {
        "i": np.arange(len(t_euler)),
        "t": t_euler,
        "Euler Improved": y_euler[:, 0],
        "Exact": ode_methods_euler.exact_solution,
    }
    df_euler = pd.DataFrame(data_euler)
    print("Таблица значений для улучшенного метода Эйлера:")
    print(df_euler)

    # Create tables
    data_rk4 = {
        "i": np.arange(len(t_rk4)),
        "t": t_rk4,
        "Runge-Kutta-4 ": y_rk4[:, 0],
        "Exact": ode_methods_rk4.exact_solution,
    }
    df_rk4 = pd.DataFrame(data_rk4)
    print("Таблица значений для метода Рунге-Кутта 4- го порядка с пересчетом:")
    print(df_rk4)

    data_milne = {
        "i": np.arange(max(len(t_milne), len(t_milne))),
        "t": t_milne,
        "Milne": y_milne[:, 0],
        "Exact": ode_methods_milne.exact_solution,
    }
    df_milne = pd.DataFrame(data_milne)
    print("Таблица значений для метода Милна:")
    print(df_milne)
    
    
    data_adams = {
        "i": np.arange(max(len(t_adams), len(t_adams))),
        "t": t_adams,
        "adams": y_adams[:, 0],
        "Exact": ode_methods_adams.exact_solution,
    }
    df_adams = pd.DataFrame(data_adams)
    print("Таблица значений для метода Адамса:")
    print(df_adams)

    # Evaluate accuracy
    error_euler = np.max(np.abs(y_euler[:, 0] - ode_methods_euler.exact_solution))
    error_rk4 = np.max(np.abs(y_rk4[:, 0] - ode_methods_rk4.exact_solution))
    error_milne = np.max(np.abs(y_milne[:, 0] - ode_methods_milne.exact_solution))
    error_adams = np.max(np.abs(y_adams[:, 0] - ode_methods_adams.exact_solution))

    print(f"Точность метода Эйлера с пересчетом: {error_euler}")
    print(f"Точность метода Рунге-Кутта 4-го порядка: {error_rk4}")
    print(f"Точность метода Милна: {error_milne}")
    print(f"Точность метода Адамса: {error_adams}")

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(t_euler, y_euler[:, 0], label="Euler Improved", color="blue")
    plt.plot(t_rk4, y_rk4[:, 0], label="Runge-Kutta 4", color="green")
    plt.plot(t_milne, y_milne[:, 0], label="Milne", color="red")
    plt.plot(t_adams, y_adams[:, 0], label="Adams", color="yellow")
    plt.plot(
        t_euler,
        ode_methods_euler.exact_solution,
        label="Exact Solution",
        color="black",
        linestyle="dashed",
    )
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend()
    plt.title("Численные решения ОДУ")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
