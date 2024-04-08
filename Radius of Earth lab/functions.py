import matplotlib.pyplot as plt
import numpy
import pylab
from scipy.optimize import curve_fit
import numpy as np
from scipy.signal import find_peaks


"""global functions only
"""
def read_data(data):
    file = open( data, 'r')
    lines = file.readlines()
    lines.pop(0) # remove the title
    return lines


def data_to_xy(data):
    data = read_data(data)
    x_data = []
    y_data = []
    x_uncert = []
    y_uncert = []
    for line in data:
        line.replace("\t", '')  # replace white space
        line.replace("\n", '')  # replace line jump
        this_line = [float(num) for num in line.split()]
        x_data.append(this_line[0])
        y_data.append(this_line[1])
        x_uncert.append(this_line[2])
        y_uncert.append(this_line[3])
    return x_data, y_data, x_uncert, y_uncert


def model(g, slope):
    # to fit our plot of delta_g by delta_r
    # slope = delta_r / delta_g
    # therefore R = -2g (delta_r / delta_g)
    return -2 * slope * g


