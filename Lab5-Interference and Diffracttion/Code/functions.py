import matplotlib.pyplot as plt
import numpy
import pylab
from scipy.optimize import curve_fit
import numpy as np
from scipy.signal import find_peaks

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


def draw_data_and_curve(data, x_ax, y_ax, title, legend, function, amplitude):
    xdata, ydata = data_to_xy(data)
    xdata = numpy.array(xdata)
    # xdata = numpy.array([x / D for x in xdata])
    ydata = numpy.array(ydata)
    min_x = abs(min(xdata))
    max_I = abs(max(ydata))
    max_I_x = xdata[int(numpy.mean(numpy.argmax(ydata)))]
    popt, pcov = curve_fit(function, xdata, ydata, p0=[max_I, max_I_x, 0.02, 11])

    popt[0] = amplitude # fixing the amplitude

    curve_data = function(xdata, *popt)

    max_I_x_curve = xdata[int(numpy.mean(numpy.argmax(curve_data)))]

    xdata = numpy.array([x + abs(max_I_x_curve) for x in xdata])

    plt.errorbar(xdata, ydata, fmt=".", label="", markersize=1, elinewidth=0.2)
    plt.plot(xdata, curve_data)
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.legend(legend)
    plt.title(title)
    plt.show()



def crop_data(x_data, y_data, x_start, x_end):
    crop_x = []
    crop_y = []
    for i in range(len(x_data)):
        if x_start <= x_data[i] <= x_end:
            crop_x.append(x_data[i])
            crop_y.append(y_data[i])
    return crop_x, crop_y


def fit_double_slit_outline(data, x_start, x_end, prominence, width, function):
    xdata, ydata = data_to_xy(data)

    # xdata, ydata = crop_data(xdata, ydata, x_start, x_end)
    xdata = np.array(xdata)
    ydata = np.array(ydata)

    peak_index, _ = find_peaks(ydata, height=0, prominence=prominence, width=width) # x_peaks is ""ïndex"" of the 1d array that contains a peak
    peak_index = np.array(peak_index)

    x_peaks = []
    y_peaks = []
    for i in peak_index:
        x_peaks.append(xdata[i])
        y_peaks.append(ydata[i])

    plt.errorbar(xdata, ydata, fmt='.', markersize=1)
    plt.plot(x_peaks, y_peaks, "x")
    # plt.show()
    # curvefit the outline
    popt, pcov = curve_fit(function, x_peaks, y_peaks, maxfev=10000)
    curve_data = function(xdata, *popt)
    plt.plot(xdata, curve_data)

    plt.show()

    # return peaks, np.array(y[peaks])


def double_slit_intensity(theta, d, a, wavelength, I0, c, b):
    theta += b
    alpha = (np.pi * d / wavelength) * theta
    beta = (np.pi * a / wavelength) * theta
    intensity = I0 / (theta ** 2) * ((np.sin(alpha) / alpha) ** 2) * (np.cos(beta) ** 2) + c
    return intensity

def diffraction(x, I, p, c, b):
    return I * ((np.sin((b * x) - p)/((b * x) - p)) ** 2) + c

def eq(x, I, p, c, b, I_2, d, q ):
    return I * ((np.sin((b * x) - p)/((b * x) - p)) ** 2) * (I_2 * np.cos((d * x) - q)) ** 2 + c

def cos_2(x, I, w, p, c):
    return I * (numpy.cos((w * x + p)) ** 2) + c
