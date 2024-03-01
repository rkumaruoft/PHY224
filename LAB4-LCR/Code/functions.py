import matplotlib.pyplot as plt
def read_file_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    return lines

def draw_data(data, title, legend):
    data = read_file_data("../" + data)
    # time data is in seconds
    x_data = []
    y_data = []
    for line in data:
        line.replace("\n", '')
        this_line = [float(num) for num in line.split(",")]
        x_data.append(this_line[0])
        y_data.append(this_line[1])

    plt.errorbar(x_data, y_data, fmt=".", label="Resistance Data")
    plt.legend(legend)
    plt.title(title)
    plt.show()
