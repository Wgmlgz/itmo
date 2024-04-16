
# Function to read data from console input
import json
import numpy as np
import matplotlib.pyplot as plt


def read_data_console():
    print("Введите значения x и y через запятую (например, 0.1, 2.3). Для завершения ввода оставьте строку пустой и нажмите Enter")
    x_values = []
    y_values = []
    while True:
        try:
            line = input()
            if line.strip() == '':
                break
            x, y = map(float, line.split(','))
            x_values.append(x)
            y_values.append(y)
        except ValueError:
            print(
                "Некорректный ввод")
    return np.array(x_values), np.array(y_values)


# Function to read data from a file
def read_data_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        x_values = np.array(data['x_values'])
        y_values = np.array(data['y_values'])
        return x_values, y_values


def output_to_json(approximations, rms_values, pearson_corr, r_squared, best_fit_name):
    output = {
        'Linear': approximations[0].to_json(),
        'Quadratic': approximations[1].to_json(),
        'Cubic': approximations[2].to_json(),
        'Exponential': approximations[3].to_json(),
        'Logarithmic': approximations[4].to_json(),
        'Power': approximations[5].to_json(),
        'Pearson Correlation Coefficient': pearson_corr,
        'Coefficient of Determination': r_squared,
        'Best Fit': best_fit_name
    }
    # fs = }
    
    
    return json.dumps(output, indent=4)


# Function to plot the data and fits
def plot_data_and_fits(x, y, approximations):
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, 'ko', label='Original Data')
    
    x_dense = np.linspace(np.min(x), np.max(x), 500)
     
    for item in approximations:
        fitted_values_dense = item.function(x_dense, *item.params)
        plt.plot(x_dense, fitted_values_dense, label=item.name)
        
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function Approximations')
    plt.legend()
    plt.grid(True)
    plt.show()