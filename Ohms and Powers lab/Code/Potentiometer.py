import matplotlib as mat
import numpy
from functions import *

if __name__ == "__main__":
    data = numpy.loadtxt("../voltage_current_data_part2.csv", delimiter=',')
    main_func(data)
