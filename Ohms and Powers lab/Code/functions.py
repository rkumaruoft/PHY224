import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy


def func_ohm_law(voltage, resistance):
    return voltage / resistance


def linear_model(x, a, b):
    return (a * x) + b


def linear_model_2(x, a):
    return a * x


def x_r2_metric(N, m, measured_current_data, voltage_data, a, b, uncertainties):
    sum = 0
    for i in range(N):
        sum += (((measured_current_data[i] - linear_model(voltage_data[i], a, b)) ** 2) / (uncertainties[i] ** 2))
    return sum / (N - m)


def main_func(data):
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
    plt.errorbar(voltage_data, current_data, yerr=current_uncert, xerr=voltage_uncert, fmt=" ")
    popt, pcov = curve_fit(linear_model, xdata=voltage_data, ydata=current_data, p0=[1 / 470, 0])
    print(popt)
    fit_data = func_ohm_law(voltage_data, 1 / popt[0])
    plt.plot(voltage_data, fit_data, label='Curve Fit (y = mx +b)')
    x_r2 = x_r2_metric(len(current_data), 2, current_data, voltage_data, popt[0], popt[1], current_uncert)
    print(x_r2)
    popt, pcov = curve_fit(linear_model_2, xdata=voltage_data, ydata=current_data, p0=[1 / 470])
    fit_data = func_ohm_law(voltage_data, 1 / popt[0])
    plt.plot(voltage_data, fit_data, label='Curve Fit (y = mx)', linestyle='dashed', color='blue')
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Ohm's Law")
    plt.legend()
    plt.rcParams["figure.dpi"] = 900
    plt.show()
