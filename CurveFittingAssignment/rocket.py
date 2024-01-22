import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# linear regression
def best_speed_estimate(times, distances, mean_time, mean_distance):
    numerators = []
    denominators = []
    for index in range(len(times)):
        numerators.append((times[index] - mean_time) * (distances[index] - mean_distance))
        denominators.append((times[index] - mean_time) ** 2)
    return sum(numerators) / sum(denominators)


def best_position_estimate(speed_estimate, mean_time, mean_distance):
    return mean_distance - speed_estimate * mean_time


def distance_formula(x, initial_position, speed):
    return initial_position + (speed * x)


# noinspection PyShadowingNames
def x_r2_metric(N, m, initial_position, speed, measured_distance_data, times, uncertainties):
    to_sum = []
    for i in range(N):
        to_sum.append(((measured_distance_data[i] - distance_formula(times[i], initial_position, speed)) ** 2)
                      / (uncertainties[i] ** 2))
    return sum(to_sum) / (N - m)


if __name__ == '__main__':
    mat.use('TkAgg')
    data = numpy.loadtxt("rocket.csv", delimiter=",")
    xpoints = []
    ypoints = []
    uncertainties = []
    i = 0
    for line in data:
        xpoints.append(line[0])
        ypoints.append(line[1])
        uncertainties.append(line[2])
        i += 1

    speeds = []
    i = 0
    for i in range(len(xpoints)):
        if xpoints[i] != 0:
            speeds.append(ypoints[i] / xpoints[i])
        i += 1

    speeds = numpy.array(speeds)
    xpoints = numpy.array(xpoints)
    ypoints = numpy.array(ypoints)

    average_speed = numpy.mean(speeds)
    std = numpy.std(speeds)
    print("Average Speed: " + str(average_speed))
    print("Standard Error: " + str(std))

    # best estimates for u and d
    mean_distance = numpy.mean(ypoints)
    mean_time = numpy.mean(xpoints)
    speed_estimate = best_speed_estimate(xpoints, ypoints, mean_time, mean_distance)
    position_estimate = best_position_estimate(speed_estimate, mean_time, mean_distance)
    print("Best Speed Estimate: ", str(speed_estimate))
    print("Best position Estimate: ", str(position_estimate))

    # X_r^2
    x_r = x_r2_metric(len(xpoints), 2, position_estimate, speed_estimate, ypoints, xpoints, uncertainties)
    print("X_r^2 : " + str(x_r))

    # curve fit
    popt,pcov = curve_fit(distance_formula, xpoints, ypoints)
    plt.errorbar(xpoints, ypoints, yerr=uncertainties, fmt='.', label="Data")
    plt.plot(xpoints, distance_formula(xpoints, position_estimate, speed_estimate), label="Prediction")
    print(popt)
    fit_0 = popt[0]
    fit_1 = popt[1]
    fit_data = distance_formula(xpoints, fit_0, fit_1)
    plt.plot(xpoints, fit_data, label="CurveFit", linestyle='dashed', color="blue")
    plt.title("Saturn V data")
    plt.xlabel("Time(hour)")
    plt.ylabel("Position(km)")
    plt.savefig("Saturn V data.png")
    plt.legend()
    plt.show()
