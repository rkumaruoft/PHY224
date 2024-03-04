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
    #curve 1
    draw_curve(-4.283, -3.438, time_data, voltage_data, RC_eqn_V_c)
    #curve 2
    draw_curve(-2.585, -1.7, time_data, voltage_data, RC_eqn_V_c)
    #curve 3
    draw_curve(-0.9,-0.01, time_data, voltage_data, RC_eqn_V_c)
    # curve 4
    draw_curve(0.75, 1.64, time_data, voltage_data, RC_eqn_V_c)
    # curve 5
    draw_curve(2.856, 3.77, time_data, voltage_data, RC_eqn_V_c)

    # time_data_intervals = []
    # an_interval = []
    # for i in range(len(time_data)):
    #     an_interval.append(time_data[i])
    #     if
    #     if voltage_data[i+1] - voltage_data[i] >0.8:
    #         time_data_intervals.append(an_interval)
    #         an_interval = []

    # for n in time_data_intervals:
    #     draw_curve_2(n, voltage_data)
    #



    plt.show()



    # draw_data_and_curves("RC_circuit_battery_resistor_ex1.csv", "RC resistor ex1",
                         #['TBD'], RC_function, [],False)

    # Part 2

    # draw_data("RC_circuit_capacitor_ex2.csv", "RC capacitor ex2", "ex")
    #curve 1
    # draw_curve()
    draw_data("RC_circuit_resistor_ex2.csv", "RC resistor ex2", "ex")
    time_data, voltage_data = data_to_xy("RC_circuit_resistor_ex2.csv")

    draw_curve(-0.0925, -0.074, time_data, voltage_data, RC_eqn_V_r)

    draw_curve(-0.0554, -0.0371, time_data, voltage_data, RC_eqn_V_r)

    draw_curve(-0.0554, -0.0371, time_data, voltage_data, RC_eqn_V_r)
    plt.show()
    #
    # draw_data("RL_circuit_inductor_ex2.csv", "RL inductor ex2", "ex")
    draw_data("RL_circuit_resistor_ex2.csv", "RL resistor ex2", "ex")
    plt.show()
    #
    draw_data("LC_circuit_capacitor_ex2.csv", "LC capacitor ex2", "ex")
    draw_data("LC_circuit_inductor_ex2.csv", "LC inductor ex2", "ex")
    plt.show()
