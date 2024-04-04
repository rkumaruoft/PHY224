import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    xdata, ydata = data_to_xy("../Uncertainty Data.txt")
    max_Y = max(ydata)
    min_y = min(ydata)

    uncertainty = max_Y - min_y
    print(uncertainty)