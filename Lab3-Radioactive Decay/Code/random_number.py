import scipy.stats as st
import radioactive_decay as rd
import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def fit_func(k, lamb):
    return st.poisson.pmf(k, lamb)


if __name__ == "__main__":
    fiesta_counts_raw = rd.get_counts_array(fileName="../fiesta20min3sec2024.txt")
    fiesta_back_ground = rd.get_counts_array("../background20min3sec2024.txt")

    fiesta_back_ground_mean = round(numpy.mean(fiesta_back_ground))

    fiesta_counts = numpy.array(
        [fiesta_counts_raw[i] - fiesta_back_ground_mean for i in range(len(fiesta_counts_raw))])

    fiesta_count_uncert = []
    for i in range(len(fiesta_counts_raw)):
        fiesta_count_uncert.append(math.sqrt(fiesta_counts_raw[i] + fiesta_back_ground[i]))
    fiesta_count_uncert = numpy.array(fiesta_count_uncert)
    # convert 20sec data to rates
    fiesta_count_rate = numpy.array([count / (20 * 60) for count in fiesta_counts])
    fiesta_count_rate_uncert = numpy.array([count / (20 * 60) for count in fiesta_count_uncert])
    mu = numpy.mean(fiesta_counts)
    x_data = numpy.array([i for i in range(len(fiesta_counts))])
    plt.hist(fiesta_counts, histtype="bar", edgecolor="black")
    plt.show()
    # Define the Poisson distribution parameter lambda
    lam = mu
    # Create an array of x values
    x = fiesta_counts
    # Create the Poisson probability mass function
    pmf = st.poisson.pmf(x, lam)
    # Create the plot
    plt.plot(x, pmf, 'bo', ms=8)
    plt.vlines(x, 0, pmf, colors='b', lw=5, label="Poisson Distribution")
    plt.title('Poisson Probability Mass Function')
    plt.xlabel('Count')
    plt.ylabel('Probability')

    # Gaussian
    mean = mu
    sd = round(math.sqrt(mu))

    n = st.norm.pdf(x, mean, sd)
    ind = numpy.argsort(x)
    x = x[ind]
    n = n[ind]
    plt.plot(x, n, label="Gaussian Distribution")
    plt.xlabel('Count')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()
