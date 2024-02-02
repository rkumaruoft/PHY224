import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import linear_model
from Bulb import theoretical_model, power_model


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
    popt, pcov = curve_fit(linear_model, xdata=log_voltage_data, ydata=log_current_data)
    print("Popt of log model: ", popt)
    log_model_data = linear_model(log_voltage_data, popt[0], popt[1])
    antilog_model_data = []
    for line in log_model_data:
        antilog_model_data.append(math.exp(line))
    plt.plot(voltage_data, antilog_model_data, linestyle='dotted', color='black', label='Log Linear regression')
    popt, pcov = curve_fit(power_model, xdata=voltage_data, ydata=current_data)
    print(popt)
    model_data = power_model(voltage_data, popt[0], popt[1])
    popt, pcov = curve_fit(theoretical_model, xdata=voltage_data, ydata=current_data)
    print(popt)
    theoretical_data = theoretical_model(voltage_data, popt[0])
    plt.plot(voltage_data, model_data)
    plt.plot(voltage_data, theoretical_data, linestyle='dashed', color='blue')
    pylab.plt.xscale('log')
    pylab.plt.yscale('log')
    plt.xlabel("log(Voltage) (V)")
    plt.ylabel("log(Current) (A)")
    plt.title("Bulb Data")
    plt.legend()
    plt.rcParams["figure.dpi"] = 900
    plt.show()
