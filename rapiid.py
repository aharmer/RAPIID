import sys
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from rapiid_GUI import Ui_MainWindow  # importing main window of the GUI
from qt_material import apply_stylesheet
import cv2

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Select output folder
        self.output_location = str(Path.cwd())
        self.update_output_location()
        self.ui.pushButton_outputFolder.pressed.connect(self.set_output_location)
        self.output_location_folder = Path(self.output_location)

        # Connect camera 1        
        self.thread1 = thread1()
        self.thread1.start()
        self.thread1.imageUpdate.connect(self.imageUpdateSlot)

        # Show the app
        self.showMaximized()

    def set_output_location(self):
        new_location = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose output folder...", str(Path.cwd()))
                
        if new_location:
            self.output_location = new_location

        self.update_output_location()

    def update_output_location(self):
        self.ui.display_path.setText(self.output_location)

    def imageUpdateSlot(self, image):
        self.ui.camera_1.setPixmap(QPixmap.fromImage(image))


class thread1(QThread):
    imageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        capture = cv2.VideoCapture(1)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # flippedImage = cv2.flip(image, 1)
                # convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
                # pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                convertToQtFormat = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
                pic = convertToQtFormat
                self.imageUpdate.emit(pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

# Initialise the app
app = QApplication(sys.argv)
UIWindow = UI()
apply_stylesheet(app, theme = 'dark_teal.xml')
app.exec_()