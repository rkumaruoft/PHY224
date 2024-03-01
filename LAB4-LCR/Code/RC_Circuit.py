import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    # Part 1
    # RESISTOR DATA
    rc_resistance_data = read_file_data("../RC_circuit_battery_resistor_ex1.csv")
    # time data is in seconds and voltage data is in Volts
    time_data = []
    voltage_data = []
    for line in rc_resistance_data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        time_data.append(this_line[0])
        voltage_data.append(this_line[1])

    plt.errorbar(time_data, voltage_data, fmt=".", label="Resistance Data")
    plt.legend("Resistor")
    plt.title("Resistor")
    plt.show()
    # CAPACITOR DATA
    rc_capacitor_data = read_file_data("../RC_circuit_battery_capacitor_ex1.csv")
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
    plt.legend("Capacitor")
    plt.title("Capacitor")
    plt.show()

    # Part 2

    draw_data("RC_circuit_capacitor_ex2.csv", "RC capacitor ex2", "ex")
    draw_data("RC_circuit_resistor_ex2.csv", "RC resistor ex2", "ex")

    draw_data("RL_circuit_inductor_ex2.csv", "RL inductor ex2", "ex")
    draw_data("RL_circuit_resistor_ex2.csv", "RL resistor ex2", "ex")

    draw_data("LC_circuit_capacitor_ex2.csv", "LC capacitor ex2", "ex")
    draw_data("LC_circuit_inductor_ex2.csv", "LC inductor ex2", "ex")
