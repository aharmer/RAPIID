# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HarmerA\repos\rapiid\GUI\rapiid_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2317, 1128)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2297, 1108))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_5.addWidget(self.doubleSpinBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_8.addWidget(self.spinBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_9.addWidget(self.spinBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.pushButton_camera_1 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_1.setObjectName("pushButton_camera_1")
        self.horizontalLayout_2.addWidget(self.pushButton_camera_1, 0, QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.camera_1 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_1.sizePolicy().hasHeightForWidth())
        self.camera_1.setSizePolicy(sizePolicy)
        self.camera_1.setMinimumSize(QtCore.QSize(180, 135))
        self.camera_1.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_1.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_1.setText("")
        self.camera_1.setScaledContents(False)
        self.camera_1.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_1.setObjectName("camera_1")
        self.verticalLayout.addWidget(self.camera_1)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_20 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_13.addWidget(self.label_20)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.verticalLayout_13.addWidget(self.doubleSpinBox_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_21 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_14.addWidget(self.label_21)
        self.spinBox_8 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_8.setObjectName("spinBox_8")
        self.verticalLayout_14.addWidget(self.spinBox_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_22 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_15.addWidget(self.label_22)
        self.spinBox_9 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_9.setObjectName("spinBox_9")
        self.verticalLayout_15.addWidget(self.spinBox_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_15)
        self.pushButton_camera_2 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_2.setObjectName("pushButton_camera_2")
        self.horizontalLayout_4.addWidget(self.pushButton_camera_2, 0, QtCore.Qt.AlignBottom)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(180, 135))
        self.label_4.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.camera_3_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.camera_3_label.setFont(font)
        self.camera_3_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_3_label.setObjectName("camera_3_label")
        self.verticalLayout_2.addWidget(self.camera_3_label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.camera_3_exposure_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3_exposure_label.setObjectName("camera_3_exposure_label")
        self.verticalLayout_19.addWidget(self.camera_3_exposure_label)
        self.spinBox_camera_3_exposure = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_camera_3_exposure.setMinimum(1000)
        self.spinBox_camera_3_exposure.setMaximum(1000000)
        self.spinBox_camera_3_exposure.setSingleStep(1000)
        self.spinBox_camera_3_exposure.setProperty("value", 90000)
        self.spinBox_camera_3_exposure.setObjectName("spinBox_camera_3_exposure")
        self.verticalLayout_19.addWidget(self.spinBox_camera_3_exposure)
        self.horizontalLayout_6.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.camera_3_gain_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3_gain_label.setObjectName("camera_3_gain_label")
        self.verticalLayout_20.addWidget(self.camera_3_gain_label)
        self.doubleSpinBox_camera_3_gain = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_3_gain.setMaximum(25.0)
        self.doubleSpinBox_camera_3_gain.setProperty("value", 1.83)
        self.doubleSpinBox_camera_3_gain.setObjectName("doubleSpinBox_camera_3_gain")
        self.verticalLayout_20.addWidget(self.doubleSpinBox_camera_3_gain)
        self.horizontalLayout_6.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.camera_3_gamma_label = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_3_gamma_label.setObjectName("camera_3_gamma_label")
        self.verticalLayout_21.addWidget(self.camera_3_gamma_label)
        self.doubleSpinBox_camera_3_gamma = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_camera_3_gamma.setMinimum(0.1)
        self.doubleSpinBox_camera_3_gamma.setMaximum(4.0)
        self.doubleSpinBox_camera_3_gamma.setSingleStep(0.1)
        self.doubleSpinBox_camera_3_gamma.setProperty("value", 0.8)
        self.doubleSpinBox_camera_3_gamma.setObjectName("doubleSpinBox_camera_3_gamma")
        self.verticalLayout_21.addWidget(self.doubleSpinBox_camera_3_gamma)
        self.horizontalLayout_6.addLayout(self.verticalLayout_21)
        self.pushButton_camera_3 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_3.setObjectName("pushButton_camera_3")
        self.horizontalLayout_6.addWidget(self.pushButton_camera_3, 0, QtCore.Qt.AlignBottom)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.camera_3 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_3.sizePolicy().hasHeightForWidth())
        self.camera_3.setSizePolicy(sizePolicy)
        self.camera_3.setMinimumSize(QtCore.QSize(180, 135))
        self.camera_3.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.camera_3.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_3.setText("")
        self.camera_3.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_3.setObjectName("camera_3")
        self.verticalLayout_2.addWidget(self.camera_3)
        self.label_7 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_23 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_16.addWidget(self.label_23)
        self.spinBox_10 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_10.setObjectName("spinBox_10")
        self.verticalLayout_16.addWidget(self.spinBox_10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_24 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_17.addWidget(self.label_24)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.verticalLayout_17.addWidget(self.doubleSpinBox_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_25 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_18.addWidget(self.label_25)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.verticalLayout_18.addWidget(self.doubleSpinBox_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        self.pushButton_camera_4 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_4.setObjectName("pushButton_camera_4")
        self.horizontalLayout_5.addWidget(self.pushButton_camera_4, 0, QtCore.Qt.AlignBottom)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_8 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(180, 135))
        self.label_8.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_29 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_22.addWidget(self.label_29)
        self.spinBox_16 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_16.setObjectName("spinBox_16")
        self.verticalLayout_22.addWidget(self.spinBox_16)
        self.horizontalLayout_7.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_30 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_23.addWidget(self.label_30)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.verticalLayout_23.addWidget(self.doubleSpinBox_17)
        self.horizontalLayout_7.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_31 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_24.addWidget(self.label_31)
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.verticalLayout_24.addWidget(self.doubleSpinBox_18)
        self.horizontalLayout_7.addLayout(self.verticalLayout_24)
        self.pushButton_camera_5 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_5.setObjectName("pushButton_camera_5")
        self.horizontalLayout_7.addWidget(self.pushButton_camera_5, 0, QtCore.Qt.AlignBottom)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(180, 135))
        self.label_10.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setText("")
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_32 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_25.addWidget(self.label_32)
        self.spinBox_19 = QtWidgets.QSpinBox(self.horizontalWidget)
        self.spinBox_19.setObjectName("spinBox_19")
        self.verticalLayout_25.addWidget(self.spinBox_19)
        self.horizontalLayout_8.addLayout(self.verticalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_33 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_26.addWidget(self.label_33)
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_20.setObjectName("doubleSpinBox_20")
        self.verticalLayout_26.addWidget(self.doubleSpinBox_20)
        self.horizontalLayout_8.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_34 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_27.addWidget(self.label_34)
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.doubleSpinBox_21.setObjectName("doubleSpinBox_21")
        self.verticalLayout_27.addWidget(self.doubleSpinBox_21)
        self.horizontalLayout_8.addLayout(self.verticalLayout_27)
        self.pushButton_camera_6 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_camera_6.setObjectName("pushButton_camera_6")
        self.horizontalLayout_8.addWidget(self.pushButton_camera_6, 0, QtCore.Qt.AlignBottom)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.label_12 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(180, 135))
        self.label_12.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid #1de9b6;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setText("")
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
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
        self.pushButton_outputFolder = QtWidgets.QPushButton(self.verticalWidget_4)
        self.pushButton_outputFolder.setObjectName("pushButton_outputFolder")
        self.verticalLayout_4.addWidget(self.pushButton_outputFolder)
        self.display_path = QtWidgets.QLabel(self.verticalWidget_4)
        self.display_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.display_path.setFrameShadow(QtWidgets.QFrame.Plain)
        self.display_path.setWordWrap(True)
        self.display_path.setObjectName("display_path")
        self.verticalLayout_4.addWidget(self.display_path)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem6)
        self.label_13 = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_13.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalWidget_4)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        spacerItem7 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.listWidget_log = QtWidgets.QListWidget(self.verticalWidget_4)
        self.listWidget_log.setMinimumSize(QtCore.QSize(0, 200))
        self.listWidget_log.setMaximumSize(QtCore.QSize(1000, 400))
        self.listWidget_log.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_log.setProperty("isWrapping", True)
        self.listWidget_log.setWordWrap(True)
        self.listWidget_log.setObjectName("listWidget_log")
        self.verticalLayout_4.addWidget(self.listWidget_log)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout.addWidget(self.verticalWidget_4)
        self.horizontalLayout_9.addWidget(self.horizontalWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RAPIID v1.0"))
        self.label.setText(_translate("MainWindow", "Dorsal Camera"))
        self.label_14.setText(_translate("MainWindow", "Aperture"))
        self.label_15.setText(_translate("MainWindow", "Shutterspeed"))
        self.label_16.setText(_translate("MainWindow", "ISO"))
        self.pushButton_camera_1.setText(_translate("MainWindow", "Start live view"))
        self.label_3.setText(_translate("MainWindow", "Lateral Camera"))
        self.label_20.setText(_translate("MainWindow", "Aperture"))
        self.label_21.setText(_translate("MainWindow", "Shutterspeed"))
        self.label_22.setText(_translate("MainWindow", "ISO"))
        self.pushButton_camera_2.setText(_translate("MainWindow", "Start live view"))
        self.camera_3_label.setText(_translate("MainWindow", "Label Camera 1"))
        self.camera_3_exposure_label.setText(_translate("MainWindow", "Exposure time (us)"))
        self.camera_3_gain_label.setText(_translate("MainWindow", "Gain level (dB)"))
        self.camera_3_gamma_label.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_3.setText(_translate("MainWindow", "Start live view"))
        self.label_7.setText(_translate("MainWindow", "Label Camera 2"))
        self.label_23.setText(_translate("MainWindow", "Exposure time (us)"))
        self.label_24.setText(_translate("MainWindow", "Gain level (dB)"))
        self.label_25.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_4.setText(_translate("MainWindow", "Start live view"))
        self.label_9.setText(_translate("MainWindow", "Label Camera 3"))
        self.label_29.setText(_translate("MainWindow", "Exposure time (us)"))
        self.label_30.setText(_translate("MainWindow", "Gain level (dB)"))
        self.label_31.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_5.setText(_translate("MainWindow", "Start live view"))
        self.label_11.setText(_translate("MainWindow", "Label Camera 4"))
        self.label_32.setText(_translate("MainWindow", "Exposure time (us)"))
        self.label_33.setText(_translate("MainWindow", "Gain level (dB)"))
        self.label_34.setText(_translate("MainWindow", "Gamma correction"))
        self.pushButton_camera_6.setText(_translate("MainWindow", "Start live view"))
        self.pushButton_load_config.setText(_translate("MainWindow", "Load config file..."))
        self.pushButton_outputFolder.setText(_translate("MainWindow", "Output folder..."))
        self.display_path.setText(_translate("MainWindow", "Path"))
        self.label_13.setText(_translate("MainWindow", "NZAC accession no."))
        self.pushButton.setText(_translate("MainWindow", "Capture image set"))
        self.label_2.setText(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
