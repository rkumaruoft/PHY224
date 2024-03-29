import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    # single slit

    D = 0.526
    xdata, ydata = data_to_xy("C:\Year2\Phy224\PythonCode\Lab5-Interference and Diffracttion\Single Slit - 0.04- Data2.txt")

    xdata = numpy.array(xdata)

    xdata = numpy.array([x / D for x in xdata])

    ydata = numpy.array(ydata)
    min_x = abs(min(xdata))
    max_I = abs(max(ydata))
    max_I_x = xdata[int(numpy.mean(numpy.argmax(ydata)))]
    popt, pcov = curve_fit(diffraction, xdata, ydata, p0=[max_I, max_I_x, 0.04, 10])
    curve_data = diffraction(xdata, *popt)
    print(popt)
    max_I_x_curve = xdata[int(numpy.mean(numpy.argmax(curve_data)))]
    xdata = numpy.array([x + abs(max_I_x_curve) for x in xdata])
    plt.errorbar(xdata, ydata, fmt=".", label="", markersize=1, elinewidth=0.2)
    plt.plot(xdata, curve_data)
    plt.xlabel("Location (theta)")
    plt.ylabel("Intensity)")
    plt.axhline(y=0)
    plt.title("0.04")
    wavelength = 515 * (10 ** -9)
    slit_width = popt[3] * wavelength/numpy.pi
    print(slit_width)
    plt.show()




    # maxILocation = int(numpy.mean(numpy.argmax(curve_data)))
    # max_I_x_curve = xdata[int(numpy.mean(numpy.argmax(curve_data)))]
    # print(max_I_x_curve)
    # width = 0
    # for i in range(maxILocation, len(xdata)):
    #     if ydata[i] <= 0:
    #         width = xdata[i]
    #         break
    # print(width)
    # wavelength = 515 * (10 ** -9)
    # slit_width = wavelength * D / width
    # print(slit_width)
    #
    # print(wavelength / (popt[3]))
