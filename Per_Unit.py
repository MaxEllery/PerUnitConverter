from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
import sys
import math

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.resetButton.clicked.connect(self.calculate)
        self.calculateButton.clicked.connect(self.calculate)

    def calculate(self):
        #Gens and Transformers
        system_base = is_input_float(self.powerBaseText.text())
        voltage_base = is_input_float(self.voltageBaseText.text())
        power_rating = is_input_float(self.powerRatingText.text())
        value = is_input_float(self.valueText.text())
        unit = self.unitList.currentText()
        z_base = ((voltage_base * 1000) ** 2) / (system_base * 1000000)
        #cables
        distance = is_input_float(self.distanceText.text())
        R_in = is_input_float(self.RText.text())
        X_in = is_input_float(self.XText.text())
        C_in = is_input_float(self.CText.text())
        output, R_out, X_out, B_out = 0, 0, 0, 0

        if not power_rating == None:
            if unit == "Per Unit":
                output = round(value * system_base / power_rating, 5)
            else:
                output = round((value / 100) * system_base / power_rating, 5)

        if not ((distance == None) and ((R_in == None) or (X_in == None) or (C_in == None))):
            if not R_in == None:
                R_out = round((distance * (R_in/1000)) / z_base, 5)

            if not X_in == None:
                X_out = round((distance * (X_in/1000)) / z_base, 5)

            if not C_in == None:
                B_out = 2 * math.pi * 50 * (z_base * distance * (C_in/1000) / 1000000)

        self.output_gen_txText.setText(str(output))
        self.R_outText.setText(str(R_out))
        self.X_outText.setText(str(X_out))
        self.C_outText.setText(str(B_out))
        return

    def reset(self):
        self.powerBaseText.setText("100")
        self.voltageBaseText.setText("11")
        self.powerRatingText.setText("0")
        self.valueText.setText("0")
        self.output_gen_txText.setText("0")
        self.distanceText.setText("0")
        self.RText.setText("0")
        self.XText.setText("0")
        self.CText.setText("0")
        self.R_outText.setText("0")
        self.X_outText.setText("0")
        self.C_outText.setText("0")
        return

def is_input_float(input):
    if input=="":
        return None
    else:
        try:
            float(input)
            return float(input)
        except ValueError:
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())