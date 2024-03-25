import matplotlib.pyplot as plt
import numpy
import pylab
from scipy.optimize import curve_fit
import numpy as np
import math

"""Light Interference and diffraction lab"""


def read_file_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    return lines


def data_to_xy(data):
    data = read_file_data(data)
    x_data = []
    y_data = []
    for line in data:
        line.replace("\t", '')  # replace white space
        line.replace("\n", '')  # replace line jump
        this_line = [float(num) for num in line.split()]
        x_data.append(this_line[0])
        y_data.append(this_line[1])
    return x_data, y_data


def draw_data(data, x_ax, y_ax, title, legend):
    x_data, y_data = data_to_xy(data)
    # x_data, y_data = crop_data(x_data, y_data, 1, 1) ################# delete this to draw the uncropped data

    plt.errorbar(x_data, y_data, fmt=".", label="", markersize=1, elinewidth=0.2)
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.legend(legend, loc="upper left")
    plt.title(title)
    plt.show()


def draw_data_and_curve(data, x_ax, y_ax, title, legend, function):
    xdata, ydata = data_to_xy(data)
    popt, pcov = curve_fit(function, xdata, ydata)
    curve_data = function(xdata, popt[0], popt[1])
    plt.show()
    draw_data(data, x_ax, y_ax, title, legend)  # the show() function is in here


def crop_data(x_data, y_data, x_start, x_end):
    crop_x = []
    crop_y = []
    for i in range(len(x_data)):
        if -0.09 <= x_data[i] <= -0.04:
            crop_x.append(x_data[i])
            crop_y.append(y_data[i])
    return crop_x, crop_y


def diffraction(x, I, p, c, d):
    return I * ((np.sin((d * x) - p)/((d * x) - p)) ** 2) + c
