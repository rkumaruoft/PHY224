from functions import *

if __name__ == '__main__':
    # x, y = fit_double_slit_outline("../More Data/Double_slit_0.04_0.25.txt", -0.075, -0.059, None, 1.2, diffraction)

    draw_data_and_curve("..\More Data\Double_slit_0.04_0.25.txt",
                        "Sensor position (Metres)", "Light intensity (Volts)", "Double slit 0.04, 0.25 separation",
                        ["fit", "Data"], diffraction, 0.065)

    draw_data_and_curve("..\More Data\Double_slit_0.04_0.50.txt",
                        "Sensor position (Metres)", "Light intensity (Volts)", "Double slit 0.04, 0.50 separation",
                        ["fit", "Data"], diffraction, 0.085)

    draw_data_and_curve("..\More Data\Double_slit_0.08_0.25.txt",
                        "Sensor position (Metres)", "Light intensity (Volts)", "Double slit 0.08, 0.25 separation",
                        ["fit", "Data"], diffraction, 4.77)
