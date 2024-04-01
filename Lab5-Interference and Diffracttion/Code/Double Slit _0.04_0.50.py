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
    plt.errorbar(xdata, ydata, fmt=".", label="", markersize=1, elinewidth=0.2)

    popt, pcov = curve_fit(cos_2, xdata, ydata, p0=[max_I, (numpy.pi * 0.00050 / (wavelength * D)), 0, -0.01])
    cos_2_data = cos_2(xdata, max_I, popt[1], popt[2], -0.01)
    plt.plot(xdata, cos_2_data, alpha=0.2)

    print(popt[1]*wavelength*D/numpy.pi)


    plt.xlabel("Location")
    plt.ylabel("Intensity")
    plt.axhline(y=0)
    plt.legend()

    # curve for diffraction pattern
    popt, pcov = curve_fit(diffraction, xdata, ydata, p0=[max_I, max_I_x, 0.04, 10],
                           maxfev=100000)

    popt[0] = 0.085  # fixing the amplitude

    curve_data = diffraction(xdata, *popt)
    plt.plot(xdata, curve_data)


    wavelength = 515 * (10 ** -9)
    error_slitwidth = numpy.sqrt(pcov[3][3]) * wavelength / numpy.pi
    slit_width = popt[3] * wavelength/numpy.pi
    print(slit_width, error_slitwidth)
    plt.show()
