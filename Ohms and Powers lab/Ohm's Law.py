import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func_ohm_law(current, resistance):
    return current * resistance


def linear_model(x, a, b):
    return (a * x) + b


def linear_model_2(x, a):
    return a * x


def x_r2_metric(N, m, func, measured_data, uncertainties):
    to_sum = []
    for i in range(N):
        to_sum.append(((measured_data[i] - func) ** 2)
                      / (uncertainties[i] ** 2))
    return sum(to_sum) / (N - m)


if __name__ == "__main__":
    # TODO: Get device uncertainty and add to to the uncertainty data
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
    popt, pcov = curve_fit(linear_model, xdata=current_data, ydata=voltage_data, p0=[470, 0])
    print(popt)
    plt.errorbar(current_data, voltage_data, yerr=voltage_uncert, xerr=current_uncert, fmt=" ")
    fit_data = func_ohm_law(current_data, popt[0])
    plt.plot(current_data, fit_data)
    popt, pcov = curve_fit(linear_model_2, xdata=current_data, ydata=voltage_data, p0=[470])
    #TODO: x_r_metric
    # x_r_metric = x_r2_metric(len(current_data), 2, func_ohm_law(current_data, popt[0]), voltage_data, voltage_uncert)
    # print(x_r_metric)
    print(popt)
    plt.xlabel("Current (A)")
    plt.ylabel("Voltage (V)")
    plt.title("Ohm's Law")
    plt.rcParams["figure.dpi"] = 900
    plt.show()
