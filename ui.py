# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'per_unit_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 594)
        MainWindow.setMaximumSize(QtCore.QSize(481, 594))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.powerBaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.powerBaseLabel.setGeometry(QtCore.QRect(0, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(16)
        self.powerBaseLabel.setFont(font)
        self.powerBaseLabel.setObjectName("powerBaseLabel")
        self.powerBaseText = QtWidgets.QLineEdit(self.centralwidget)
        self.powerBaseText.setGeometry(QtCore.QRect(180, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.powerBaseText.setFont(font)
        self.powerBaseText.setObjectName("powerBaseText")
        self.powerRatingLabel = QtWidgets.QLabel(self.centralwidget)
        self.powerRatingLabel.setGeometry(QtCore.QRect(0, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(16)
        self.powerRatingLabel.setFont(font)
        self.powerRatingLabel.setObjectName("powerRatingLabel")
        self.powerRatingText = QtWidgets.QLineEdit(self.centralwidget)
        self.powerRatingText.setGeometry(QtCore.QRect(180, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.powerRatingText.setFont(font)
        self.powerRatingText.setText("")
        self.powerRatingText.setObjectName("powerRatingText")
        self.voltageBaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.voltageBaseLabel.setGeometry(QtCore.QRect(260, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(16)
        self.voltageBaseLabel.setFont(font)
        self.voltageBaseLabel.setObjectName("voltageBaseLabel")
        self.voltageBaseText = QtWidgets.QLineEdit(self.centralwidget)
        self.voltageBaseText.setGeometry(QtCore.QRect(410, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.voltageBaseText.setFont(font)
        self.voltageBaseText.setObjectName("voltageBaseText")
        self.valueText = QtWidgets.QLineEdit(self.centralwidget)
        self.valueText.setGeometry(QtCore.QRect(180, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.valueText.setFont(font)
        self.valueText.setText("")
        self.valueText.setObjectName("valueText")
        self.valueLabel = QtWidgets.QLabel(self.centralwidget)
        self.valueLabel.setGeometry(QtCore.QRect(0, 190, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(16)
        self.valueLabel.setFont(font)
        self.valueLabel.setObjectName("valueLabel")
        self.unitList = QtWidgets.QComboBox(self.centralwidget)
        self.unitList.setGeometry(QtCore.QRect(260, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.unitList.setFont(font)
        self.unitList.setObjectName("unitList")
        self.unitList.addItem("")
        self.unitList.addItem("")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(120, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(24)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.ImpedanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImpedanceLabel.setGeometry(QtCore.QRect(90, 100, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.ImpedanceLabel.setFont(font)
        self.ImpedanceLabel.setObjectName("ImpedanceLabel")
        self.ImpedanceLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.ImpedanceLabel_2.setGeometry(QtCore.QRect(190, 280, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.ImpedanceLabel_2.setFont(font)
        self.ImpedanceLabel_2.setObjectName("ImpedanceLabel_2")
        self.distanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.distanceLabel.setGeometry(QtCore.QRect(60, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.distanceLabel.setFont(font)
        self.distanceLabel.setObjectName("distanceLabel")
        self.RLabel = QtWidgets.QLabel(self.centralwidget)
        self.RLabel.setGeometry(QtCore.QRect(160, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.RLabel.setFont(font)
        self.RLabel.setObjectName("RLabel")
        self.XLabel = QtWidgets.QLabel(self.centralwidget)
        self.XLabel.setGeometry(QtCore.QRect(260, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.XLabel.setFont(font)
        self.XLabel.setObjectName("XLabel")
        self.CLabel = QtWidgets.QLabel(self.centralwidget)
        self.CLabel.setGeometry(QtCore.QRect(360, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.CLabel.setFont(font)
        self.CLabel.setObjectName("CLabel")
        self.distanceText = QtWidgets.QLineEdit(self.centralwidget)
        self.distanceText.setGeometry(QtCore.QRect(90, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.distanceText.setFont(font)
        self.distanceText.setText("")
        self.distanceText.setObjectName("distanceText")
        self.RText = QtWidgets.QLineEdit(self.centralwidget)
        self.RText.setGeometry(QtCore.QRect(180, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.RText.setFont(font)
        self.RText.setText("")
        self.RText.setObjectName("RText")
        self.XText = QtWidgets.QLineEdit(self.centralwidget)
        self.XText.setGeometry(QtCore.QRect(270, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.XText.setFont(font)
        self.XText.setText("")
        self.XText.setObjectName("XText")
        self.CText = QtWidgets.QLineEdit(self.centralwidget)
        self.CText.setGeometry(QtCore.QRect(360, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.CText.setFont(font)
        self.CText.setText("")
        self.CText.setObjectName("CText")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(20, 450, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.calculateButton.setFont(font)
        self.calculateButton.setObjectName("calculateButton")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(20, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.output_gen_txText = QtWidgets.QLineEdit(self.centralwidget)
        self.output_gen_txText.setGeometry(QtCore.QRect(180, 240, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.output_gen_txText.setFont(font)
        self.output_gen_txText.setText("")
        self.output_gen_txText.setObjectName("output_gen_txText")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(0, 230, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(16)
        self.outputLabel.setFont(font)
        self.outputLabel.setObjectName("outputLabel")
        self.R_outText = QtWidgets.QLineEdit(self.centralwidget)
        self.R_outText.setGeometry(QtCore.QRect(220, 430, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.R_outText.setFont(font)
        self.R_outText.setText("")
        self.R_outText.setObjectName("R_outText")
        self.C_outText = QtWidgets.QLineEdit(self.centralwidget)
        self.C_outText.setGeometry(QtCore.QRect(220, 510, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.C_outText.setFont(font)
        self.C_outText.setText("")
        self.C_outText.setObjectName("C_outText")
        self.X_outText = QtWidgets.QLineEdit(self.centralwidget)
        self.X_outText.setGeometry(QtCore.QRect(220, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        self.X_outText.setFont(font)
        self.X_outText.setText("")
        self.X_outText.setObjectName("X_outText")
        self.R_outLabel = QtWidgets.QLabel(self.centralwidget)
        self.R_outLabel.setGeometry(QtCore.QRect(170, 420, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.R_outLabel.setFont(font)
        self.R_outLabel.setObjectName("R_outLabel")
        self.X_outLabel = QtWidgets.QLabel(self.centralwidget)
        self.X_outLabel.setGeometry(QtCore.QRect(170, 460, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.X_outLabel.setFont(font)
        self.X_outLabel.setObjectName("X_outLabel")
        self.B_outLabel = QtWidgets.QLabel(self.centralwidget)
        self.B_outLabel.setGeometry(QtCore.QRect(170, 500, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.B_outLabel.setFont(font)
        self.B_outLabel.setObjectName("B_outLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.powerBaseLabel.setText(_translate("MainWindow", "System Base (MVA)"))
        self.powerBaseText.setText(_translate("MainWindow", "100"))
        self.powerRatingLabel.setText(_translate("MainWindow", "Power Rating (MVA)"))
        self.voltageBaseLabel.setText(_translate("MainWindow", "Voltage Base (kV)"))
        self.voltageBaseText.setText(_translate("MainWindow", "11"))
        self.valueLabel.setText(_translate("MainWindow", "Value to Change"))
        self.unitList.setItemText(0, _translate("MainWindow", "Per Unit"))
        self.unitList.setItemText(1, _translate("MainWindow", "%"))
        self.TitleLabel.setText(_translate("MainWindow", "Per Unit Calculator"))
        self.ImpedanceLabel.setText(_translate("MainWindow", "For Generators / Transformers"))
        self.ImpedanceLabel_2.setText(_translate("MainWindow", "For Cables"))
        self.distanceLabel.setText(_translate("MainWindow", "Distance (m)"))
        self.RLabel.setText(_translate("MainWindow", "R(ohms/km)"))
        self.XLabel.setText(_translate("MainWindow", "X(ohms/km)"))
        self.CLabel.setText(_translate("MainWindow", "C(uF/km)"))
        self.calculateButton.setText(_translate("MainWindow", "CALCULATE"))
        self.resetButton.setText(_translate("MainWindow", "RESET"))
        self.outputLabel.setText(_translate("MainWindow", "Output"))
        self.R_outLabel.setText(_translate("MainWindow", "R (pu)"))
        self.X_outLabel.setText(_translate("MainWindow", "X (pu)"))
        self.B_outLabel.setText(_translate("MainWindow", "B (pu)"))
