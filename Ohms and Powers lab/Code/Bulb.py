import math

import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import linear_model


def theoretical_model(voltage, prop_constant):
    return prop_constant * (voltage ** (3 / 5))


def power_model(x, c, d):
    return c * (x ** d)


def x_r2_metric(N, m, measured_current_data, calculated_data, uncertainties):
    sum = 0
    for i in range(N):
        sum += ((measured_current_data[i] - calculated_data[i]) ** 2) / (uncertainties[i] ** 2)
    return sum / (N - m)


def x_r2_metric_power(N, m, measured_current_data, voltage_data, c, d, uncertainties):
    sum = 0
    for i in range(N):
        sum += (((measured_current_data[i] - power_model(voltage_data[i], c, d)) ** 2) / (uncertainties[i] ** 2))
    return sum / (N - m)


if __name__ == "__main__":
    data = numpy.loadtxt("../voltage_current_data_bulb_part3.csv", delimiter=',')
    voltage_data = []
    current_data = []
    voltage_uncert = []
    current_uncert = []
    # for linear regression on the linear model
    i = 0
    for line in data:
        voltage_data.append(line[0])
        current_data.append(line[1])
        voltage_uncert.append(line[2])
        current_uncert.append(line[3])

    log_voltage_data = numpy.array([math.log(x) for x in voltage_data])
    log_current_data = numpy.array([math.log(x) for x in current_data])
    voltage_data = numpy.array(voltage_data)
    current_data = numpy.array(current_data)
    voltage_uncert = numpy.array(voltage_uncert)
    current_uncert = numpy.array(current_uncert)

    plt.errorbar(voltage_data, current_data, yerr=current_uncert, xerr=voltage_uncert, fmt=" ")

    # LOG MODEL CALCULATIONS
    popt, pcov = curve_fit(linear_model, xdata=log_voltage_data, ydata=log_current_data)
    print("Popt of log model: ", popt)
    log_model_data = linear_model(log_voltage_data, popt[0], popt[1])
    antilog_model_data = []
    for line in log_model_data:
        antilog_model_data.append(math.exp(line))
    plt.plot(voltage_data, antilog_model_data, linestyle='dotted', color='black', label='Log Linear regression')
    # X_r_linear metric calculations
    x_r_linear = x_r2_metric(len(log_current_data), 2, current_data, antilog_model_data, current_uncert)
    print(x_r_linear)

    # POWER MODEL CALCULATIONS
    popt, pcov = curve_fit(power_model, xdata=voltage_data, ydata=current_data)
    print("Popt of powermodel:" + str(popt))
    model_data = power_model(voltage_data, popt[0], popt[1])
    plt.plot(voltage_data, model_data, label='Nonlinear Regression')
    # X-r_power metric calculations
    x_r_power = x_r2_metric(len(current_data), 2,current_data, model_data, current_uncert)
    print(x_r_power)
    # Theoretical Model Calculations- get a constant from just one v-I value and use it to plot the rest of the data
    popt, pcov = curve_fit(theoretical_model, xdata=voltage_data, ydata=current_data)
    print("Popt of thoretical model" + str(popt))
    theoretical_data = theoretical_model(voltage_data, popt[0])
    plt.plot(voltage_data, theoretical_data, linestyle='dashed', color='blue', label='Theoretical Curve')

    # Co-Variance calculations



    print(pcov)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Ohm's Law")
    plt.legend()
    plt.rcParams["figure.dpi"] = 900
    plt.show()
