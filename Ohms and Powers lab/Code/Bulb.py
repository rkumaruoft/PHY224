import math

import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import linear_model


def power_law(voltage, prop_constant):  # TODO
    return prop_constant * (voltage**(3/5))


def power_model(x, c, d):
    return c * x ** d


def linear_log_model(x, a, b):
    return b * math.log(x) + math.log(a)


def x_r2_metric(N, m, measured_current_data, voltage_data, a, b, uncertainties):
    sum = 0
    for i in range(N):
        sum += (((measured_current_data[i] - linear_model(voltage_data[i], a, b)) ** 2) / (uncertainties[i] ** 2))
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
    #TODO curve fit log_x and log_y
    # popt, pcov = curve_fit(linear_model, xdata=log_voltage_data, ydata=log_current_data)  # logarithm on the data
    # print(popt)
    # # # b^Log_b(K) = k
    # # # do math to convert log model to power formula
    # # # y=cx^d , log(y) = dlog(x) + log(c)
    # # from curve fitting the log of x and y data;
    # # log(y)=a log(x)+b
    # # a=d, b=log(c)
    # a = popt[0]
    # # plt.plot(log_voltage_data, fit_data)
    # fit_data = powe(voltage_data, a)
    popt, pcov = curve_fit(power_model, xdata=voltage_data, ydata=current_data)
    print(popt)
    model_data = power_model(voltage_data,popt[0],popt[1])
    plt.plot(voltage_data, model_data)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Ohm's Law")
    plt.legend()
    plt.rcParams["figure.dpi"] = 900
    plt.show()
