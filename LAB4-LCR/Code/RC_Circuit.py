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
    means = []
    means.append( draw_curve(-4.63, -3.265, time_data, voltage_data, RC_eqn_V_c) )
    means.append( draw_curve(-3.265, -2.046, time_data, voltage_data, RC_eqn_V_c_up) )
    # # #curves
    means.append( draw_curve(-2.0466, -0.689, time_data, voltage_data, RC_eqn_V_c) )
    means.append( draw_curve(-0.689, 0.498, time_data, voltage_data, RC_eqn_V_c_up) )
    # # #curves 3
    means.append( draw_curve(0.4982, 1.80, time_data, voltage_data, RC_eqn_V_c) )
    means.append( draw_curve(1.8, 3.4, time_data, voltage_data, RC_eqn_V_c_up) )
    # # # curves 4
    means.append( draw_curve(3.41, 4.599, time_data, voltage_data, RC_eqn_V_c) )
    plt.show()

    v_mean = 0
    v_errors = 0
    tau_mean = 0
    tau_errors = 0
    for i in means:
        v_mean += i[0]
        v_errors += (i[1])**2
        tau_mean += i[2]
        tau_errors += (i[3])**2
    v_mean = v_mean / len(means)
    tau_mean = tau_mean / len(means)
    print("mean of v_0", v_mean)
    print("standard error of v_0_mean", 1/len(means) * np.sqrt(v_errors)) # uncertainty propagation
    print("mean of tau", tau_mean)
    print("error of tau", 1/len(means)* np.sqrt(tau_errors))

    # Part 2

    #procurement 1 RC
    ################
    """draw_data("RC_circuit_resistor_ex2.csv", "RC resistor ex2", "ex")
    """
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    print()

    draw_data("RC_extra_data_resistor.csv", "RC resistor ex2", "time", "voltage", "ex", 0)
    time_data_1, voltage_data_1 = data_to_xy("RC_extra_data_resistor.csv")
    means = []
    means.append(draw_curve(-0.002499, -0.002004, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(-0.001997, -0.001498, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(-0.001498, -0.001003, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(-0.001, -0.000505, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(-0.000497, -0.000006, time_data_1, voltage_data_1, RC_eqn_V_r))

    means.append(draw_curve(0.000002, 0.00049, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(0.000595, 0.00099, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(0.000998, 0.0015, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(0.0015, 0.001998, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append(draw_curve(0.002002, 0.002493, time_data_1, voltage_data_1, RC_eqn_V_r))
    plt.show()
    print()

    # in this case the acutal tau is 1/tau, since the curvefit eqn only worked with *
    v_mean = 0
    v_errors = 0
    tau_mean = 0
    tau_errors = 0
    for i in means:
        v_mean += i[0]
        v_errors += (i[1])**2
        tau_mean += 1 / i[2] # changes
        tau_errors += (1 / i[3])**2

    v_mean = v_mean / len(means)
    tau_mean = tau_mean / len(means)
    print("mean of v_0", v_mean)
    print("standard error of v_0_mean", 1/len(means) * np.sqrt(v_errors)) # uncertainty propagation
    print("mean of tau", tau_mean)
    print("error of tau", 1/len(means) * np.sqrt(tau_errors))
    ##################################

    #procurement 2 RL
    """
    draw_data("RL_circuit_resistor_ex2.csv", "RL resistor ex2","time", "voltage", "ex", 0)
    time_data_2, voltage_data_2 = data_to_xy("RL_circuit_resistor_ex2.csv")

    draw_curve(-0.0026, -0.00213, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(-0.00199, -0.00156, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(-0.0015, -0.00104, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(-0.000999, -0.00055, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(-0.0005, -0.0000016, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(0.000001, 0.000464, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(0.000505, 0.000989, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(0.001, 0.00147, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(0.001506, 0.001971, time_data_2, voltage_data_2, RL_eqn_V_r_up)
    draw_curve(0.002, 0.00249, time_data_2, voltage_data_2, RL_eqn_V_r_up)"""

    plt.show()

    # procurement 3 LC in another file






    # part 3
    print()
    draw_data("experiment_3_RC_circuit.csv", "RC AC circuit","frequency", "impedance", "ex", 0)
    z_data, w_data = data_to_xy("experiment_3_RC_circuit.csv")
    draw_curve(1.96, 90, z_data, w_data,  Z_RC_eqn)
    plt.show()
    draw_data("experiment3_LR_circuit.csv", "LR AC circuit","", "", "ex", 0)
    plt.show()
