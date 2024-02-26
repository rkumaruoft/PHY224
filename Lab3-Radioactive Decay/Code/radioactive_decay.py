import math

import numpy


def model_func_1(x, a, b):
    return (a * x) + b


def model_func_2(x, a, b):
    return b * (math.e ** (a * x))


def get_counts_array(fileName):
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    lines.pop(0)
    lines.pop(0)
    return numpy.array([int(line.split('\t')[1].replace('\n', '')) for line in lines])


if __name__ == "__main__":
    # Load Background file 3sec
    background_3_counts = get_counts_array('../background20min3sec2024.txt')
    print(numpy.mean(background_3_counts))

    # Load Background file 20 sec
    background_20_counts = get_counts_array('../background20min20sec2024.txt')
    background_20_mean = numpy.mean(background_20_counts)

    # Load 20sec data
    cesium_20_counts = get_counts_array("../cesium20min20sec2024.txt")
    cesium_20_counts = [cesium_20_counts[i] - background_20_mean for i in range(len(cesium_20_counts))]
