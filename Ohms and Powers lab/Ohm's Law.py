import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func_ohm_law(x, r):
    return x / r


if __name__ == "__main__":
    data = numpy.loadtxt("part1_resistor_data.csv", delimiter=',')

    voltage_data = []
    current_data = []
    voltage_uncert = []
    current_uncert = []
    i = 0
    for line in data:
        voltage_data.append(line[0])
        current_data.append(line[1])
        voltage_uncert.append(line[2])
        current_uncert.append(line[3])
