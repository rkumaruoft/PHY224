import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def x_r2_metric(N, m, initial_position, speed, measured_distance_data, times, uncertainties):
    to_sum = []
    for i in range(N):
        to_sum.append(((measured_distance_data[i] - motion_equation(times[i], initial_position, speed, -9.8/7)) ** 2)
                      / (uncertainties[i] ** 2))
    return sum(to_sum) / (N - m)

def motion_equation(x, initial_position, velocity, acceleration):
    return initial_position + (velocity * x) + (0.5 * acceleration * (x ** 2))


if __name__ == '__main__':
    data = numpy.loadtxt("feather.csv", delimiter=",")
    xpoints = []
    ypoints = []
    uncertainties = []
    i = 0
    for line in data:
        xpoints.append(line[0])
        ypoints.append(line[1])
        uncertainties.append(line[2])
        i += 1

    xpoints = numpy.array(xpoints)
    ypoints = numpy.array(ypoints)
    uncertainties = numpy.array(uncertainties)

    # curve fit
    popt, pcov = curve_fit(motion_equation, xpoints, ypoints)
    plt.errorbar(xpoints, ypoints, yerr=uncertainties, fmt='.', label="Data")
    print(popt)
    fit_0 = popt[0]
    fit_1 = popt[1]
    fit_2 = popt[2]
    print("Initial Position: " + str(fit_0) + "\nInitial Velocity: " + str(fit_1) + "\nAcceleration: " + str(fit_2))

    fit_data = motion_equation(xpoints, fit_0, fit_1, fit_2)
    plt.plot(xpoints, fit_data, label="CurveFit", linestyle='solid', color="blue")
    plt.legend()
    plt.title("Feather data")
    plt.xlabel("Time(sec)")
    plt.ylabel("Position(m)")
    plt.savefig("feather.png")
    plt.show()
