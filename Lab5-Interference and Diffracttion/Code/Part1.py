import matplotlib as mat
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit
from functions import *

if __name__ == '__main__':


    draw_data_and_curve2("../Single Slit - 0.02- Data.txt", "x", "y", "Single slit 0.02", ["fit","Data"], diffraction)
    draw_data_and_curve2("../Single Slit - 0.04- Data1.txt", "x", "y", "Single slit 0.04", "Data", diffraction)
    draw_data_and_curve2("../Single Slit - 0.08- Data.txt", "x", "y", "Single slit 0.04", "Data", diffraction)

    draw_data_and_curve2("../Double Slit -0.04-0.25-Data2.txt", "x", "y", "Double slit 0.04-0.25", "Data", diffraction)
    draw_data_and_curve2("../Double Slit - 0.04 - 0.50 - Data.txt", "x", "y", "Double slit 0.04-0.25", "Data", diffraction)
    draw_data_and_curve2("../Double Slit - 0.08 - 0.25 - Data.txt", "x", "y", "Double slit 0.04-0.25", "Data", diffraction)
    draw_data_and_curve2("../Double Slit - 0.08 - 0.25 - Data2.txt", "x", "y", "Double slit 0.04-0.25", "Data", diffraction)
    draw_data_and_curve2("../Double Slit - 0.08 - 0.50 - Data2.txt", "x", "y", "Double slit 0.04-0.25", "Data", diffraction)
