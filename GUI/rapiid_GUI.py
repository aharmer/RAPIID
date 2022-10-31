# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\HarmerA\\repos\rapiid\\GUI\\rapiid_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2311, 1110)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2291, 1090))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera_0_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_0_label.setFont(font)
        self.camera_0_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_0_label.setObjectName("camera_0_label")
        self.verticalLayout.addWidget(self.camera_0_label)
        self.horizontalLayout_0 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_0.setObjectName("horizontalLayout_0")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.camera_0_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_0_exposure_label.setObjectName("camera_0_exposure_label")
        self.verticalLayout_5.addWidget(self.camera_0_exposure_label)
        self.spinBox_camera_0_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_0_exposure.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_camera_0_exposure.setKeyboardTracking(False)
        self.spinBox_camera_0_exposure.setMinimum(1000)
        self.spinBox_camera_0_exposure.setMaximum(1000000)
        self.spinBox_camera_0_exposure.setSingleStep(10000)
        self.spinBox_camera_0_exposure.setProperty("value", 90000)
        self.spinBox_camera_0_exposure.setObjectName("spinBox_camera_0_exposure")
        self.verticalLayout_5.addWidget(self.spinBox_camera_0_exposure)
        self.horizontalLayout_0.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.camera_0_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_0_gain_label.setObjectName("camera_0_gain_label")
        self.verticalLayout_8.addWidget(self.camera_0_gain_label)
        self.doubleSpinBox_camera_0_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_0_gain.setKeyboardTracking(False)
        self.doubleSpinBox_camera_0_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_0_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_0_gain.setObjectName("doubleSpinBox_camera_0_gain")
        self.verticalLayout_8.addWidget(self.doubleSpinBox_camera_0_gain)
        self.horizontalLayout_0.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.camera_0_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_0_gamma_label.setObjectName("camera_0_gamma_label")
        self.verticalLayout_9.addWidget(self.camera_0_gamma_label)
        self.doubleSpinBox_camera_0_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_0_gamma.setKeyboardTracking(False)
        self.doubleSpinBox_camera_0_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_0_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_0_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_0_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_0_gamma.setObjectName("doubleSpinBox_camera_0_gamma")
        self.verticalLayout_9.addWidget(self.doubleSpinBox_camera_0_gamma)
        self.horizontalLayout_0.addLayout(self.verticalLayout_9)
        self.pushButton_camera_0 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_0.setObjectName("pushButton_camera_0")
        self.horizontalLayout_0.addWidget(self.pushButton_camera_0, 0, QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_0.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_0)
        self.camera_0 = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_0.setEnabled(True)
        self.camera_0.setMinimumSize(QtCore.QSize(540, 405))
        self.camera_0.setMaximumSize(QtCore.QSize(540, 405))
        self.camera_0.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_0.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_0.setText("")
        self.camera_0.setScaledContents(True)
        self.camera_0.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_0.setObjectName("camera_0")
        self.verticalLayout.addWidget(self.camera_0)
        self.camera_1_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_1_label.setFont(font)
        self.camera_1_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_1_label.setObjectName("camera_1_label")
        self.verticalLayout.addWidget(self.camera_1_label)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.camera_1_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_1_exposure_label.setObjectName("camera_1_exposure_label")
        self.verticalLayout_13.addWidget(self.camera_1_exposure_label)
        self.spinBox_camera_1_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_1_exposure.setKeyboardTracking(False)
        self.spinBox_camera_1_exposure.setMinimum(1000)
        self.spinBox_camera_1_exposure.setMaximum(1000000)
        self.spinBox_camera_1_exposure.setSingleStep(10000)
        self.spinBox_camera_1_exposure.setProperty("value", 90000)
        self.spinBox_camera_1_exposure.setObjectName("spinBox_camera_1_exposure")
        self.verticalLayout_13.addWidget(self.spinBox_camera_1_exposure)
        self.horizontalLayout_1.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.camera_1_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_1_gain_label.setObjectName("camera_1_gain_label")
        self.verticalLayout_14.addWidget(self.camera_1_gain_label)
        self.doubleSpinBox_camera_1_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_1_gain.setKeyboardTracking(False)
        self.doubleSpinBox_camera_1_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_1_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_1_gain.setObjectName("doubleSpinBox_camera_1_gain")
        self.verticalLayout_14.addWidget(self.doubleSpinBox_camera_1_gain)
        self.horizontalLayout_1.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.camera_1_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_1_gamma_label.setObjectName("camera_1_gamma_label")
        self.verticalLayout_15.addWidget(self.camera_1_gamma_label)
        self.doubleSpinBox_camera_1_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_1_gamma.setKeyboardTracking(False)
        self.doubleSpinBox_camera_1_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_1_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_1_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_1_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_1_gamma.setObjectName("doubleSpinBox_camera_1_gamma")
        self.verticalLayout_15.addWidget(self.doubleSpinBox_camera_1_gamma)
        self.horizontalLayout_1.addLayout(self.verticalLayout_15)
        self.pushButton_camera_1 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_1.setObjectName("pushButton_camera_1")
        self.horizontalLayout_1.addWidget(self.pushButton_camera_1, 0, QtCore.Qt.AlignBottom)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.camera_1 = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_1.setMinimumSize(QtCore.QSize(540, 405))
        self.camera_1.setMaximumSize(QtCore.QSize(540, 405))
        self.camera_1.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_1.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_1.setText("")
        self.camera_1.setScaledContents(True)
        self.camera_1.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_1.setObjectName("camera_1")
        self.verticalLayout.addWidget(self.camera_1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.camera_2_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_2_label.setFont(font)
        self.camera_2_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_2_label.setObjectName("camera_2_label")
        self.verticalLayout_2.addWidget(self.camera_2_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.camera_2_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_2_exposure_label.setObjectName("camera_2_exposure_label")
        self.verticalLayout_19.addWidget(self.camera_2_exposure_label)
        self.spinBox_camera_2_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_2_exposure.setKeyboardTracking(False)
        self.spinBox_camera_2_exposure.setMinimum(1000)
        self.spinBox_camera_2_exposure.setMaximum(1000000)
        self.spinBox_camera_2_exposure.setSingleStep(10000)
        self.spinBox_camera_2_exposure.setProperty("value", 90000)
        self.spinBox_camera_2_exposure.setObjectName("spinBox_camera_2_exposure")
        self.verticalLayout_19.addWidget(self.spinBox_camera_2_exposure)
        self.horizontalLayout_4.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.camera_2_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_2_gain_label.setObjectName("camera_2_gain_label")
        self.verticalLayout_20.addWidget(self.camera_2_gain_label)
        self.doubleSpinBox_camera_2_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_2_gain.setKeyboardTracking(False)
        self.doubleSpinBox_camera_2_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_2_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_2_gain.setObjectName("doubleSpinBox_camera_2_gain")
        self.verticalLayout_20.addWidget(self.doubleSpinBox_camera_2_gain)
        self.horizontalLayout_4.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.camera_2_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_2_gamma_label.setObjectName("camera_2_gamma_label")
        self.verticalLayout_21.addWidget(self.camera_2_gamma_label)
        self.doubleSpinBox_camera_2_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_2_gamma.setKeyboardTracking(False)
        self.doubleSpinBox_camera_2_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_2_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_2_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_2_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_2_gamma.setObjectName("doubleSpinBox_camera_2_gamma")
        self.verticalLayout_21.addWidget(self.doubleSpinBox_camera_2_gamma)
        self.horizontalLayout_4.addLayout(self.verticalLayout_21)
        self.pushButton_camera_2 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_2.setObjectName("pushButton_camera_2")
        self.horizontalLayout_4.addWidget(self.pushButton_camera_2, 0, QtCore.Qt.AlignBottom)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.camera_2 = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_2.setMinimumSize(QtCore.QSize(540, 405))
        self.camera_2.setMaximumSize(QtCore.QSize(540, 405))
        self.camera_2.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_2.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_2.setText("")
        self.camera_2.setScaledContents(True)
        self.camera_2.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_2.setObjectName("camera_2")
        self.verticalLayout_2.addWidget(self.camera_2)
        self.camera_3_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_3_label.setFont(font)
        self.camera_3_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_3_label.setObjectName("camera_3_label")
        self.verticalLayout_2.addWidget(self.camera_3_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.camera_3_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3_exposure_label.setObjectName("camera_3_exposure_label")
        self.verticalLayout_16.addWidget(self.camera_3_exposure_label)
        self.spinBox_camera_3_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_3_exposure.setKeyboardTracking(False)
        self.spinBox_camera_3_exposure.setMinimum(1000)
        self.spinBox_camera_3_exposure.setMaximum(1000000)
        self.spinBox_camera_3_exposure.setSingleStep(10000)
        self.spinBox_camera_3_exposure.setProperty("value", 90000)
        self.spinBox_camera_3_exposure.setObjectName("spinBox_camera_3_exposure")
        self.verticalLayout_16.addWidget(self.spinBox_camera_3_exposure)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.camera_3_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3_gain_label.setObjectName("camera_3_gain_label")
        self.verticalLayout_17.addWidget(self.camera_3_gain_label)
        self.doubleSpinBox_camera_3_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_3_gain.setKeyboardTracking(False)
        self.doubleSpinBox_camera_3_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_3_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_3_gain.setObjectName("doubleSpinBox_camera_3_gain")
        self.verticalLayout_17.addWidget(self.doubleSpinBox_camera_3_gain)
        self.horizontalLayout_5.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.camera_3_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3_gamma_label.setObjectName("camera_3_gamma_label")
        self.verticalLayout_18.addWidget(self.camera_3_gamma_label)
        self.doubleSpinBox_camera_3_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_3_gamma.setKeyboardTracking(False)
        self.doubleSpinBox_camera_3_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_3_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_3_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_3_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_3_gamma.setObjectName("doubleSpinBox_camera_3_gamma")
        self.verticalLayout_18.addWidget(self.doubleSpinBox_camera_3_gamma)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        self.pushButton_camera_3 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_3.setObjectName("pushButton_camera_3")
        self.horizontalLayout_5.addWidget(self.pushButton_camera_3, 0, QtCore.Qt.AlignBottom)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.camera_3 = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3.setMinimumSize(QtCore.QSize(540, 405))
        self.camera_3.setMaximumSize(QtCore.QSize(540, 16777215))
        self.camera_3.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_3.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_3.setText("")
        self.camera_3.setScaledContents(True)
        self.camera_3.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_3.setObjectName("camera_3")
        self.verticalLayout_2.addWidget(self.camera_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.camera_4_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_4_label.setFont(font)
        self.camera_4_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_4_label.setObjectName("camera_4_label")
        self.verticalLayout_3.addWidget(self.camera_4_label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.camera_4_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_4_exposure_label.setObjectName("camera_4_exposure_label")
        self.verticalLayout_22.addWidget(self.camera_4_exposure_label)
        self.spinBox_camera_4_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_4_exposure.setKeyboardTracking(False)
        self.spinBox_camera_4_exposure.setMinimum(1000)
        self.spinBox_camera_4_exposure.setMaximum(1000000)
        self.spinBox_camera_4_exposure.setSingleStep(10000)
        self.spinBox_camera_4_exposure.setProperty("value", 90000)
        self.spinBox_camera_4_exposure.setObjectName("spinBox_camera_4_exposure")
        self.verticalLayout_22.addWidget(self.spinBox_camera_4_exposure)
        self.horizontalLayout_7.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.camera_4_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_4_gain_label.setObjectName("camera_4_gain_label")
        self.verticalLayout_23.addWidget(self.camera_4_gain_label)
        self.doubleSpinBox_camera_4_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_4_gain.setKeyboardTracking(False)
        self.doubleSpinBox_camera_4_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_4_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_4_gain.setObjectName("doubleSpinBox_camera_4_gain")
        self.verticalLayout_23.addWidget(self.doubleSpinBox_camera_4_gain)
        self.horizontalLayout_7.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.camera_4_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_4_gamma_label.setObjectName("camera_4_gamma_label")
        self.verticalLayout_24.addWidget(self.camera_4_gamma_label)
        self.doubleSpinBox_camera_4_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_4_gamma.setKeyboardTracking(False)
        self.doubleSpinBox_camera_4_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_4_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_4_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_4_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_4_gamma.setObjectName("doubleSpinBox_camera_4_gamma")
        self.verticalLayout_24.addWidget(self.doubleSpinBox_camera_4_gamma)
        self.horizontalLayout_7.addLayout(self.verticalLayout_24)
        self.pushButton_camera_4 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_4.setObjectName("pushButton_camera_4")
        self.horizontalLayout_7.addWidget(self.pushButton_camera_4, 0, QtCore.Qt.AlignBottom)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.camera_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_4.setMinimumSize(QtCore.QSize(540, 405))
        self.camera_4.setMaximumSize(QtCore.QSize(540, 405))
        self.camera_4.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_4.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_4.setText("")
        self.camera_4.setScaledContents(True)
        self.camera_4.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_4.setObjectName("camera_4")
        self.verticalLayout_3.addWidget(self.camera_4)
        self.camera_5_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_5_label.setFont(font)
        self.camera_5_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_5_label.setObjectName("camera_5_label")
        self.verticalLayout_3.addWidget(self.camera_5_label)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.camera_5_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_5_exposure_label.setObjectName("camera_5_exposure_label")
        self.verticalLayout_25.addWidget(self.camera_5_exposure_label)
        self.spinBox_camera_5_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_5_exposure.setKeyboardTracking(False)
        self.spinBox_camera_5_exposure.setMinimum(1000)
        self.spinBox_camera_5_exposure.setMaximum(1000000)
        self.spinBox_camera_5_exposure.setSingleStep(10000)
        self.spinBox_camera_5_exposure.setProperty("value", 90000)
        self.spinBox_camera_5_exposure.setObjectName("spinBox_camera_5_exposure")
        self.verticalLayout_25.addWidget(self.spinBox_camera_5_exposure)
        self.horizontalLayout_8.addLayout(self.verticalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.camera_5_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_5_gain_label.setObjectName("camera_5_gain_label")
        self.verticalLayout_26.addWidget(self.camera_5_gain_label)
        self.doubleSpinBox_camera_5_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_5_gain.setKeyboardTracking(False)
        self.doubleSpinBox_camera_5_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_5_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_5_gain.setObjectName("doubleSpinBox_camera_5_gain")
        self.verticalLayout_26.addWidget(self.doubleSpinBox_camera_5_gain)
        self.horizontalLayout_8.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.camera_5_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_5_gamma_label.setObjectName("camera_5_gamma_label")
        self.verticalLayout_27.addWidget(self.camera_5_gamma_label)
        self.doubleSpinBox_camera_5_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_5_gamma.setKeyboardTracking(False)
        self.doubleSpinBox_camera_5_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_5_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_5_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_5_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_5_gamma.setObjectName("doubleSpinBox_camera_5_gamma")
        self.verticalLayout_27.addWidget(self.doubleSpinBox_camera_5_gamma)
        self.horizontalLayout_8.addLayout(self.verticalLayout_27)
        self.pushButton_camera_5 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_5.setObjectName("pushButton_camera_5")
        self.horizontalLayout_8.addWidget(self.pushButton_camera_5, 0, QtCore.Qt.AlignBottom)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.camera_5 = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_5.setMinimumSize(QtCore.QSize(540, 405))
        self.camera_5.setMaximumSize(QtCore.QSize(540, 405))
        self.camera_5.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_5.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_5.setText("")
        self.camera_5.setScaledContents(True)
        self.camera_5.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_5.setObjectName("camera_5")
        self.verticalLayout_3.addWidget(self.camera_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalWidget_4 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy)
        self.verticalWidget_4.setMinimumSize(QtCore.QSize(200, 0))
        self.verticalWidget_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_load_config = QtWidgets.QPushButton(self.verticalWidget_4)
        self.pushButton_load_config.setObjectName("pushButton_load_config")
        self.verticalLayout_4.addWidget(self.pushButton_load_config)
        self.pushButton_writeConfig = QtWidgets.QPushButton(self.verticalWidget_4)
        self.pushButton_writeConfig.setObjectName("pushButton_writeConfig")
        self.verticalLayout_4.addWidget(self.pushButton_writeConfig)
        spacerItem6 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem6)
        self.pushButton_outputFolder = QtWidgets.QPushButton(self.verticalWidget_4)
        self.pushButton_outputFolder.setObjectName("pushButton_outputFolder")
        self.verticalLayout_4.addWidget(self.pushButton_outputFolder)
        self.display_path = QtWidgets.QLabel(self.verticalWidget_4)
        self.display_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.display_path.setFrameShadow(QtWidgets.QFrame.Plain)
        self.display_path.setWordWrap(True)
        self.display_path.setObjectName("display_path")
        self.verticalLayout_4.addWidget(self.display_path)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.label_project = QtWidgets.QLabel(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_project.setFont(font)
        self.label_project.setObjectName("label_project")
        self.verticalLayout_4.addWidget(self.label_project)
        self.lineEdit_project = QtWidgets.QLineEdit(self.verticalWidget_4)
        self.lineEdit_project.setObjectName("lineEdit_project")
        self.verticalLayout_4.addWidget(self.lineEdit_project)
        self.label_accession = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_accession.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_accession.sizePolicy().hasHeightForWidth())
        self.label_accession.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_accession.setFont(font)
        self.label_accession.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_accession.setObjectName("label_accession")
        self.verticalLayout_4.addWidget(self.label_accession)
        self.lineEdit_accession = QtWidgets.QLineEdit(self.verticalWidget_4)
        self.lineEdit_accession.setObjectName("lineEdit_accession")
        self.verticalLayout_4.addWidget(self.lineEdit_accession)
        spacerItem8 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem8)
        self.pushButton_capture = QtWidgets.QPushButton(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_capture.setFont(font)
        self.pushButton_capture.setObjectName("pushButton_capture")
        self.verticalLayout_4.addWidget(self.pushButton_capture)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.label_log = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_log.setObjectName("label_log")
        self.verticalLayout_4.addWidget(self.label_log)
        self.listWidget_log = QtWidgets.QListWidget(self.verticalWidget_4)
        self.listWidget_log.setMinimumSize(QtCore.QSize(0, 300))
        self.listWidget_log.setMaximumSize(QtCore.QSize(1000, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_log.setFont(font)
        self.listWidget_log.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_log.setProperty("isWrapping", False)
        self.listWidget_log.setWordWrap(True)
        self.listWidget_log.setObjectName("listWidget_log")
        self.verticalLayout_4.addWidget(self.listWidget_log)
        self.horizontalLayout_2.addWidget(self.verticalWidget_4)
        self.horizontalLayout_9.addWidget(self.horizontalWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RAPIID v1.0"))
        self.camera_0_label.setText(_translate("MainWindow", "Dorsal Camera"))
        self.camera_0_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_0_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_0_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_0.setText(_translate("MainWindow", "Start live view"))
        self.camera_1_label.setText(_translate("MainWindow", "Lateral Camera"))
        self.camera_1_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_1_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_1_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_1.setText(_translate("MainWindow", "Start live view"))
        self.camera_2_label.setText(_translate("MainWindow", "Label Camera 1"))
        self.camera_2_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_2_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_2_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_2.setText(_translate("MainWindow", "Start live view"))
        self.camera_3_label.setText(_translate("MainWindow", "Label Camera 2"))
        self.camera_3_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_3_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_3_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_3.setText(_translate("MainWindow", "Start live view"))
        self.camera_4_label.setText(_translate("MainWindow", "Label Camera 3"))
        self.camera_4_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_4_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_4_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_4.setText(_translate("MainWindow", "Start live view"))
        self.camera_5_label.setText(_translate("MainWindow", "Label Camera 4"))
        self.camera_5_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_5_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_5_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_5.setText(_translate("MainWindow", "Start live view"))
        self.pushButton_load_config.setText(_translate("MainWindow", "Load config file..."))
        self.pushButton_writeConfig.setText(_translate("MainWindow", "Save config file..."))
        self.pushButton_outputFolder.setText(_translate("MainWindow", "Output folder..."))
        self.display_path.setText(_translate("MainWindow", "Path"))
        self.label_project.setText(_translate("MainWindow", "Project name"))
        self.label_accession.setText(_translate("MainWindow", "NZAC accession no."))
        self.pushButton_capture.setText(_translate("MainWindow", "Capture image set"))
        self.label_log.setText(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
