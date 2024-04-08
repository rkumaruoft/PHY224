import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *
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


def x_r2_metric_2(N, m, measured_data, calculated_data, uncertainties):
    sum = 0
    for i in range(N):
        sum += ((measured_data[i] - calculated_data[i]) ** 2) / (uncertainties[i] ** 2)
    return sum / (N - m)


def draw_residual(measured_data, calculated_data, x_axis_data, measured_uncert):
    residuals = []
    for line in range(len(measured_data)):
        residuals.append(measured_data[line] - calculated_data[line])
    plt.errorbar(x_axis_data, residuals, yerr=measured_uncert, fmt=".")
    plt.xlabel("Current")
    plt.ylabel("Voltage")
    plt.title("Change in g v.s change in R Residual plot")
    plt.axhline(y=0)
    plt.figure(figsize=(10, 6))
    # plt.savefig('.png', dpi=250)
    plt.show()


if __name__ == '__main__':
    #  hastag the label of the csv data file.

    data2 = numpy.loadtxt("radius of earth-dat2.csv", delimiter=',')

    x_data, y_data, x_uncert, y_uncert = make_data_array(data2)

    x_data = x_data * 0.1055 # convert to m/s^2

    popt, pcov = curve_fit(model, x_data, y_data)

    print("change in R/change in G: ", popt[0])

    curve_data = model(x_data, *popt)

    # draw

    plt.errorbar(x_data, y_data, fmt=".", label="", markersize=1, elinewidth=0.2, yerr=y_uncert[0])

    plt.plot(x_data, curve_data)
    plt.xlabel("Delta g")
    plt.ylabel("Delta R")
    plt.legend(["Curve-fit", "Data"])
    plt.title("G vs R")
    plt.show()

    # residual and reduced Chi metric

    draw_residual(y_data, curve_data, x_data, y_uncert[0])

    print("Chi^2 metric: " + str( x_r2_metric_2(len(x_data), 1, y_data, curve_data, y_uncert) ) )


