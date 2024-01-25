import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func_ohm_law(I, R):
    return I * R


def linear_model(x, a, b):
    return (a * x) + b


if __name__ == "__main__":
    data = numpy.loadtxt("voltage-current-data-part1.csv", delimiter=',')

    voltage_data = []
    current_data = []
    voltage_uncert = []
    current_uncert = []
    i = 0
    for line in data:
        voltage_data.append(line[0])
        current_data.append(line[1])
        voltage_uncert.append(line[2])
        current_uncert.append(line[3])

    voltage_data = numpy.array(voltage_data)
    current_data = numpy.array(current_data)
    voltage_uncert = numpy.array(voltage_uncert)
    current_uncert = numpy.array(current_uncert)
    print(voltage_data)
    print(current_data)
    popt, pcov = curve_fit(linear_model, xdata=current_data, ydata=voltage_data, p0 = [470, 1])
    print(popt)
    fit_data = func_ohm_law(current_data, popt[0]) + popt[1]
    residuals = []
    for line in range(len(voltage_data)):
        residuals.append(voltage_data[line] - fit_data[line])
    plt.scatter(voltage_data, residuals)
    plt.xlabel("Current (A)")
    plt.ylabel("Voltage (V)")
    plt.title("Ohm's Law")
    plt.rcParams["figure.dpi"] = 900
    plt.show()
