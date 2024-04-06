import math

import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':

    xdata, ydata = data_to_xy("../More Data/Double_slit_0.04_0.50.txt")
    D = 0.706
    wavelength = 515 * (10 ** -9)

    min_x = abs(min(xdata))
    max_I = abs(max(ydata))
    min_I = abs(min(ydata))
    xdata = numpy.array([x + min_x for x in xdata])
    xdata = numpy.array(xdata)
    ydata = numpy.array(ydata)
    max_I_x = xdata[int(numpy.mean(numpy.argmax(ydata)))]
    x_data_crop = []
    y_data_crop = []
    for index in range(len(xdata)):
        if 0.055 <= xdata[index] <= 0.071:
            x_data_crop.append(xdata[index])
            y_data_crop.append(ydata[index])
    min_x = abs(min(x_data_crop))
    max_I = abs(max(y_data_crop))
    xdata = numpy.array(x_data_crop)
    ydata = numpy.array(y_data_crop)
    plt.errorbar(xdata, ydata, fmt=".", label="Sensor Data", markersize=1, elinewidth=0.2, yerr=y_uncert)

    popt, pcov = curve_fit(cos_2, xdata, ydata, p0=[max_I, (numpy.pi * 0.00050 / (wavelength * D)), 0, -0.01])
    cos_2_data = cos_2(xdata, max_I, popt[1], popt[2], -0.01)
    plt.plot(xdata, cos_2_data, alpha=0.2, label="Interference Curve")

    print(popt[1] * wavelength * D / numpy.pi, math.sqrt(pcov[1][1]) * wavelength * D / numpy.pi)

    plt.xlabel("Location (meters)")
    plt.ylabel("Intensity (Volts)")

    # curve for diffraction pattern
    popt, pcov = curve_fit(diffraction, xdata, ydata, p0=[max_I, max_I_x, 0.04, 10])

    popt[0] = 0.085  # fixing the amplitude

    curve_data = diffraction(xdata, *popt)
    plt.plot(xdata, curve_data, label="Diffraction Curve")

    wavelength = 515 * (10 ** -9)
    error_slitwidth = numpy.sqrt(pcov[3][3]) * wavelength / numpy.pi * D
    slit_width = popt[3] * wavelength / numpy.pi * D
    print(slit_width, error_slitwidth)

    """residual graph"""
    # find the peaks
    peak_index, _ = find_peaks(ydata, height=0, prominence=0.01,
                               width=None)  # x_peaks is ""ïndex"" of the 1d array that contains a peak
    peak_index = np.array(peak_index)

    x_peaks = []
    y_peaks = []
    for i in peak_index:
        x_peaks.append(xdata[i])
        y_peaks.append(ydata[i])

    plt.legend()
    plt.savefig("Pics/double_slit_0.04_0.50.png", dpi=250)

    plt.show()
    # Calculate the x residual of the peaks
    x_peaks = np.array(x_peaks)
    curve_data_peaks = diffraction(x_peaks, *popt)

    residuals = []
    for l in range(len(x_peaks)):
        residuals.append(y_peaks[l] - curve_data_peaks[l])

    plt.errorbar(x_peaks, residuals, yerr=y_uncert, fmt=".", markersize=1, elinewidth=0.4, alpha=1,
                 label="Residual data")
    plt.xlabel("Sensor location (Meters)") 
    plt.ylabel("Intensity (Volts)")
    plt.axhline(y=0)
    plt.legend()
    plt.savefig("Pics/double_slit_0.04_0.50_residuals.png", dpi=250)
    plt.show()

    """chi_r^2 (of peak values, outline only)"""
    summ = 0
    N = len(x_peaks)
    for i in range(N):
        summ += ((y_peaks[i] - curve_data_peaks[i]) ** 2) / (y_uncert ** 2)
    chi_r = summ / (N - 4)
    print("chi_r^2 value: ", chi_r)
