import matplotlib.pyplot as plt
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
        line.replace("\t", '') # replace white space
        line.replace("\n", '') # replace line jump
        this_line = [float(num) for num in line.split()]
        x_data.append(this_line[0])
        y_data.append(this_line[1])
    return x_data, y_data


def draw_data(data, x_ax, y_ax, title, legend):
    x_data, y_data = data_to_xy(data)
    x_data, y_data = crop_data(x_data, y_data, 1, 1) ################# delete this to draw the uncropped data
    x_data, y_data = rescale_data(x_data, y_data, 1000, 1000)

    plt.errorbar(x_data, y_data, fmt=".", label="", markersize=1, elinewidth=0.2)
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.legend(legend, loc="upper left")
    plt.title(title)
    plt.show()


def draw_data_and_curve(data, x_ax, y_ax, title, legend, function):
    x_data, y_data = data_to_xy(data)
    xdata, ydata = crop_data(x_data, y_data, 1, 1)##################### delete this to draw the uncropped data
    print(x_data[0])

    xdata, ydata = rescale_data(xdata, ydata, 1000, 1000)
    print(xdata[0])

    popt, pcov = curve_fit(function, xdata, ydata,
                           maxfev=1000)
    print("popt", popt)
    curve_data = function(xdata, popt[0])
    print("popt", popt)
    plt.plot(xdata, curve_data)
    #plt.show()
    draw_data(data, x_ax, y_ax, title, legend) # the show() function is in here


def crop_data(x_data, y_data, x_start, x_end):
    crop_x = []
    crop_y = []
    for i in range(len(x_data)):
        if -0.09 <= x_data[i] <= -0.04:
            crop_x.append(x_data[i])
            crop_y.append(y_data[i])
    return crop_x, crop_y


def rescale_data(x_data, y_data, x_scale, y_scale):
    new_x = x_data * x_scale
    new_y = y_data * y_scale
    return new_x, new_y


def diffraction(x, I):
    return I * ((np.sin(x)/ x ) ** 2)
