import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

def func(x, i):
    return np

if __name__ == '__main__':
    # single slit
    xdata, ydata = data_to_xy("../Single Slit - 0.02- Data.txt")
    xdata = numpy.array(xdata)
    ydata = numpy.array(ydata)
    min_x = abs(min(xdata))
    max_I = abs(max(ydata))
    # xdata = numpy.array([x + min_x for x in xdata])
    max_I_x = xdata[int(numpy.mean(numpy.argmax(ydata)))]
    plt.errorbar(xdata, ydata, fmt=".", label="", markersize=1, elinewidth=0.2)
    popt, pcov = curve_fit(diffraction, xdata, ydata, p0=[max_I, max_I_x, 0.02, 10])
    curve_data = diffraction(xdata, *popt)
    plt.plot(xdata, curve_data)
    plt.xlabel("Location (m)")
    plt.ylabel("Intensity)")
    plt.axhline(y=0)
    plt.legend()
    plt.show()




