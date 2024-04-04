import math

import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    # single slit
    fig = plt.figure(0)
    fig.canvas.set_window_title('0.02')
    y_uncert = 0.021749999999999936
    D = 0.526
    xdata, ydata = data_to_xy("../More Data/Single_Slit_0.02.txt")
    xdata.reverse()
    ydata.reverse()
    xdata = numpy.array(xdata)
    # xdata = numpy.array([x / D for x in xdata])
    ydata = numpy.array(ydata)
    min_x = abs(min(xdata))
    max_I = abs(max(ydata))
    max_I_x = xdata[int(numpy.mean(numpy.argmax(ydata)))]
    popt, pcov = curve_fit(diffraction, xdata, ydata, p0=[max_I, max_I_x, 0.02, 10])
    curve_data = diffraction(xdata, *popt)
    print(popt)
    max_I_x_curve = xdata[int(numpy.mean(numpy.argmax(curve_data)))]
    xdata = numpy.array([x + abs(max_I_x_curve) for x in xdata])
    plt.errorbar(xdata, ydata, fmt=".", label="", markersize=1, elinewidth=0.2, yerr=y_uncert, alpha=0.1)
    plt.plot(xdata, curve_data)
    plt.xlabel("Location (meters)")
    plt.ylabel("Intensity (Volts)")
    plt.axhline(y=0)
    plt.legend()
    plt.show()

    wavelength = 515 * (10 ** -9)
    error_slitwidth = numpy.sqrt(pcov[3][3]) * wavelength/numpy.pi * D

    slit_width = popt[3] * wavelength/numpy.pi * D
    print(slit_width, error_slitwidth)

    """residual graph"""
    fig = plt.figure(0)
    fig.canvas.set_window_title('0.02 Residual')

    residuals = []
    for line in range(len(xdata)):
        residuals.append(ydata[line] - curve_data[line])
    plt.errorbar(xdata, residuals, yerr=y_uncert, fmt=".", markersize=1, elinewidth=0.1, alpha=0.1)
    plt.xlabel("Location (meters)")
    plt.ylabel("Intensity (Volts)")
    plt.axhline(y=0)

    plt.show()

    """chi_r"""
    summ = 0
    N = len(xdata)
    for i in range(N):
        summ += ((ydata[i] - curve_data[i]) ** 2) / (y_uncert ** 2)
    chi_r = summ / (N - 4)
    print("chi_r^2 value: ", chi_r)

    #Method 2
    first_min = 0.015558 - 0.0018354
    print(wavelength/math.sin(first_min) * D)


