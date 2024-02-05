import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functions import func_ohm_law, linear_model, linear_model_2

if __name__ == "__main__":
    data = numpy.loadtxt("../voltage_current_data_part2.csv", delimiter=',')

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
    popt, pcov = curve_fit(linear_model_2, xdata=voltage_data, ydata=current_data)
    print(popt)
    fit_data = linear_model_2(voltage_data, popt[0])
    residuals = []
    for line in range(len(current_data)):
        residuals.append(current_data[line] - fit_data[line])
    plt.errorbar(voltage_data, residuals, yerr=current_uncert, xerr=voltage_uncert, fmt=".")
    plt.axhline(y=0)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.savefig("potentiometer_residual(mx)", dpi=250)
    plt.show()

    popt, pcov = curve_fit(linear_model, xdata=voltage_data, ydata=current_data)
    print(popt)
    fit_data = linear_model(voltage_data, popt[0], popt[1])
    residuals = []
    for line in range(len(current_data)):
        residuals.append(current_data[line] - fit_data[line])
    plt.errorbar(voltage_data, residuals, yerr=current_uncert, xerr=voltage_uncert, fmt=".")
    plt.axhline(y=0)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.savefig("potentiometer_residual(mx+b)", dpi=250)
    plt.show()
