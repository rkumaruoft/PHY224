import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy
import pylab


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


def x_r2_metric_2(N, m, measured_current_data, calculated_data, uncertainties):
    sum = 0
    for i in range(N):
        sum += ((measured_current_data[i] - calculated_data[i]) ** 2) / (uncertainties[i] ** 2)

    return sum / (N - m)


def main_func(data):
    voltage_data = []
    current_data = []
    voltage_uncert = []
    current_uncert = []
    i = 0
    for line in data:
        voltage_data.append(line[0])
        current_data.append(line[1] * 1000)
        voltage_uncert.append(line[2])
        current_uncert.append(line[3] * 1000)

    voltage_data = numpy.array(voltage_data)
    current_data = numpy.array(current_data)
    voltage_uncert = numpy.array(voltage_uncert)
    current_uncert = numpy.array(current_uncert)
    plt.errorbar(voltage_data, current_data, yerr=current_uncert, xerr=voltage_uncert, fmt=" ")
    """ Fitting the model"""
    popt, pcov = curve_fit(linear_model, xdata=voltage_data, ydata=current_data,
                           sigma=current_uncert, absolute_sigma=True,
                           p0=[1 / 470, 0])
    print(popt)
    perr = numpy.sqrt(numpy.diag(pcov))[0]
    print("Uncertainty on 1/r(" + str(popt[0]) + ") = " + str(perr))
    resistance_error = (popt[0] ** -1) * (perr / popt[0])
    print("Resistance = " + str(1 / popt[0]) + "+-" + str(resistance_error))
    fit_data = linear_model(voltage_data, popt[0], popt[1])
    plt.plot(voltage_data, fit_data, label='y = mx +b')
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")

    plt.subplots_adjust(bottom=0.2)
    plt.legend()
    plt.savefig("Ohm's_law(mx+b)", dpi=250)
    plt.show()

    """ chi_r^2 metric calculation"""
    x_r2 = x_r2_metric(len(current_data), 2, current_data, voltage_data, popt[0], popt[1], current_uncert)
    print(x_r2)
    popt, pcov = curve_fit(linear_model_2,
                           xdata=voltage_data,
                           ydata=current_data,
                           sigma=current_uncert,
                           absolute_sigma=True,
                           p0=[1 / 470])
    print(popt)
    perr = numpy.sqrt(numpy.diag(pcov))[0]
    print("Uncertainty on 1/r(" + str(popt[0]) + ") = " + str(perr))
    resistance_error = (popt[0] ** -1) * (perr / popt[0])
    print("Resistance = " + str(1 / popt[0]) + "+-" + str(resistance_error))
    """ plotting graphs"""
    plt.errorbar(voltage_data, current_data, yerr=current_uncert, xerr=voltage_uncert, fmt=" ")
    fit_data = linear_model_2(voltage_data, popt[0])
    x_r2 = x_r2_metric_2(len(current_data), 2, current_data, fit_data,current_uncert)
    print(x_r2)
    plt.plot(voltage_data, fit_data, label='y = mx', linestyle='dashed', color='blue')
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.subplots_adjust(bottom=0.2)
    plt.legend()
    plt.savefig("Ohm's_Law(mx)", dpi=250)
    plt.show()
