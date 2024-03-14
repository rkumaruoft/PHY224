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


def draw_data(data, title, xlabel, ylabel, legend, uncertainty):
    x_data, y_data = data_to_xy(data)

    plt.errorbar(x_data, y_data, yerr=uncertainty, fmt=".", label="Resistance Data")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
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

    this_arr_x_1 = np.array([(line - x_start) for line in this_arr_x])  #

    popt, pcov = curve_fit(function, xdata=this_arr_x_1, ydata=this_arr_y,
                           maxfev=10000)
    curve_data = function(this_arr_x_1, popt[0], popt[1])
    plt.plot(this_arr_x, curve_data)
    print(popt[0])
    print(popt[1])
    return popt[0], popt[1]


def draw_curve_3(x_start, x_end, x_data, y_data, function):
    this_arr_x = []
    this_arr_y = []
    uncert = []
    for i in range(len(x_data)):
        if x_start <= x_data[i] <= x_end:
            this_arr_x.append(x_data[i])
            this_arr_y.append(y_data[i])
            uncert.append(0.001)
    this_arr_x = np.array(this_arr_x)
    this_arr_y = np.array(this_arr_y)

    this_arr_x_1 = np.array([(line - x_start) for line in this_arr_x])  # np.array this

    popt, pcov = curve_fit(function, xdata=this_arr_x_1, ydata=this_arr_y, sigma=uncert,
                           maxfev=10000)
    curve_data = function(this_arr_x_1, popt[0], popt[1], popt[2])
    plt.plot(this_arr_x, curve_data)
    print(popt[0])
    print(popt[1])
    print(popt[2])


# Part 1 RC circuit
def RC_eqn_V_c(t, v_o, tau):
    # time const = 1/RC
    # b=RC
    # v_in=1.468 volts
    return v_o * (np.exp(-t / tau))


def RC_eqn_V_c_up(t, v_0, tau):
    # time const = 1/RC
    # b=RC
    # v_in=1.468 volts
    return v_0 * (1 - (np.exp(-t / tau)))


# part 2 RC circuit
def RC_eqn_V_r(t, v_0, tau):
    # v_0=I_0 * R
    return -v_0 * (np.exp(-t * tau))


# RC_eqn_V_c_up(t, v_0, tau)

def RC_eqn_V_r_down(t, v_0, tau):
    return v_0 * (np.exp(-t * tau))


"""
def log_model(t, v_0, tau):
    return v_0 * (np.log(t / tau))"""


# Part 2 RL circuit
def RL_eqn_V_r(t, a, tau):
    # tau = 1/(R/L)
    # Resistance = 503 ohm
    # a= Resistance * V_0
    # probably R*V_o*math.e**(t/tau)
    return a * (np.exp(t * tau))


def RL_eqn_V_r_up(t, a, tau):
    return a * (1 - (np.exp(-t / tau)))


# part 2 LC circuit Equations
def LC_eqn_V_c(t, a, time_const, p):
    # time const = 1/sqrt(LC)
    return a * (np.sin(t * time_const + p))
    # using / tau does not fit.


def LC_eqn_V_l(t, a, time_const, p):
    return a * (1 - np.sin(t * time_const + p))


# for part 3
def Z_RL_eqn(om, l, r):
    return r + (l - (1 / om))


def Z_RC_eqn(om, c, r):
    return r - (1 / (om * c))


def reduced_x_r2(N, m, measured_data, model_data, uncertainties):
    summ = 0
    for i in range(N):
        summ += ((measured_data[i] - model_data[i]) ** 2) / (uncertainties[i] ** 2)
    return summ / (N - m)


def LC_equation(t, v_input, w, p):
    # time const = sqrt(LC)
    return v_input * (1 - np.sin((t * w * 1 / (2 * np.pi)) + p))


def RL_rise_equation(t, v_in, tau):
    return v_in * (1 - (math.e ** (-t / tau)))


def RL_fall_equation(t, v_in, r):
    return v_in * np.exp(-1 / r * t)
