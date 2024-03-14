import math
import matplotlib as mat
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *


if __name__ == '__main__':
    RL_resistor_data = read_file_data("../RL_circuit_resistor_ex2.csv")
    time_data = []
    voltage_data = []
    for line in RL_resistor_data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        time_data.append(this_line[0])
        voltage_data.append(this_line[1])

    min_time = abs(min(time_data))
    time_data = np.array([(t + min_time) * (10 ** 3) for t in time_data])
    min_voltage = abs(min(voltage_data))
    voltage_data = np.array([v + min_voltage for v in voltage_data])
    plt.errorbar(time_data, voltage_data, ls="None", marker=".", label="Capacitor Data")

    tau_values = []
    tau_errors = []

    # rise 1 from 0.4899 - 0.9829
    rise_1_time_data = []
    rise_1_voltage_data = []
    for index in range(len(time_data)):
        if 0.4899 <= time_data[index] <= 0.9829:
            rise_1_time_data.append(time_data[index])
            rise_1_voltage_data.append(voltage_data[index])

    rise_1_voltage_data = np.array(rise_1_voltage_data)
    min_time_rise_1 = min(rise_1_time_data)
    rise_1_time_data_scaled = np.array([(t - min_time_rise_1) for t in rise_1_time_data])
    popt, pcov = curve_fit(RL_rise_equation, rise_1_time_data_scaled, rise_1_voltage_data)
    rise_1_fit_data = RL_rise_equation(rise_1_time_data_scaled, popt[0], popt[1])
    tau_values.append(popt[1])
    tau_errors.append(math.sqrt(pcov[1][1]))
    plt.plot(rise_1_time_data, rise_1_fit_data)


    # fall 1 from 0.99 - 1.47
    fall_1_time_data = []
    fall_1_voltage_data = []
    for index in range(len(time_data)):
        if 0.99 <= time_data[index] <= 1.47:
            fall_1_time_data.append(time_data[index])
            fall_1_voltage_data.append(voltage_data[index])

    fall_1_voltage_data = np.array(fall_1_voltage_data)
    min_time_fall_1 = min(fall_1_time_data)
    fall_1_time_data_scaled = np.array([(t - min_time_fall_1) for t in fall_1_time_data])
    popt, pcov = curve_fit(RL_fall_equation, fall_1_time_data_scaled, fall_1_voltage_data)
    fall_1_fit_data = RL_fall_equation(fall_1_time_data_scaled, popt[0], popt[1])
    tau_values.append(popt[1])
    tau_errors.append(math.sqrt(pcov[1][1]))
    plt.plot(fall_1_time_data, fall_1_fit_data)


    plt.axhline(y=0)
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Voltage (volts)")
    plt.show()
