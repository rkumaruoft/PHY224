def read_file_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    return lines
