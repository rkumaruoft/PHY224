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


if __name__ == "__main__":
    data = numpy.loadtxt("../voltage_current_data_bulb_part3.csv", delimiter=',')
    voltage_data = []
    current_data = []
    voltage_uncert = []
    current_uncert = []
    # calculated contanst for theoretical data (calculated from V = 10.387 I = 0.0229)
    k = 0.005622654571 * 1000

    # for linear regression on the linear model
    i = 0
    for line in data:
        voltage_data.append(line[0])
        current_data.append(line[1] * 1000)
        voltage_uncert.append(line[2])
        current_uncert.append(line[3] * 1000)

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
    print("Exponent = ", popt[0])
    log_model_data = linear_model(log_voltage_data, popt[0], popt[1])
    antilog_model_data = []
    for line in log_model_data:
        antilog_model_data.append(math.exp(line))
    plt.plot(voltage_data, antilog_model_data, linestyle='dotted', color='black', label='Log Linear regression')
    # X_r_linear metric calculations
    x_r_linear = x_r2_metric(len(log_current_data), 2, current_data, antilog_model_data, current_uncert)
    print(x_r_linear)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.legend()
    plt.savefig('Log_Linear_Model.png', dpi=250)
    plt.show()

    # parameter standerd deviation
    print("pcov log model :", pcov)
    variance_a = pcov[0][0]
    standard_dev_a = math.sqrt(variance_a)
    print("Standard Deviation Exponent (a): ", standard_dev_a)
    variance_b = pcov[1][1]
    standard_dev_b = math.sqrt(variance_b)
    # th
    print("Standard Deviation of log(proportionality constant (b)): ", standard_dev_b)

    # log model residuals
    residuals = []
    for line in range(len(log_model_data)):
        residuals.append(log_current_data[line] - log_model_data[line])
    plt.scatter(voltage_data, residuals)
    plt.axhline(y=0)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.savefig('Log_Linear_Model_residuals.png', dpi=250)
    plt.show()
    print("\n\n\nPOWER MODEL\n\n\n")
    # POWER MODEL CALCULATIONS
    plt.errorbar(voltage_data, current_data, yerr=current_uncert, xerr=voltage_uncert, fmt=" ")
    popt, pcov = curve_fit(power_model, xdata=voltage_data, ydata=current_data)
    print("Popt of powermodel:" + str(popt))
    model_data = power_model(voltage_data, popt[0], popt[1])
    print("Exponent = ", popt[1])
    # X-r_power metric calculations
    x_r_power = x_r2_metric(len(current_data), 2, current_data, model_data, current_uncert)
    print(x_r_power)
    plt.plot(voltage_data, model_data, label='Nonlinear Regression')
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.legend()
    plt.savefig('power_model.png', dpi=250)
    plt.show()

    # parameter standerd deviation
    print("pcov power model :", pcov)
    variance_c = pcov[0][0]
    standard_dev_c = math.sqrt(variance_c)
    print("Standard Deviation Proportionality Constant (c): ", standard_dev_c)
    variance_d = pcov[1][1]
    standard_dev_d = math.sqrt(variance_d)
    print("Standard Deviation Exponent (d): ", standard_dev_d)

    # power model residuals
    residuals_power = []
    for line in range(len(model_data)):
        residuals_power.append(current_data[line] - model_data[line])
    plt.scatter(voltage_data, residuals)
    plt.axhline(y=0)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.savefig('power_model_residuals.png', dpi=250)
    plt.show()

    print("\n\n\nTHEORETICAL MODEL\n\n\n")
    # Theoretical Model Calculations- get a constant from just one v-I value and use it to plot the rest of the data
    plt.errorbar(voltage_data, current_data, yerr=current_uncert, xerr=voltage_uncert, fmt=" ")
    popt, pcov = curve_fit(theoretical_model, xdata=voltage_data, ydata=current_data)
    print("Popt of thoretical model" + str(popt))
    theoretical_data = theoretical_model(voltage_data, k)
    plt.plot(voltage_data, theoretical_data, linestyle='dashed', color='blue', label='Theoretical Curve')
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.title("Bulb Plot (Theoretical Model)")
    plt.legend()
    plt.show()

    # theoretical model residuals
    residuals_theoretical = []
    for line in range(len(model_data)):
        residuals_theoretical.append(current_data[line] - theoretical_data[line])
    plt.scatter(voltage_data, residuals_theoretical)
    plt.axhline(y=0)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.title("Theoretical model residuals")
    plt.show()
