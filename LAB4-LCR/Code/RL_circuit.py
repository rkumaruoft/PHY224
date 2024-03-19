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
    plt.errorbar(time_data, voltage_data, yerr= 0.05, ls="None", marker=".",
                 label="Resistor Data", markersize=1, elinewidth=0.2)
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

    """ For Residual """


    measured_data1 = rise_1_voltage_data
    calculated_data1 = rise_1_fit_data
    x_axis_data1 = rise_1_time_data


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

    """ For Residual """


    measured_data2 = fall_1_voltage_data
    calculated_data2 = fall_1_fit_data
    x_axis_data2 = fall_1_time_data




# rise 1 from 1.501 - 1.97
    rise_1_time_data = []
    rise_1_voltage_data = []
    for index in range(len(time_data)):
        if 1.501 <= time_data[index] <= 1.97:
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

    # fall 1 from 1.996 - 2.484
    fall_1_time_data = []
    fall_1_voltage_data = []
    for index in range(len(time_data)):
        if 1.996 <= time_data[index] <= 2.484:
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

    # rise 1 from 2.502 - 2.986
    rise_1_time_data = []
    rise_1_voltage_data = []
    for index in range(len(time_data)):
        if 2.502 <= time_data[index] <= 2.986:
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

    # fall 1 from 2.997 - 3.492
    fall_1_time_data = []
    fall_1_voltage_data = []
    for index in range(len(time_data)):
        if 2.997 <= time_data[index] <= 3.492:
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

    # rise 1 from 3.503 - 3.976
    rise_1_time_data = []
    rise_1_voltage_data = []
    for index in range(len(time_data)):
        if 3.503 <= time_data[index] <= 3.976:
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

    # fall 1 from 2.997 - 3.492
    fall_1_time_data = []
    fall_1_voltage_data = []
    for index in range(len(time_data)):
        if 2.997 <= time_data[index] <= 3.492:
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

    # fall 1 from 3.995 - 4.48
    fall_1_time_data = []
    fall_1_voltage_data = []
    for index in range(len(time_data)):
        if 3.995 <= time_data[index] <= 4.48:
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
    plt.xlabel("Time (milli-Seconds)")
    plt.ylabel("Voltage (Volts)")
    plt.savefig("RL_circuit_resistor_voltage.png", dpi=250)
    plt.show()

    print("mean of tau", numpy.mean(tau_values))
    print("error of tau", np.sqrt(numpy.sum([t**2 for t in tau_errors])))


    """ For residuals """
    plot_residual(measured_data1, calculated_data1, x_axis_data1, 0.05,
                  "RL Resistor voltage Residual (rise)",
                  "Time (milli-Seconds)", "Voltage (Volts)")
    #chi_r^2
    # for the first rise
    print("chi^2 of rise: ", reduced_x_r2_abs(len(measured_data1), 2,
                                              measured_data1,
                                              calculated_data1, 0.05))

    plot_residual(measured_data2, calculated_data2, x_axis_data2, 0.05,
                  "RL Resistor voltage Residual (fall)",
                  "Time (milli-Sec)", "Voltage (V)")

    #chi_r^2
    # for the first rise
    print("chi^2 of fall: ", reduced_x_r2_abs(len(measured_data2), 2,
                                              measured_data2,
                                              calculated_data2, 0.05))






    # last curve, fall, just for considertion or an extra look perhaps.
    # measured_data2 = fall_1_voltage_data
    # calculated_data2 = fall_1_fit_data
    # x_axis_data2 = fall_1_time_data
    #
    # plot_residual(measured_data2, calculated_data2, x_axis_data2, 0, "RL Resistor voltage Residual (fall, last )", "Time (milli-Sec)", "Voltage (V)")

