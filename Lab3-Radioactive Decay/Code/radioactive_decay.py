import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit


def model_func_1(x, a, b):
    return (a * x) + b


def model_func_2(x, a, b):
    return b * (math.e ** (a * x))


def get_counts_array(fileName):
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    lines.pop(0)
    lines.pop(0)
    return numpy.array([float(line.split('\t')[1].replace('\n', '')) for line in lines])


if __name__ == "__main__":
    # Load Background file 3sec
    background_3_counts = get_counts_array('../background20min3sec2024.txt')

    # Load Background file 20 sec
    background_20_counts = get_counts_array('../background20min20sec2024.txt')
    background_20_mean = numpy.mean(background_20_counts)

    # Load 20sec data
    cesium_20_counts_raw = get_counts_array("../cesium20min20sec2024.txt")
    cesium_20_counts = numpy.array([cesium_20_counts_raw[i] - background_20_mean for i in range(len(cesium_20_counts_raw))])

    # Uncertainty for 20sec data
    cesium_20_uncert = []
    for i in range(len(cesium_20_counts_raw)):
        cesium_20_uncert.append(math.sqrt(cesium_20_counts_raw[i] + background_20_counts[i]))

    # convert 20sec data to rates
    cesium_20_rates = numpy.array([count/(20*60) for count in cesium_20_counts])
    cesium_20_rates_uncert = numpy.array([count/(20*60) for count in cesium_20_uncert])

    # 20sec x-data
    x_data = numpy.array([i * 20 for i in range(len(cesium_20_counts))])
    plt.errorbar(x_data, cesium_20_counts, yerr=cesium_20_uncert, fmt=".")

    cesium_20_counts_log = numpy.array([math.log(count, math.e) for count in cesium_20_counts])
    popt, pcov = curve_fit(model_func_1, xdata=x_data, ydata=cesium_20_counts_log,
                           sigma=cesium_20_uncert)
    model_func_1_data = model_func_1(x_data, popt[0], popt[1])
    antilog_model_data = []
    for data in model_func_1_data:
        antilog_model_data.append(math.exp(data))
    plt.plot(x_data, antilog_model_data)
    plt.xlabel("Time (sec)")
    plt.ylabel("Count")
    plt.show()
