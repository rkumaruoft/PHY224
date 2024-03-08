import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    # Part 1



    # # CAPACITOR DATA
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

    plt.axhline(y=0)

    # skip the exponential increase sections
    #curves 1
    draw_curve(-4.63, -3.265, time_data, voltage_data, RC_eqn_V_c)
    #
    # # #curves
    draw_curve(-2.0466, -0.689, time_data, voltage_data, RC_eqn_V_c)
    # #
    # # #curves 3 -0.9,-0.01
    draw_curve(0.4982, 1.80, time_data, voltage_data, RC_eqn_V_c)
    # #
    # # # curves 4
    draw_curve(0.75, 1.64, time_data, voltage_data, RC_eqn_V_c)
    # #
    # # # curves 5
    draw_curve(3.41, 4.599, time_data, voltage_data, RC_eqn_V_c)



    plt.show()



    # Part 2

    #curve 1
    # draw_data("RC_circuit_resistor_ex2.csv", "RC resistor ex2", "ex")
    # time_data, voltage_data = data_to_xy("RC_circuit_resistor_ex2.csv")
    #
    # draw_curve(-0.0925, -0.074, time_data, voltage_data, RC_eqn_V_r)
    # #draw_curve(-0.0739, -0.0555, time_data, voltage_data, RC_eqn_V_r)
    # draw_curve(-0.0554, -0.0371, time_data, voltage_data, RC_eqn_V_r)
    #
    # draw_curve(-0.0554, -0.0371, time_data, voltage_data, RC_eqn_V_r)
    #
    # draw_curve(-0.0185, -0.000058, time_data, voltage_data, RC_eqn_V_r)
    #
    # draw_curve(0.0185, 0.037, time_data, voltage_data, RC_eqn_V_r)
    #
    # draw_curve(0.0556, 0.0739, time_data, voltage_data, RC_eqn_V_r)
    # plt.show()
    # #
    # # draw_data("RL_circuit_inductor_ex2.csv", "RL inductor ex2", "ex")
    #
    # draw_data("RL_circuit_resistor_ex2.csv", "RL resistor ex2", "ex")
    # time_data, voltage_data = data_to_xy("RL_circuit_resistor_ex2.csv")
    #
    # draw_curve(-0.00249, -0.002, time_data, voltage_data, RL_eqn_V_r)
    # draw_curve(-0.002016, -0.00165, time_data, voltage_data, RL_eqn_V_r)
    # plt.show()
    # #
    draw_data("LC_circuit_capacitor_ex2.csv", "LC capacitor ex2", "ex")
    plt.show()

    draw_data("LC_circuit_inductor_ex2.csv", "LC inductor ex2", "ex")
    plt.show()
