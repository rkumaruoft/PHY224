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

    plt.errorbar(time_data, voltage_data, fmt=".", label="Capacitor Data", )
    plt.xlabel("Time (mili Seconds")
    plt.ylabel("Voltage (V)")
    plt.legend(["Capacitor data","Curvefit"])
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
    v_error = 0
    tau_mean = 0
    tau_error = 0
    for i in means:
        v_mean += i[0]
        v_error += i[1] ** 2
        tau_mean += i[2]
        tau_error += i[3]**2
    print("mean of v_0", v_mean / len(means))
    print("error of v_0 mean", 1 / len(means) * np.sqrt(v_error))
    print("mean of tau", tau_mean / len(means))
    print("error of tau mean", 1 / len(means) * np.sqrt(tau_error))


    # residual
    # fall
    measured_data = []
    x_axis_data = []
    for n in range(len(time_data)):
        if -4.63 <= time_data[n] <= -3.265:
            measured_data.append(voltage_data[n])
            x_axis_data.append(time_data[n])
    x_axis_data = np.array([(line - (-4.63)) for line in x_axis_data])# shift to start from 0
    #print(measured_data)
    print()
    #print(x_axis_data)
    calculated_data = RC_eqn_V_c(x_axis_data, means[0][0], means[0][2])# for one curve

    plot_residual(measured_data, calculated_data, x_axis_data, 0.05, "RC Capacitor voltage Residual", "Time (milli-Sec)", "Voltage (V)")
    plt.show()

    # rise
    measured_data2, calculated_data2, x_axis_data2 = residual_stuff(time_data,
                                                                    voltage_data, means[1][0], means[1][2], -3.265, -2.046, RC_eqn_V_c_up)

    plot_residual(measured_data2, calculated_data2, x_axis_data2, 0.05, "RC Capacitor voltage Residual (rise)", "Time (milli-Sec)", "Voltage (V)")
    plt.show()

    # chi_r^2
    print("chi^2 of fall: ", reduced_x_r2_abs(len(measured_data), 2, measured_data, calculated_data, 0.05))
    # first fall
    print("chi^2 of rise: ", reduced_x_r2_abs(len(measured_data2), 2, measured_data2, calculated_data2, 0.05))


    # Part 2

    #procurement 1 RC
    ################
    """draw_data("RC_circuit_resistor_ex2.csv", "RC resistor ex2", "ex")
    """
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    print()
    draw_data("RC_extra_data_resistor.csv", "RC resistor ex2", "Time (ms)", "Voltage (V)", ["Resistor data", "curve_fit"], 0)
    time_data_1, voltage_data_1 = data_to_xy("RC_extra_data_resistor.csv")

    means = []

    means.append( draw_curve(-0.002499, -0.002004, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(-0.001997, -0.001501, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(-0.001498, -0.001003, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(-0.001, -0.000505, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(-0.000497, -0.000006, time_data_1, voltage_data_1, RC_eqn_V_r))

    means.append( draw_curve(0.000002, 0.00049, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(0.000595, 0.00099, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(0.000998, 0.0015, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(0.0015, 0.001998, time_data_1, voltage_data_1, RC_eqn_V_r))
    means.append( draw_curve(0.002002, 0.002493, time_data_1, voltage_data_1, RC_eqn_V_r))
    plt.show()
    print()



    v_mean = 0
    v_error = 0
    tau_mean = 0
    tau_error = 0
    for i in means:
        v_mean += i[0]
        v_error += i[1] ** 2 # changes here, tau is inverse, since the curve fit only works with *
        tau_mean += 1 / i[2]
        tau_error += (1 / i[3])**2
    print("mean of v_0", v_mean / len(means))
    print("error of v_0 mean", 1 / len(means) * np.sqrt(v_error))
    print("mean of tau", tau_mean / len(means))
    print("error of tau mean", 1 / len(means) * np.sqrt(tau_error))
    ##################################

    """ Residuals"""

    measured_data1, calculated_data1, x_axis_data1 = residual_stuff(time_data_1,
                                                                 voltage_data_1, means[0][0], means[0][2], -0.002499, -0.002004, RC_eqn_V_r)
    measured_data2, calculated_data2, x_axis_data2 = residual_stuff(time_data_1,
                                                                    voltage_data_1, means[1][0], means[1][2], -0.001997, -0.001501, RC_eqn_V_r)

    plot_residual(measured_data1, calculated_data1, x_axis_data1, 0.05, "RC resistor voltage Residual (rise)", "Time (milli-Sec)", "Voltage (V)")
    plt.show()

    plot_residual(measured_data2, calculated_data2, x_axis_data2, 0.05, "RC resistor voltage Residual (drop)", "Time (milli-Sec)", "Voltage (V)")
    plt.show()

    """ chi_r^2"""
    # for the first rise
    print("chi^2 of rise: ", reduced_x_r2_abs(len(measured_data1), 2, measured_data1, calculated_data1, 0.05))
    # first fall
    print("chi^2 of fall: ", reduced_x_r2_abs(len(measured_data2), 2, measured_data2, calculated_data2, 0.05))
