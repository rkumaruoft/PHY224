import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    xdata, ydata = data_to_xy("../Double Slit -0.04-0.25- Data1.txt")

    D = 50.6
    wavelength = 515 * (10 ** -9)
    min_x = abs(min(xdata))
    max_I = abs(max(ydata))
    xdata = numpy.array([x + min_x for x in xdata])
    xdata = numpy.array(xdata)
    ydata = numpy.array(ydata)
    max_I_x = xdata[int(numpy.mean(numpy.argmax(ydata)))]

    x_data_crop = []
    y_data_crop = []
    for index in range(len(xdata)):
        if 0.0514998 <= xdata[index] <= 0.065224:
            x_data_crop.append(xdata[index] / D)
            y_data_crop.append(ydata[index])

    for i in range(len(x_data_crop)):
        print(x_data_crop[i], ",", y_data_crop[i])

    min_x = abs(min(x_data_crop))
    max_I = abs(max(y_data_crop))
    xdata = numpy.array(x_data_crop)
    ydata = numpy.array(y_data_crop)

    plt.errorbar(xdata, ydata, fmt=".", label="", markersize=1, elinewidth=0.2)
    # popt, pcov = curve_fit(diffraction, xdata, ydata, p0=[max_I, 0.11, 0, 10], maxfev=1000000)

    popt, pcov = curve_fit(double_slit_intensity, xdata, ydata,
                           p0=[0.25 * (10 ** -3), 0.04 * (10 ** -3), wavelength, max_I])
    curve_data = double_slit_intensity(xdata, *popt)
    plt.plot(xdata, curve_data)
    plt.xlabel("Location (m)")
    plt.ylabel("Intensity")
    plt.axhline(y=0)
    plt.legend()
    plt.show()
