import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

def rise_equation(t, v_in, tau):
    return v_in * (1 - (math.e ** (-t / tau)))


def phi_rc(w, a):
    return numpy.arctan(-a / w)

def phi_rl(w, a):
    return numpy.arctan(w * a)

def z_mod_RC(w, R, C):
    return R ** 2 + (-1 / w * C)


if __name__ == '__main__':
    # RC CIRCUIT
    file1 = open("../experiment_3_RC_circuit.csv", 'r')
    lines = file1.readlines()
    lines.pop(0)
    rc_freq = []
    rc_phase = []
    rc_phase_err = []
    for line in lines:
        line = line.replace("\n", "")
        this_line = line.split(',')
        rc_freq.append(float(this_line[0]))
        rc_phase.append(float(this_line[1]) * numpy.pi/180)
        rc_phase_err.append(float(this_line[2]) * numpy.pi/180)

    rc_freq = numpy.array(rc_freq)
    rc_phase = numpy.array(rc_phase)
    rc_phase_err = numpy.array(rc_phase_err)

    plt.errorbar(rc_freq, rc_phase, yerr=rc_phase_err, fmt=".", label="RC")

    popt, pcov = curve_fit(phi_rc, xdata=rc_freq, ydata=rc_phase, sigma=rc_phase_err, p0=[1990.04975124])
    print(popt)
    rc_phase_fit_data = phi_rc(rc_freq, popt[0])
    plt.plot(rc_freq, rc_phase_fit_data)

    #
    # LR circuit
    file2 = open("../experiment3_LR_circuit.csv")
    lines = file2.readlines()
    lines.pop(0)
    lr_freq = []
    lr_phase = []
    lr_phase_err = []
    for line in lines:
        line.replace('\n', '')
        this_line = line.split(',')
        lr_freq.append(float(this_line[0]))
        lr_phase.append(float(this_line[1])*numpy.pi/180)
        lr_phase_err.append(float(this_line[2]))

    lr_freq = numpy.array(lr_freq)
    lr_phase = numpy.array(lr_phase)
    lr_phase_err = numpy.array(lr_phase_err)

    plt.errorbar(lr_freq, lr_phase, yerr=lr_phase_err, fmt=".", label="LR")

    popt, pcov = curve_fit(phi_rl, xdata=lr_freq, ydata=lr_phase, sigma=lr_phase_err)
    print(popt)
    rl_phase_fit_data = phi_rl(lr_freq, popt[0])
    plt.plot(lr_freq, rl_phase_fit_data)

    plt.legend(loc="upper right")
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Phase Angle (radians)")
    plt.axhline(y=0)
    plt.show()

    # residual rc_freq
    measured_data = rc_phase
    calculated_data = rc_phase_fit_data
    x_axis_data = rc_freq
    plot_residual(measured_data, calculated_data, x_axis_data, 0, "RC Phase angle Residual", "Frequency (kHz)", "Phase Angle (Degree)")
    print("RC impedance chi_r2: ",reduced_x_r2(len(measured_data), 1, measured_data, calculated_data, rc_phase_err))

    measured_data = lr_phase #
    calculated_data = rl_phase_fit_data
    x_axis_data = lr_freq
    plot_residual(measured_data, calculated_data, x_axis_data, 0, "LR Phase angle Residual", "Frequency (kHz)", "Phase Angle (Degree)")
    print("LR impedance chi_r2: ", reduced_x_r2(len(measured_data), 1, measured_data, calculated_data, lr_phase_err))
    # # LR on top, trippy.

