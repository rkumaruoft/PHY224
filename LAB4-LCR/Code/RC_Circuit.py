import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':

    # RESISTOR DATA
    rc_resistance_data = read_file_data("../scope_1_resistence.csv")
    # time data is in seconds and voltage data is in Volts
    time_data = []
    voltage_data = []
    for line in rc_resistance_data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        time_data.append(this_line[0])
        voltage_data.append(this_line[1])

    plt.errorbar(time_data, voltage_data, fmt=".", label="Resistance Data")

    # CAPACITOR DATA
    rc_capacitor_data = read_file_data("../scope_2_capacitor.csv")
    time_data = []
    voltage_data = []
    for line in rc_capacitor_data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        time_data.append(this_line[0])
        voltage_data.append(this_line[1])

    plt.errorbar(time_data, voltage_data, fmt=".", label="Capacitor Data")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.legend()
    plt.show()
