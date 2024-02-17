import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit

int_resistance = []


def terminal_voltage_func(current, r_internal, v_inf):
    return v_inf - (r_internal * current)

def loaf_file_data(voltage_arr, current_arr, voltage_uncert, current_uncert, filename):
    data = numpy.loadtxt(filename)
    return data


def draw_func(data1, data2, title):
    volt_data1 = make_data_array(data1)[0]
    curr_data1 = make_data_array(data1)[1]
    volt_uncert1 = make_data_array(data1)[2]
    curr_uncert1 = make_data_array(data1)[3]

    plt.scatter(curr_data1, volt_data1)
    plt.errorbar(curr_data1, volt_data1, xerr=curr_uncert1, yerr=volt_uncert1, fmt=".")
    # plotting the curve fit for data1
    model_data1 = terminal_voltage_func(curr_data1, calc_resistance(data1)[0], calc_resistance(data1)[1])
    plt.plot(curr_data1,
             model_data1)

    volt_data2 = make_data_array(data2)[0]
    curr_data2 = make_data_array(data2)[1]
    volt_uncert2 = make_data_array(data2)[2]
    curr_uncert2 = make_data_array(data2)[3]

    plt.scatter(curr_data2, volt_data2)
    plt.errorbar(curr_data2, volt_data2, xerr=curr_uncert2, yerr=volt_uncert2, fmt=".")
    # plotting the curve fit for data1
    model_data2 = terminal_voltage_func(curr_data2, calc_resistance(data2)[0], calc_resistance(data2)[1])
    plt.plot(curr_data2,
             model_data2)

    plt.xlabel("Current")
    plt.ylabel("Voltage")
    plt.legend(["option 1", "curve fit 1", "option 2", "curve fit 2"])
    plt.title(title)
    plt.savefig('Log_Linear_Model.png', dpi=250)
    plt.show()

    # DATA 1 residuals
    draw_residual(volt_data1, model_data1, curr_data1, volt_uncert1, title + " option_1 residuals")
    # Data 2 residulas
    draw_residual(volt_data2, model_data2, curr_data2, volt_uncert2, title + " option_2 residuals")


def draw_residual(measured_data, calculated_data, x_axis_data, measured_uncert, title):
    residuals = []
    for line in range(len(measured_data)):
        residuals.append(measured_data[line] - calculated_data[line])
    plt.errorbar(x_axis_data, residuals, yerr=measured_uncert, fmt=".")
    plt.xlabel("Current")
    plt.ylabel("Voltage")
    plt.title(title)
    plt.axhline(y=0)
    plt.figure(figsize=(10, 6))
    plt.savefig('.png', dpi=250)
    plt.show()


def make_data_array(data):
    volt_data = []
    curr_data = []
    volt_uncert = []
    curr_uncert = []
    for line in data:
        volt_data.append(line[0])
        curr_data.append(line[1])
        volt_uncert.append(line[2])
        curr_uncert.append(line[3])
    volt_data = numpy.array(volt_data)
    curr_data = numpy.array(curr_data)
    volt_uncert = numpy.array(volt_uncert)
    curr_uncert = numpy.array(volt_uncert)
    return volt_data, curr_data, volt_uncert, curr_uncert


def calc_resistance(data):
    volt_data = make_data_array(data)[0]
    curr_data = make_data_array(data)[1]
    volt_uncert = make_data_array(data)[2]
    curr_uncert = make_data_array(data)[3]
    popt, pcov = curve_fit(terminal_voltage_func, curr_data, volt_data,
                           sigma=volt_uncert, absolute_sigma=True)

    return popt[0], popt[1]


def x_r2_metric_2(N, m, measured_data, calculated_data, uncertainties):
    sum = 0
    for i in range(N):
        sum += ((measured_data[i] - calculated_data[i]) ** 2) / (uncertainties[i] ** 2)
    return sum / (N - m)


