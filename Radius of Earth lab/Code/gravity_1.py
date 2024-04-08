import math

import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit


def get_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines.pop(0)  # remove the title

    delta_g = []
    delta_r = []
    delta_g_err = []
    delta_r_err = []
    for line in lines:
        this_line = line.split(",")
        delta_g.append(float(this_line[1]))
        delta_r.append(float(this_line[2]))
        delta_g_err.append(float(this_line[4]))
        delta_r_err.append(float(this_line[5]))

    for i in range(len(delta_g)):
        if i > 6:
            delta_g[i] = delta_g[i] - (3*0.10055)

    return numpy.array(delta_g), numpy.array(delta_r), numpy.array(delta_g_err), numpy.array(delta_r_err)


def model(r, R, c):
    # to fit our plot of delta_g by delta_r
    # slope = delta_r / delta_g
    # therefore R = -2g (delta_r / delta_g)
    return (((-2 * 9.804253) / R) * r) + c


def draw_residual(measured_data, calculated_data, x_axis_data, measured_uncert):
    residuals = []
    for line in range(len(measured_data)):
        residuals.append(measured_data[line] - calculated_data[line])
    plt.errorbar(x_axis_data, residuals, yerr=measured_uncert, fmt=".")
    plt.xlabel("$\\Delta$g")
    plt.ylabel("$\\Delta$R")
    plt.axhline(y=0)
    plt.show()


def x_r2_metric_2(N, m, measured_data, calculated_data, uncertainties):
    to_sum = 0
    for i in range(N):
        to_sum += ((measured_data[i] - calculated_data[i]) ** 2) / (uncertainties[i] ** 2)
    return to_sum / (N - m)


if __name__ == '__main__':
    delta_g, delta_r, delta_g_err, delta_r_err = get_data("../G-Data - 1.csv")

    plt.errorbar(delta_r, delta_g, xerr=delta_r_err, yerr=delta_g_err, fmt='.', label="Gravity meter Data")

    popt, pcov = curve_fit(model, xdata=delta_r, ydata=delta_g)

    fit_data = model(delta_r, *popt)
    print(popt)

    plt.plot(delta_r, fit_data, label="Best Fit Curve")

    slope_err = math.sqrt(pcov[0][0])
    const_err = math.sqrt(pcov[1][1]) * 10
    radius_err = slope_err + const_err
    print(popt[0] + (popt[1] * 10), radius_err)
    #
    plt.xlabel("$\\Delta$R")
    plt.ylabel("$\\Delta$g")
    plt.legend()
    plt.show()
    #
    draw_residual(delta_g, fit_data, delta_r, delta_g_err)
    #
    x_r = x_r2_metric_2(len(delta_g), 2, delta_g, fit_data, delta_g_err)
    print(x_r)
