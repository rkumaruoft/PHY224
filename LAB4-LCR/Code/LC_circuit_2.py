import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *


def wave_equation(t, w, v_in, p):
    return v_in * (1 - numpy.sin((w * t)/2*np.pi) + p)


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
    time_data = numpy.array([(t + min_time) * 10 ** 3 for t in time_data])
    min_voltage = 0.7
    voltage_data = numpy.array([t + min_voltage for t in voltage_data])

    plt.errorbar(time_data, voltage_data, ls="None", marker=".",
                 label="Capacitor Data")
    plt.xlabel("Time (milli-Sec)")
    plt.ylabel("Voltage (V)")
    plt.title("LC Capacitor Voltage")
    plt.axhline(y=0)

    popt, pcov = curve_fit(wave_equation, xdata=time_data, ydata=voltage_data, p0=[1, 30204, math.pi])
    curve_data = wave_equation(time_data, popt[0], popt[1], popt[2])
    plt.plot(time_data, curve_data, label="Best Fit Curve")
    plt.legend(loc='upper left')
    plt.show()