def print_resistance_values(data):
    volt_data = make_data_array(data)[0]
    curr_data = make_data_array(data)[1]
    volt_uncert = make_data_array(data)[2]
    curr_uncert = make_data_array(data)[3]
    popt, pcov = curve_fit(terminal_voltage_func, curr_data, volt_data,
                           sigma=volt_uncert, absolute_sigma=True)
    print("popt: ", popt)
    print("pcov: ", pcov)
    model_data = terminal_voltage_func(curr_data, popt[0], popt[1])
    x_r = x_r2_metric_2(len(volt_data), 2, volt_data, model_data, volt_uncert)
    print("X-r: ", x_r)
    resistance_error = numpy.sqrt(numpy.diag(pcov))[0]
    v_terminal_error = numpy.sqrt(numpy.diag(pcov))[1]
    print("Error of internal resistance: ", resistance_error)
    print("Error of terminal voltage: ", v_terminal_error)
    int_resistance.append([[popt[0], resistance_error], [popt[1], v_terminal_error]])
    print()
    print()


if __name__ == "__main__":
    # for cell battery
    # todo: TALK ABOUT THE OUTLIER POINT IN DATA1
    """ Part 1"""
    title = "Cell battery"
    print(title)
    print()
    data1 = numpy.loadtxt("../cell_battery_option_1.csv", delimiter=',')
    data2 = numpy.loadtxt("../cell_battery_option_2.csv", delimiter=',')

    calc_resistance(data1)
    print_resistance_values(data1)
    calc_resistance(data2)
    print_resistance_values(data2)

    draw_func(data1, data2, " Cell battery ")
    """ Part 2"""

    # open circuit voltage

    # 6.5 V
    title = "DC supply 6.5V"
    print(title)
    print()
    data6_i = numpy.loadtxt("../DC_suppy_6.5_option_1.csv", delimiter=',')
    data6_ii = numpy.loadtxt("../DC_suppy_6.5_option_2.csv", delimiter=',')

    calc_resistance(data6_i)
    print_resistance_values(data6_i)
    calc_resistance(data6_ii)
    print_resistance_values(data6_ii)

    draw_func(data6_i, data6_ii, title)
    # 10 V
    title = "DC supply 10V"
    print(title)
    print()
    data10_i = numpy.loadtxt("../DC_suppy_10_option_1.csv", delimiter=',')
    data10_ii = numpy.loadtxt("../DC_suppy_10_option_2.csv", delimiter=',')

    calc_resistance(data10_i)
    print_resistance_values(data10_i)
    calc_resistance(data10_ii)
    print_resistance_values(data10_ii)

    draw_func(data10_i, data10_ii, title)

    # 15 V
    title = "DC supply 15V"
    print(title)
    print()
    data15_i = numpy.loadtxt("../DC_suppy_15_option_1.csv", delimiter=',')
    data15_ii = numpy.loadtxt("../DC_suppy_15_option_2.csv", delimiter=',')

    calc_resistance(data15_i)
    print_resistance_values(data15_i)
    calc_resistance(data15_ii)
    print_resistance_values(data15_ii)

    draw_func(data15_i, data15_ii, title)

    # 20 V
    title = "DC supply 20V"
    print(title)

    data20_i = numpy.loadtxt("../DC_suppy_20_option_1.csv", delimiter=',')
    data20_ii = numpy.loadtxt("../DC_suppy_20_option_2.csv", delimiter=',')

    calc_resistance(data20_i)
    print_resistance_values(data20_i)
    calc_resistance(data20_ii)
    print_resistance_values(data20_ii)

    draw_func(data20_i, data20_ii, title)
    int_resistance.pop(0)
    int_resistance.pop(0)
    int_res = []
    int_res_err = []
    voltage = []
    voltage_err = []
    for data in int_resistance:
        int_res.append(data[0][0] * 1000)
        int_res_err.append(data[0][1] * 1000)
        voltage.append(data[1][0])
        voltage_err.append(data[1][1])

    print(int_res)
    plt.errorbar(voltage, int_res, yerr=int_res_err, linestyle=" ", marker="o")
    plt.show()

    option_1_voltages = []
    option_1_voltages_err = []
    for line in range(0, len(voltage), 2):
        option_1_voltages.append(voltage[line])
        option_1_voltages_err.append(voltage_err[line])

    print(option_1_voltages)
    print(option_1_voltages_err)

