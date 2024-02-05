import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit


def terminal_voltage_func(current, r_internal, v_inf):
    return v_inf - (r_internal * current)


def loaf_file_data(voltage_arr, current_arr, voltage_uncert, current_uncert, filename):
    data = numpy.loadtxt(filename)


if __name__ == "__main__":
    # for cell battery

    data = numpy.loadtxt()
