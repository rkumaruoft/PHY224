import matplotlib as mat
import numpy
from functions import *

if __name__ == "__main__":
    data = numpy.loadtxt("../voltage-current-data-part1.csv", delimiter=',')
    main_func(data)
