import matplotlib as mat
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':
    draw_data_and_curve("Single Slit - 0.02- Data.txt", "x", "y", "", "Data", diffraction)
