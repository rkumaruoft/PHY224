import math
import matplotlib as mat
import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit

e = math.e


def model_func_1(x, a, b):
    return (a * x) + b


def model_func_2(x, a, b):
    return b * ((e) ** (-a * x))


def get_counts_array(fileName):
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    lines.pop(0)
    lines.pop(0)
    return numpy.array([float(line.split('\t')[1].replace('\n', '')) for line in lines])


def reduced_x_r2(N, m, measured_data, model_data, uncertainties):
    summ = 0
    for i in range(N):
        summ += ((measured_data[i] - model_data[i]) ** 2) / (uncertainties[i] ** 2)
    return summ / (N - m)


if __name__ == "__main__":

    """PART 1"""
    # Load Background file 20 sec
    background_20_counts = get_counts_array('../background20min20sec2024.txt')
    background_20_mean = numpy.mean(background_20_counts)

    # Load 20sec data
    cesium_20_counts_raw = get_counts_array("../cesium20min20sec2024.txt")
    cesium_20_counts = numpy.array(
        [cesium_20_counts_raw[i] - background_20_mean for i in range(len(cesium_20_counts_raw))])

    # Uncertainty for 20sec data
    cesium_20_uncert = []
    for i in range(len(cesium_20_counts_raw)):
        cesium_20_uncert.append(math.sqrt(cesium_20_counts_raw[i] + background_20_counts[i]))
    cesium_20_uncert = numpy.array(cesium_20_uncert)
    # convert 20sec data to rates
    cesium_20_rates = numpy.array([count / (20 * 60) for count in cesium_20_counts])
    cesium_20_rates_uncert = numpy.array([count / (20 * 60) for count in cesium_20_uncert])

    # 20sec x-data
    x_data = numpy.array([i for i in range(len(cesium_20_counts))])
    plt.errorbar(x_data*20/60, cesium_20_counts, yerr=cesium_20_uncert, fmt=".")

    # Model 1
    cesium_20_counts_log = numpy.array([math.log(count, math.e) for count in cesium_20_counts])
    cesium_20_uncert_log = numpy.array([cesium_20_uncert[i]
                                        / cesium_20_counts[i]
                                        for i in range(len(cesium_20_uncert))])
    popt, pcov = curve_fit(model_func_1, xdata=x_data, ydata=cesium_20_counts_log,
                           sigma=cesium_20_uncert_log, absolute_sigma=True)
    print("Log Model")
    print(popt)
    model_func_1_data = model_func_1(x_data, popt[0], popt[1])
    antilog_model_data = []
    for data in model_func_1_data:
        antilog_model_data.append(math.exp(data))
    plt.plot(x_data*20/60, antilog_model_data, label='Log Model regression')
    x_r_log = reduced_x_r2(len(antilog_model_data), 2, cesium_20_counts, antilog_model_data, cesium_20_uncert)
    print("X_r: ", x_r_log)
    decay_rate = popt[0]
    decay_rate_error = math.sqrt(pcov[0][0])
    initial_intensity = math.exp(popt[1])
    initial_intensity_error = initial_intensity * math.sqrt(pcov[1][1])
    print("Rate: ", decay_rate, " Error: ", decay_rate_error)
    print("Initial intensity: ", initial_intensity, " Error: ", initial_intensity_error)
    half_life = math.log(1/2, e) / decay_rate
    half_life_error = abs(- (math.log(1 / 2, e) / (decay_rate ** 2)) * decay_rate_error)
    print("Half Life: ", half_life * 20 / 60, "Error: ", half_life_error)

    print("\n\n\n")
    print("Exponent Model")
    popt, pcov = curve_fit(model_func_2, xdata=x_data, ydata=cesium_20_counts,
                           sigma=cesium_20_uncert, absolute_sigma=True)
    print(popt)
    model_func_2_data = model_func_2(x_data, popt[0], popt[1])
    plt.plot(x_data*20/60, model_func_2_data, label='Exponential Model regression', linestyle='dashed', color='blue')
    x_r_power = reduced_x_r2(len(model_func_2_data), 2, cesium_20_counts, model_func_2_data, cesium_20_uncert)
    print("X_r: ", x_r_power)
    decay_rate = -popt[0]
    decay_rate_error = math.sqrt(pcov[0][0])
    initial_intensity = popt[1]
    initial_intensity_error = math.sqrt(pcov[1][1])
    print("Rate: ", decay_rate, " Error: ", decay_rate_error)
    print("Initial intensity: ", initial_intensity, " Error: ", initial_intensity_error)
    half_life = math.log(1/2, e) / decay_rate
    half_life_error = abs(- (math.log(1 / 2, e) / (decay_rate ** 2)) * decay_rate_error)
    print("Half Life: ", half_life * 20 / 60, "Error: ", half_life_error)

    # Theoretical Model
    print("\n\n\n")
    print("Theoretical Model")
    average_rate = numpy.mean(cesium_20_rates)
    average_rate_error = max([abs(average_rate - i) for i in cesium_20_rates])
    initial_y = cesium_20_counts[0]
    theoretical_model_data = []
    for i in x_data:
        new_y = initial_y * ((1/2) ** (i * average_rate))
        theoretical_model_data.append(new_y)
    x_r_theory = reduced_x_r2(len(theoretical_model_data), 2, cesium_20_counts,
                              theoretical_model_data, cesium_20_uncert)
    print("X_r: ", x_r_theory)
    half_life = math.log(1 / 2, e) / -average_rate
    half_life_error = abs(- (math.log(1 / 2, e) / (average_rate ** 2)) * average_rate_error)
    print("Half Life: ", half_life * 20 / 60, "Error: ", half_life_error)

    plt.plot(x_data*20/60, theoretical_model_data, label='Theoretical Model', linestyle='dotted', color='brown')
    plt.xlabel("Time (min)")
    plt.ylabel("Count")
    plt.legend()
    plt.show()

    #----------------RESIDUALS GO HERE-------------------#
