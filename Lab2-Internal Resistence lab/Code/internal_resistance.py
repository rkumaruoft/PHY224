import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit


def terminal_voltage_func(current, r_internal, v_inf):
    return v_inf - (r_internal * current)


def loaf_file_data(voltage_arr, current_arr, voltage_uncert, current_uncert, filename):
    data = numpy.loadtxt(filename)
    return data


def draw_func(data1, data2, title):
    volt_data = make_data_array(data1)[0]
    curr_data = make_data_array(data1)[1]
    volt_uncert = make_data_array(data1)[2]
    curr_uncert = make_data_array(data1)[3]

    plt.scatter(curr_data, volt_data)
    plt.errorbar(curr_data, volt_data, xerr=curr_uncert, yerr=volt_uncert, fmt=".")
    # plotting the curve fit for data1
    plt.plot(curr_data,
             terminal_voltage_func(curr_data, calc_resistance(data1)[0], calc_resistance(data1)[1]))

    volt_data = make_data_array(data2)[0]
    curr_data = make_data_array(data2)[1]
    volt_uncert = make_data_array(data2)[2]
    curr_uncert = make_data_array(data2)[3]

    plt.scatter(curr_data, volt_data)
    plt.errorbar(curr_data, volt_data, xerr=curr_uncert, yerr=volt_uncert, fmt=".")
    # plotting the curve fit for data1
    plt.plot(curr_data,
             terminal_voltage_func(curr_data, calc_resistance(data2)[0], calc_resistance(data2)[1]))

    plt.xlabel("Current")
    plt.ylabel("Voltage")
    plt.legend(["option 1", "curve fit 1", "option 2", "curve fit 2"])
    plt.title(title)
    plt.savefig('Log_Linear_Model.png', dpi=250)
    plt.show()


def draw_residual(data):
    # draw one residual plot
    i = 0


def print_chi_r(data,N, x_data, y_data, model,a,b):
    uncertainties=[]
    sum = 0
    for i in range(N):
        sum += (((y_data[i] - model(x_data[i], a, b)) ** 2) / (uncertainties[i] ** 2))
    chi_r = sum / (N - 2) # 2 parameters in our terminal voltage function
    print("chi_r")


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


def print_resistance_values(data):
    volt_data = make_data_array(data)[0]
    curr_data = make_data_array(data)[1]
    volt_uncert = make_data_array(data)[2]
    curr_uncert = make_data_array(data)[3]
    popt, pcov = curve_fit(terminal_voltage_func, curr_data, volt_data,
                           sigma=volt_uncert, absolute_sigma=True)
    print("popt: ", popt)
    print("pcov: ", pcov)
    resistance_error = numpy.sqrt(numpy.diag(pcov))[0]

    v_terminal_error = numpy.sqrt(numpy.diag(pcov))[1]
    print("Error of internal resistance: ", resistance_error)
    print("Error of terminal voltage: ", v_terminal_error)
    print()
    print()


if __name__ == "__main__":
    # for cell battery
    # todo: TALK ABOUT THE OUTLIER POINT IN DATA1
    """ Part 1"""
    title="Cell battery"
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
    title="DC supply 6.5V"
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
    title="DC supply 10V"
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
    title="DC supply 15V"
    print(title)
    print()
    data15_i = numpy.loadtxt("../DC_suppy_15_option_1.csv", delimiter=',')
    data15_ii = numpy.loadtxt("../DC_suppy_15_option_2.csv", delimiter=',')

    calc_resistance(data15_i)
    print_resistance_values(data15_i)
    calc_resistance(data15_ii)
    print_resistance_values(data15_ii)

    draw_func(data15_i, data15_ii,title)

    # 20 V
    title="DC supply 20V"
    print(title)

    data20_i = numpy.loadtxt("../DC_suppy_20_option_1.csv", delimiter=',')
    data20_ii = numpy.loadtxt("../DC_suppy_20_option_2.csv", delimiter=',')

    calc_resistance(data20_i)
    print_resistance_values(data20_i)
    calc_resistance(data20_ii)
    print_resistance_values(data20_ii)

    draw_func(data20_i, data20_ii, title)
