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
    draw_curve(-3.265, -2.046, time_data, voltage_data, RC_eqn_V_c_up)
    # # #curves
    draw_curve(-2.0466, -0.689, time_data, voltage_data, RC_eqn_V_c)
    draw_curve(-0.689, 0.498, time_data, voltage_data, RC_eqn_V_c_up)
    # # #curves 3 -0.9,-0.01
    draw_curve(0.4982, 1.80, time_data, voltage_data, RC_eqn_V_c)
    draw_curve(1.8, 3.4, time_data, voltage_data, RC_eqn_V_c_up)
    # # # curves 4
    draw_curve(3.41, 4.599, time_data, voltage_data, RC_eqn_V_c)



    plt.show()



    # Part 2

    #procurement 1
    ################
    """draw_data("RC_circuit_resistor_ex2.csv", "RC resistor ex2", "ex")
    """
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    print()
    draw_data("RC_extra_data_resistor.csv", "RC resistor ex2", "time", "voltage", "ex", 0)
    time_data_1, voltage_data_1 = data_to_xy("RC_extra_data_resistor.csv")
    draw_curve(0.000595, 0.00099, time_data_1, voltage_data_1, RC_eqn_V_r_down)
    plt.show()
    print()
    ##################################

    #procurement 2
    draw_data("RL_circuit_resistor_ex2.csv", "RL resistor ex2","time", "voltage", "ex", 0)
    time_data_2, voltage_data_2 = data_to_xy("RL_circuit_resistor_ex2.csv")

    draw_curve(-0.0026, -0.00213, time_data_2, voltage_data_2, RL_eqn_V_r)
    draw_curve(-0.00199, -0.00156, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(-0.0015, -0.00104, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    plt.show()

    # procurement 3
    draw_data("LC_circuit_capacitor_ex2.csv", "LC capacitor ex2", "time", "voltage", "ex", 0)
    time_data_3, voltage_data_3 = data_to_xy("LC_circuit_capacitor_ex2.csv")

    draw_curve_3(-0.0023, -0.0014, time_data_3, voltage_data_3,  LC_eqn_V_c)
    draw_curve_3(-0.00135, -0.000357, time_data_3, voltage_data_3,  LC_eqn_V_c)
    draw_curve_3(-0.000355, 0.000627, time_data_3, voltage_data_3,  LC_eqn_V_c)
    draw_curve_3(0.000656, 0.00165, time_data_3, voltage_data_3,  LC_eqn_V_c)
    draw_curve_3(0.00166, 0.0025, time_data_3, voltage_data_3,  LC_eqn_V_c)
    plt.show()



    draw_data("LC_circuit_inductor_ex2.csv", "LC inductor ex2", "time", "voltage","ex", 0)
    time_data_3, voltage_data_3 = data_to_xy("LC_circuit_inductor_ex2.csv")
    draw_curve_3(-0.002496, -0.0020689, time_data_3, voltage_data_3,  LC_eqn_V_l)
    draw_curve_3(-0.00199, -0.00152, time_data_3, voltage_data_3,  LC_eqn_V_l)
    draw_curve_3(-0.001499, -0.00102, time_data_3, voltage_data_3,  LC_eqn_V_l)
    
    plt.show()





    # part 3
    draw_data("experiment_3_RC_circuit.csv", "RC AC circuit","frequency", "impedance", "ex", 0)

    plt.show()
    draw_data("experiment3_LR_circuit.csv", "LR AC circuit","", "", "ex", 0)
    plt.show()
