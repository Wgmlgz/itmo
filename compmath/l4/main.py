import argparse
import json
import numpy as np
from approx import CubicApproximation, ExponentialApproximation, LinearApproximation, LogarithmicApproximation, PowerApproximation, QuadraticApproximation
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

from utils import output_to_json, plot_data_and_fits, read_data_console, read_data_json

# Add argparse functionality to parse command line arguments


def parse_args():
    parser = argparse.ArgumentParser(
        description='Fit various functions to data using the method of least squares.')
    parser.add_argument('-f', '--file', type=str,
                        help='Path to the JSON file with input data. If not provided, data is read from console.')
    return parser.parse_args()

# Main execution function with argparse implementation


def main():
    args = parse_args()

    if args.file:
        x_values, y_values = read_data_json(args.file)
    else:
        x_values, y_values = read_data_console()

    # Instantiate each approximation type
    approximations = [
        LinearApproximation(x_values, y_values, p0=[1, 1]),
        QuadraticApproximation(x_values, y_values, p0=[1, 1, 1]),
        CubicApproximation(x_values, y_values, p0=[1, 1, 1, 1]),
        ExponentialApproximation(x_values, y_values, p0=[1, -1, 1]),
        LogarithmicApproximation(x_values, y_values, p0=[1, 1]),
        PowerApproximation(x_values, y_values, p0=[1, 0.1])
    ]

    # Fit data and calculate RMS for each approximation
    for approximation in approximations:
        approximation.prepare()
        approximation.fit()
        approximation.post_process()

    # Calculate Pearson correlation coefficient for linear function
    pearson_corr, _ = pearsonr(x_values, y_values)
    r_squared = pearson_corr**2

    print(f'Коэффициент корреляции Пирсона: {pearson_corr}')
    print(f'Коэффициент детерминации (R^2): {r_squared}')

    # Find the best fitting function
    rms_values = [approximation.rms for approximation in approximations]
    best_fit_index = np.argmin(rms_values)
    best_fit_name = approximations[best_fit_index].name

    print(f'Лучшее приближение: {best_fit_name}')

    # Output to JSON
    output = output_to_json(approximations,
                            rms_values, pearson_corr, r_squared, best_fit_name)
    print(output)

    # Plot the data and fits
    plot_data_and_fits(x_values, y_values, approximations)


if __name__ == '__main__':
    main()
