import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *


def rise_equation(t, v_in, tau):
    return v_in * (1 - (math.e ** (-t / tau)))


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
        rc_phase.append(float(this_line[1]))
        rc_phase_err.append(float(this_line[2]))

    rc_freq = numpy.array(rc_freq)
    rc_phase = numpy.array(rc_phase)
    rc_phase_err = numpy.array(rc_phase_err)

    min_phase = abs(min(rc_phase))
    rc_phase_scaled = numpy.array([p + min_phase for p in rc_phase])
    plt.errorbar(rc_freq, rc_phase, yerr=rc_phase_err, fmt=".", label="RC")

    popt, pcov = curve_fit(rise_equation, xdata=rc_freq, ydata=rc_phase_scaled, sigma=rc_phase_err)
    fit_data = rise_equation(rc_freq, popt[0], popt[1])
    fit_data = numpy.array([f - min_phase for f in fit_data])
    plt.plot(rc_freq, fit_data)

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
        lr_phase.append(float(this_line[1]))
        lr_phase_err.append(float(this_line[2]))

    lr_freq = numpy.array(lr_freq)
    lr_phase = numpy.array(lr_phase)
    lr_phase_err = numpy.array(lr_phase_err)

    plt.errorbar(lr_freq, lr_phase, yerr=lr_phase_err, fmt=".", label="LR")

    popt, pcov = curve_fit(rise_equation, xdata=lr_freq, ydata=lr_phase, sigma=lr_phase_err)
    fit_data = rise_equation(lr_freq, popt[0], popt[1])
    plt.plot(lr_freq, fit_data)

    plt.legend(loc="upper right")
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Phase Angle (degrees)")
    plt.axhline(y=0)
    plt.show()
