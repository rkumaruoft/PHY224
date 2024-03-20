import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
import numpy as np
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
        print(line)
        this_line = [float(num) for num in line.split()]
        x_data.append(this_line[0])
        y_data.append(this_line[1])
    return x_data, y_data


def draw_data(data, x_ax, y_ax, title, legend):
    x_data, y_data = data_to_xy(data)

    plt.errorbar(x_data, y_data, fmt=".", label="", markersize=1, elinewidth=0.2)
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.legend(legend, loc="upper left")
    plt.title(title)
    plt.show()


def draw_data_and_curve(data, x_ax, y_ax, title, legend, function):
    xdata, ydata = data_to_xy(data)
    popt, pcov = curve_fit(function, xdata, ydata,
                           maxfev=10000)
    curve_data = function(xdata, popt[0])
    plt.plot(xdata, curve_data)

    draw_data(data, x_ax, y_ax, title, legend) # the show() function is in here


def diffraction(phi,I_0):
    return I_0 * (np.sin(phi) / phi) ** 2
