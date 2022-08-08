import sys
from pathlib import Path
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.rapiid_GUI import Ui_MainWindow  # importing main window of the GUI
from qt_material import apply_stylesheet
import scripts.ymlRW as ymlRW
import cv2

class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    '''
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)


class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.setWindowIcon(QtGui.QIcon(str(Path.cwd().joinpath("images", "RAPIID_icon2.png"))))

        self.exit_program = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # start thread pool
        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # search for cameras connected to the computer and supported by installed drivers
        self.liveView = False
        self.camera_type = "FLIR"
        self.camera_model = None
        self.file_format = ".tif"
        # self.DSLR_read_out = False
        self.ActiveSavingProcess = False

        self.ui.pushButton_camera_3.pressed.connect(self.begin_live_view)
        self.ui.spinBox_camera_3_exposure.valueChanged.connect(self.set_exposure_manual)

        # Find FLIR cameras, if attached
        try:
            from rapiid_FLIR import customFLIR
            self.FLIR = customFLIR()
            # camera needs to be initialised before use (self.cam.initialise_camera)
            # all detected FLIR cameras are listed in self.cam.device_names
            # by default, use the first camera found in the list
            self.cam = self.FLIR
            self.cam.initialise_camera(select_cam=0)
            # now retrieve the name of all found FLIR cameras and add them to the camera selection
            # for cam in self.cam.device_names:
            #     self.ui.comboBox_selectCamera.addItem(str(cam[0] + " ID: " + cam[1]))
            self.camera_type = "FLIR"
            # cam.device_names contains both model and serial number
            self.camera_model = self.cam.device_names[0][0]
            self.FLIR_found = True
            self.FLIR_image_queue = []
        except IndexError:
            message = "No FLIR camera found!"
            self.log_info(message)
            print(message)
            self.FLIR_found = False
            self.disable_FLIR_inputs()
        except ModuleNotFoundError:
            message = "PYSPIN has not been installed - Disabling FLIR camera inputs"
            self.log_info(message)
            print(message)
            self.FLIR_found = False
            self.disable_FLIR_inputs()

        # FLIR settings
        # self.ui.doubleSpinBox_exposureTime.valueChanged.connect(self.set_exposure_manual)

        # Select output folder
        self.output_location = str(Path.cwd())
        self.update_output_location()
        self.ui.pushButton_outputFolder.pressed.connect(self.set_output_location)
        self.output_location_folder = Path(self.output_location)

        # use config file
        self.loadedConfig = False
        self.ui.pushButton_load_config.pressed.connect(self.loadConfig)

        # Show the app
        self.showMaximized()

    def set_output_location(self):
        new_location = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose output folder...", str(Path.cwd()))
                
        if new_location:
            self.output_location = new_location
            self.log_info("Output location updated.")

        self.update_output_location()

    def update_output_location(self):
        self.ui.display_path.setText(self.output_location)

    # def imageUpdateSlot(self, image):
    #     self.ui.camera_3.setPixmap(QPixmap.fromImage(image))

    def log_info(self, info):
        now = datetime.datetime.now()
        self.ui.listWidget_log.addItem(now.strftime("%H:%M:%S") + " " + info)
        self.ui.listWidget_log.sortItems(QtCore.Qt.DescendingOrder)

    def update_live_view(self, progress_callback):
        while self.liveView and self.camera_type == "FLIR":
            try:
                img = self.cam.live_view()

                live_img = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                live_img_pixmap = QtGui.QPixmap.fromImage(live_img)

                # Setup pixmap with the acquired image
                live_img_scaled = live_img_pixmap.scaled(self.ui.camera_3.width(),
                                                         self.ui.camera_3.height(),
                                                         QtCore.Qt.KeepAspectRatio)
                # Set the pixmap onto the label
                self.ui.camera_3.setPixmap(live_img_scaled)
                # Align the label to center
                self.ui.camera_3.setAlignment(QtCore.Qt.AlignCenter)
            except AttributeError:
                print("Live view ended")
        self.ui.camera_3.setText("Live view disabled.")

    def begin_live_view(self):
        if not self.liveView:
            self.log_info("Began camera live view")
            self.ui.pushButton_camera_3.setText("Stop Live View")
            self.liveView = True

            worker = Worker(self.update_live_view)
            self.threadpool.start(worker)

        else:
            self.ui.camera_3.setText("Live view disabled.")
            self.ui.pushButton_camera_3.setText("Start live view")
            self.log_info("Ended camera live view")
            self.liveView = False

    def set_exposure_manual(self):
        # self.ui.label_exposureTime.setEnabled(True)
        self.ui.spinBox_camera_3_exposure.setEnabled(True)
        value = self.ui.spinBox_camera_3_exposure.value()
        if value is not None:
            self.log_info("Exposure time set to " + str(value) + " [us]")
            self.cam.configure_exposure(float(value))

    def loadConfig(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Load existing config file", str(Path.cwd()), "config file (*.yaml)")
        config_location = file[0]
        if config_location:
            # if a file has been selected, convert it into a Path object
            config_location = Path(config_location)
            config = ymlRW.read_config_file(config_location)

            # check if the camera type in the config file matches the connected/selected camera type
            if config["general"]["camera_type"] != self.camera_type:
                self.log_warning("The selected config file was generated for a different camera type!")
                QtWidgets.QMessageBox.critical(self, "Failed to load " + str(config_location.name),
                                               "The selected config file was generated for a different camera type!")
                return

            # camera_settings:

            if config["general"]["camera_type"] == "FLIR":
                # FLIR
                self.ui.doubleSpinBox_exposureTime.setValue(config["camera_settings"]["exposure_time"])
                self.ui.doubleSpinBox_gainLevel.setValue(config["camera_settings"]["gain_level"])
                self.ui.doubleSpinBox_gamma.setValue(config["camera_settings"]["gamma"])
                self.set_gamma()

            # else:
            #     # DSLR
            #     self.ui.comboBox_shutterSpeed.setCurrentIndex(
            #         self.ui.comboBox_shutterSpeed.findText(str(config["camera_settings"]["shutterspeed"])))
            #     self.ui.comboBox_aperture.setCurrentIndex(
            #         self.ui.comboBox_aperture.findText(str(config["camera_settings"]["aperture"])))
            #     self.ui.comboBox_iso.setCurrentIndex(
            #         self.ui.comboBox_iso.findText(str(config["camera_settings"]["iso"])))
            #     self.ui.comboBox_whiteBalance.setCurrentIndex(
            #         self.ui.comboBox_whiteBalance.findText(str(config["camera_settings"]["whitebalance"])))
            #     self.ui.comboBox_compression.setCurrentIndex(
            #         self.ui.comboBox_compression.findText(str(config["camera_settings"]["compression"])))

            # meta data (exif)
            self.exif = config["exif_data"]

            self.loadedConfig = True
            self.log_info("Loaded config-file successfully!")

            print(config)

    def closeEvent(self, event):
        # report the program is to be closed so threads can be exited
        self.exit_program = True

        # stop the live view if currently in use
        if self.liveView:
            self.begin_live_view()  # sets live view false if already running

        if self.camera_type == "FLIR":
            # release camera
            self.cam.exit_cam()

        print("Application Closed!")

# Initialise the app
app = QApplication(sys.argv)
UIWindow = UI()
apply_stylesheet(app, theme = 'dark_teal.xml')
app.exec_()