import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':

    lc_capacitor_data = read_file_data("../LC_circuit_capacitor_ex2.csv")
    time_data = []
    voltage_data = []
    for line in lc_capacitor_data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        time_data.append(this_line[0])
        voltage_data.append(this_line[1])

    min_time = abs(min(time_data))
    time_data = numpy.array([t + min_time for t in time_data])
    min_voltage = 0.7
    voltage_data = numpy.array([t + min_voltage for t in voltage_data])

    plt.errorbar(time_data, voltage_data, ls="None", marker=".", label="Capacitor Data")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.title("LC Capacitor Voltage")
    plt.axhline(y=0)
    popt, pcov = curve_fit(LC_equation, xdata=time_data, ydata=voltage_data, p0=[1, 31723.67559, np.pi / 2])
    curve_data = LC_equation(time_data, popt[0], popt[1], abs(popt[2]))
    # Using Phase as pi + 0.5 gives a better fit
    # curve_data = LC_eqation(time_data, popt[0], popt[1], np.pi+0.5)
    plt.plot(time_data, curve_data, label="Best Fit Curve")
    omega = popt[1]
    omega_error = math.sqrt(pcov[1][1])
    print("LC CIRCUIT")
    print("Omega : ", omega, "Error: ", omega_error)
    LC_val = 1 / (omega ** 2)
    LC_err = (2 / (omega ** 3)) * omega_error
    print("LC : ", LC_val, "Error: ", LC_err)
    plt.legend(loc='upper left')
    plt.show()
