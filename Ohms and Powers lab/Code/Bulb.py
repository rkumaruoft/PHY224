import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functions import linear_model,


def power_law(voltage, resistance): # TODO
    return voltage / resistance


def power_model(x, c, d):
    return c*x**d


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
    # for linear regression on the linear model


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
    popt, pcov = curve_fit(linear_model, xdata=voltage_data, ydata=current_data, p0=[1 / 470, 0]) # logarithm on the data
    print(popt)
    fit_data = func_ohm_law(voltage_data, 1 / popt[0])
    plt.plot(voltage_data, fit_data, label='Curve Fit (y = mx +b)')
    x_r2 = x_r2_metric(len(current_data), 2, current_data, voltage_data, popt[0], popt[1], current_uncert)
    print(x_r2)
    popt, pcov = curve_fit(linear_model_2, xdata=voltage_data, ydata=current_data, p0=[1 / 470]) # curve fit the power model
    fit_data = func_ohm_law(voltage_data, 1 / popt[0])
    plt.plot(voltage_data, fit_data, label='Curve Fit (y = mx)', linestyle='dashed', color='blue')
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Ohm's Law")
    plt.legend()
    plt.rcParams["figure.dpi"] = 900
    plt.show()


if __name__ == "__main__":
    data = numpy.loadtxt("voltage-current-data_bulb-part3.csv", delimiter=',')
    main_func(data)
