import math
import matplotlib as mat
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit


def read_file_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    return lines


def data_to_xy(data):
    data = read_file_data("../" + data)
    # time data is in seconds
    x_data = []
    y_data = []
    for line in data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        x_data.append(this_line[0])
        y_data.append(this_line[1])
    return x_data, y_data


def draw_data(data, title, legend):
    x_data, y_data = data_to_xy(data)

    plt.errorbar(x_data, y_data, fmt=".", label="Resistance Data")
    plt.legend(legend)
    plt.title(title)


def draw_curve(x_start, x_end, x_data, y_data, function):
    this_arr_x = []
    this_arr_y = []
    for i in range(len(x_data)):
        if x_start <= x_data[i] <= x_end:
            this_arr_x.append(x_data[i])
            this_arr_y.append(y_data[i])
    this_arr_x = np.array(this_arr_x)
    this_arr_y = np.array(this_arr_y)

    this_arr_x_1 = np.array([(line - x_start) for line in this_arr_x])

    popt, pcov = curve_fit(function, xdata=this_arr_x_1, ydata=this_arr_y,
                           maxfev=10000)
    curve_data = function(this_arr_x_1, popt[0], popt[1])
    plt.plot(this_arr_x, curve_data)
    print(popt[0])
    print(popt[1])


def draw_curve_2(time_interval, y_data, function):
    this_arr_y = []
    for i in range(len(time_interval)):
        this_arr_y.append(y_data[i])
    this_arr_y = np.array(this_arr_y)

    popt, pcov = curve_fit(function, xdata=time_interval, ydata=this_arr_y,
                           maxfev=10000)
    curve_data = function(time_interval, popt[0], popt[1], popt[2])
    plt.plot(time_interval, curve_data)
    print(popt[0])
    print(popt[1])
    print(popt[2])


def RC_eqn_V_c(t, v_o, tau):
    # time const = 1/RC
    # b=RC
    # v_in=1.468 volts
    return v_o * (math.e ** (-t / tau))


def RC_eqn_V_c_up(t, v_0, tau):
    # time const = 1/RC
    # b=RC
    # v_in=1.468 volts
    return v_0 * (1 - (math.e ** (-t / tau)))


def RC_eqn_V_r(t, v_0, tau):
    return 1.468 - v_0 * (math.e ** (-t / tau))


def RL_eqn_V_r(t, a, time_const, b):
    # time const = R/L
    # Resistance = 503 ohm
    # a= Resistance * some_const
    # probably R*V_o*math.e**(t/tau)
    return a * (1 / 2) ** (t * time_const) + b * (1.4)


def LC_eqn_V_c(t, v_input, a, b, time_const):

    # time const = 1/sqrt(LC)
    return a * math.sin(-t * time_const) + b * math.cos(
        t * time_const) + v_input


def LC_eqn_V_l():
    return 1
