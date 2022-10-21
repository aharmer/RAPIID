import sys
import os
from pathlib import Path
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.rapiid_GUI import Ui_MainWindow  # importing main window of the GUI
import scripts.ymlRW as ymlRW
import cv2
from qt_material import apply_stylesheet


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

        self.setWindowIcon(QtGui.QIcon(str(Path.cwd().joinpath("images", "RAPIID_icon.png"))))

        self.exit_program = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # start thread pool
        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # Set initial camera variables and buttons
        self.liveView = [False, False, False, False, False, False]
        self.camera_type = None
        self.camera_0_model = None
        self.camera_1_model = None
        self.camera_2_model = None
        self.camera_3_model = None
        self.camera_4_model = None
        self.camera_5_model = None
        self.file_format = ".jpg"

        # Assign camera control features to ui
        self.ui.pushButton_camera_0.pressed.connect(lambda: self.begin_live_view(cam_id = self.ui.camera_0, select_cam = 0, button_id = self.ui.pushButton_camera_0))
        self.ui.spinBox_camera_0_exposure.valueChanged.connect(lambda: self.set_exposure_manual(lab_id = self.ui.camera_0_exposure_label, select_cam = 0, spin_id = self.ui.spinBox_camera_0_exposure))
        self.ui.doubleSpinBox_camera_0_gain.valueChanged.connect(lambda: self.set_gain_manual(lab_id = self.ui.camera_0_gain_label, select_cam = 0, dspin_id = self.ui.doubleSpinBox_camera_0_gain))
        self.ui.doubleSpinBox_camera_0_gamma.valueChanged.connect(lambda: self.set_gamma(lab_id = self.ui.camera_0_gamma_label, select_cam = 0, dspin_id = self.ui.doubleSpinBox_camera_0_gamma))

        self.ui.pushButton_camera_1.pressed.connect(lambda: self.begin_live_view(cam_id = self.ui.camera_1, select_cam = 1, button_id = self.ui.pushButton_camera_1))
        self.ui.spinBox_camera_1_exposure.valueChanged.connect(lambda: self.set_exposure_manual(lab_id = self.ui.camera_1_exposure_label, select_cam = 1, spin_id = self.ui.spinBox_camera_1_exposure))
        self.ui.doubleSpinBox_camera_1_gain.valueChanged.connect(lambda: self.set_gain_manual(lab_id = self.ui.camera_1_gain_label, select_cam = 1, dspin_id = self.ui.doubleSpinBox_camera_1_gain))
        self.ui.doubleSpinBox_camera_1_gamma.valueChanged.connect(lambda: self.set_gamma(lab_id = self.ui.camera_1_gamma_label, select_cam = 1, dspin_id = self.ui.doubleSpinBox_camera_1_gamma))

        self.ui.pushButton_camera_2.pressed.connect(lambda: self.begin_live_view(cam_id = self.ui.camera_2, select_cam = 2, button_id = self.ui.pushButton_camera_2))
        self.ui.spinBox_camera_2_exposure.valueChanged.connect(lambda: self.set_exposure_manual(lab_id = self.ui.camera_2_exposure_label, select_cam = 2, spin_id = self.ui.spinBox_camera_2_exposure))
        self.ui.doubleSpinBox_camera_2_gain.valueChanged.connect(lambda: self.set_gain_manual(lab_id = self.ui.camera_2_gain_label, select_cam = 2, dspin_id = self.ui.doubleSpinBox_camera_2_gain))
        self.ui.doubleSpinBox_camera_2_gamma.valueChanged.connect(lambda: self.set_gamma(lab_id = self.ui.camera_2_gamma_label, select_cam = 2, dspin_id = self.ui.doubleSpinBox_camera_2_gamma))

        self.ui.pushButton_camera_3.pressed.connect(lambda: self.begin_live_view(cam_id = self.ui.camera_3, select_cam = 3, button_id = self.ui.pushButton_camera_3))
        self.ui.spinBox_camera_3_exposure.valueChanged.connect(lambda: self.set_exposure_manual(lab_id = self.ui.camera_3_exposure_label, select_cam = 3, spin_id = self.ui.spinBox_camera_3_exposure))
        self.ui.doubleSpinBox_camera_3_gain.valueChanged.connect(lambda: self.set_gain_manual(lab_id = self.ui.camera_3_gain_label, select_cam = 3, dspin_id = self.ui.doubleSpinBox_camera_3_gain))
        self.ui.doubleSpinBox_camera_3_gamma.valueChanged.connect(lambda: self.set_gamma(lab_id = self.ui.camera_3_gamma_label, select_cam = 3, dspin_id = self.ui.doubleSpinBox_camera_3_gamma))

        self.ui.pushButton_camera_4.pressed.connect(lambda: self.begin_live_view(cam_id = self.ui.camera_4, select_cam = 4, button_id = self.ui.pushButton_camera_4))
        self.ui.spinBox_camera_4_exposure.valueChanged.connect(lambda: self.set_exposure_manual(lab_id = self.ui.camera_4_exposure_label, select_cam = 4, spin_id = self.ui.spinBox_camera_4_exposure))
        self.ui.doubleSpinBox_camera_4_gain.valueChanged.connect(lambda: self.set_gain_manual(lab_id = self.ui.camera_4_gain_label, select_cam = 4, dspin_id = self.ui.doubleSpinBox_camera_4_gain))
        self.ui.doubleSpinBox_camera_4_gamma.valueChanged.connect(lambda: self.set_gamma(lab_id = self.ui.camera_4_gamma_label, select_cam = 4, dspin_id = self.ui.doubleSpinBox_camera_4_gamma))

        self.ui.pushButton_camera_5.pressed.connect(lambda: self.begin_live_view(cam_id = self.ui.camera_5, select_cam = 5, button_id = self.ui.pushButton_camera_5))
        self.ui.spinBox_camera_5_exposure.valueChanged.connect(lambda: self.set_exposure_manual(lab_id = self.ui.camera_5_exposure_label, select_cam = 5, spin_id = self.ui.spinBox_camera_5_exposure))
        self.ui.doubleSpinBox_camera_5_gain.valueChanged.connect(lambda: self.set_gain_manual(lab_id = self.ui.camera_5_gain_label, select_cam = 5, dspin_id = self.ui.doubleSpinBox_camera_5_gain))
        self.ui.doubleSpinBox_camera_5_gamma.valueChanged.connect(lambda: self.set_gamma(lab_id = self.ui.camera_5_gamma_label, select_cam = 5, dspin_id = self.ui.doubleSpinBox_camera_5_gamma))

        self.ui.pushButton_capture.pressed.connect(self.capture_set)

        # Find and initialise FLIR cameras, if attached
        try:
            from scripts.rapiid_FLIR import customFLIR
            self.FLIR = customFLIR()
            
            if len(self.FLIR.cam_list_raw) == 0:
                msg = QMessageBox()
                msg.setWindowTitle("RAPIID Dialog")
                msg.setText("No cameras attached!\nConnect cameras and restart the app.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                msg.buttonClicked.connect(self.closeApp())

            # Camera 0
            if self.FLIR.cam_list[0] is not None:
                try: 
                    self.FLIR.initialise_camera(select_cam = 0)
                    self.log_info("Dorsal camera successfully initialised.")
                    self.ui.camera_0.setText("Dorsal camera successfully initialised.")
                    self.camera_type = "FLIR"
                    self.camera_0_model = 'Blackfly S BFS-U3-200S6C'
                    self.FLIR0_found = True
                    # self.FLIR_image_queue = []
                except IndexError:
                    message0 = "Dorsal camera not initialised!"
                    self.log_info(message0)
                    self.ui.camera_0.setText("Dorsal camera not initialised!")
                    print(message0)
                    self.FLIR0_found = False
                    self.disable_inputs(cam_id = 0)
            else:
                self.FLIR0_found = False
                print("Dorsal camera not connected!")
                self.ui.camera_0.setText("Dorsal camera not connected.")

            # Camera 1
            if self.FLIR.cam_list[1] is not None:
                try: 
                    self.FLIR.initialise_camera(select_cam = 1)
                    self.log_info("Lateral camera successfully initialised.")
                    self.ui.camera_1.setText("Lateral camera successfully initialised.")
                    self.camera_type = "FLIR"
                    self.camera_1_model = 'Blackfly S BFS-U3-200S6C'
                    self.FLIR1_found = True
                    # self.FLIR_image_queue = []
                except IndexError:
                    message1 = "Lateral camera not initialised!"
                    self.log_info(message1)
                    self.ui.camera_1.setText("Lateral camera not initialised!")
                    print(message1)
                    self.FLIR1_found = False
                    self.disable_inputs(cam_id = 1)
            else:
                self.FLIR1_found = False
                print("Lateral camera not connected!")
                self.ui.camera_1.setText("Lateral camera not connected.")
            
            # Camera 2
            if self.FLIR.cam_list[2] is not None:
                try: 
                    self.FLIR.initialise_camera(select_cam = 2)
                    self.log_info("Label camera 1 successfully initialised.")
                    self.ui.camera_2.setText("Label camera 1 successfully initialised.")
                    self.camera_type = "FLIR"
                    self.camera_2_model = 'Blackfly S BFS-U3-200S6M'
                    self.FLIR2_found = True
                    # self.FLIR_image_queue = []
                except IndexError:
                    message2 = "Label camera 1 not initialised!"
                    self.log_info(message2)
                    self.ui.camera_2.setText("Label camera 1 not initialised!")
                    print(message2)
                    self.FLIR2_found = False
                    self.disable_inputs(cam_id = 2)
            else:
                self.FLIR2_found = False
                print("Label camera 1 not connected!")
                self.ui.camera_2.setText("Label camera 1 not connected.")

            # Camera 3
            if self.FLIR.cam_list[3] is not None:
                try: 
                    self.FLIR.initialise_camera(select_cam = 3)
                    self.log_info("Label camera 2 successfully initialised.")
                    self.ui.camera_3.setText("Label camera 2 successfully initialised.")
                    self.camera_type = "FLIR"
                    self.camera_3_model = 'Blackfly S BFS-U3-200S6M'
                    self.FLIR3_found = True
                    # self.FLIR_image_queue = []
                except IndexError:
                    message3 = "Label camera 2 not initialised!"
                    self.log_info(message2)
                    self.ui.camera_3.setText("Label camera 2 not initialised!")
                    print(message3)
                    self.FLIR3_found = False
                    self.disable_inputs(cam_id = 3)
            else:
                self.FLIR3_found = False
                print("Label camera 2 not connected!")
                self.ui.camera_3.setText("Label camera 2 not connected.")

            # Camera 4
            if self.FLIR.cam_list[4] is not None:
                try: 
                    self.FLIR.initialise_camera(select_cam = 4)
                    self.log_info("Label camera 3 successfully initialised.")
                    self.ui.camera_4.setText("Label camera 3 successfully initialised.")
                    self.camera_type = "FLIR"
                    self.camera_4_model = 'Blackfly S BFS-U3-200S6M'
                    self.FLIR4_found = True
                    # self.FLIR_image_queue = []
                except IndexError:
                    message4 = "Label camera 3 not initialised!"
                    self.log_info(message4)
                    self.ui.camera_4.setText("Label camera 3 not initialised!")
                    print(message4)
                    self.FLIR4_found = False
                    self.disable_inputs(cam_id = 4)
            else:
                self.FLIR4_found = False
                print("Label camera 3 not connected!")
                self.ui.camera_4.setText("Label camera 3 not connected.")

            # Camera 5
            if self.FLIR.cam_list[5] is not None:
                try: 
                    self.FLIR.initialise_camera(select_cam = 5)
                    self.log_info("Label camera 4 successfully initialised.")
                    self.ui.camera_5.setText("Label camera 4 successfully initialised.")
                    self.camera_type = "FLIR"
                    self.camera_5_model = 'Blackfly S BFS-U3-200S6M'
                    self.FLIR5_found = True
                    # self.FLIR_image_queue = []
                except IndexError:
                    message5 = "Label camera 4 not initialised!"
                    self.log_info(message5)
                    self.ui.camera_5.setText("Label camera 4 not initialised!")
                    print(message5)
                    self.FLIR5_found = False
                    self.disable_inputs(cam_id = 5)
            else:
                self.FLIR5_found = False
                print("Label camera 4 not connected!")
                self.ui.camera_5.setText("Label camera 4 not connected.")

        except ModuleNotFoundError:
            message = "PYSPIN has not been installed - Disabling FLIR camera inputs"
            self.log_info(message)
            print(message)
            # self.FLIR_found = False
            self.disable_inputs(cam_id = 0)
            self.disable_inputs(cam_id = 1)
            self.disable_inputs(cam_id = 2)
            self.disable_inputs(cam_id = 3)
            self.disable_inputs(cam_id = 4)
            self.disable_inputs(cam_id = 5)

        # Select output folder
        self.output_location = str(Path.cwd())
        self.update_output_location()
        self.ui.pushButton_outputFolder.pressed.connect(self.set_output_location)
        self.output_location_folder = Path(self.output_location)

        # Config file
        self.config = self.get_default_values()
        self.ui.lineEdit_project.setText(self.config["general"]["project_name"])
        self.loadedConfig = False
        self.ui.pushButton_load_config.pressed.connect(self.loadConfig)
        self.ui.pushButton_writeConfig.pressed.connect(self.writeConfig)

        self.exif_data = self.config["exif_data"]

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

    def log_info(self, info):
        now = datetime.datetime.now()
        self.ui.listWidget_log.addItem(now.strftime("%H:%M:%S") + " " + info)
        self.ui.listWidget_log.sortItems(QtCore.Qt.DescendingOrder)

    def update_live_view(self, cam_id, select_cam, progress_callback):
        while self.liveView[select_cam] and self.camera_type == "FLIR":
            try:
                img = self.FLIR.live_view(select_cam)

                live_img = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                live_img_pixmap = QtGui.QPixmap.fromImage(live_img)

                # Setup pixmap with the acquired image
                live_img_scaled = live_img_pixmap.scaled(cam_id.width(),
                                                         cam_id.height(),
                                                         QtCore.Qt.KeepAspectRatio)
                # Set the pixmap onto the label
                cam_id.setPixmap(live_img_scaled)
                # Align the label to center
                cam_id.setAlignment(QtCore.Qt.AlignCenter)
            except AttributeError:
                print("Live view ended")
        cam_id.setText("Live view disabled.")

    def begin_live_view(self, cam_id, select_cam, button_id):
        if not self.liveView[select_cam]:
            self.log_info("Began camera live view.")
            button_id.setText("Stop Live View")
            self.liveView[select_cam] = True
            
            worker = Worker(self.update_live_view, cam_id, select_cam)
            self.threadpool.start(worker)

        else:
            cam_id.setText("Live view disabled.")
            button_id.setText("Start live view")
            self.log_info("Ended camera live view")
            self.liveView[select_cam] = False

    def set_exposure_manual(self, lab_id, select_cam, spin_id):
        lab_id.setEnabled(True)
        spin_id.setEnabled(True)
        value = spin_id.value()
        if value is not None:
            self.log_info("Exposure time set to " + str(value) + " [us]")
            self.FLIR.configure_exposure(select_cam, exposure = float(value))

    def set_gain_manual(self, lab_id, select_cam, dspin_id):
        lab_id.setEnabled(True)
        dspin_id.setEnabled(True)
        value = dspin_id.value()
        if value is not None:
            self.log_info("Gain level set to " + str(value) + " [dB]")
            self.FLIR.set_gain(select_cam, gain = float(value))

    def set_gamma(self, lab_id, select_cam, dspin_id):
        lab_id.setEnabled(True)
        dspin_id.setEnabled(True)
        value = dspin_id.value()
        if value is not None:
            self.log_info("Gamma set to " + str(value))
            self.FLIR.set_gamma(select_cam, gamma = float(value))

    def capture_set(self):
        self.output_location_folder = Path(self.output_location).joinpath(self.ui.lineEdit_project.text()).joinpath(self.ui.lineEdit_accession.text())
        if os.path.exists(self.output_location_folder):
            self.show_popup()

        else:
            self.ui.pushButton_capture.setEnabled(False)
            self.capture_image(select_cam = 0, tag = "_dorsal")
            self.capture_image(select_cam = 1, tag = "_lateral")
            self.capture_image(select_cam = 2, tag = "_label_1")
            self.capture_image(select_cam = 3, tag = "_label_2")
            self.capture_image(select_cam = 4, tag = "_label_3")
            self.capture_image(select_cam = 5, tag = "_label_4")
            self.ui.pushButton_capture.setEnabled(True)

    def show_popup(self):
        button = QMessageBox.question(self, "RAPIID Dialog", "A folder with this accession number already exists!\nDo you want to overwrite the existing files?")
        if button == QMessageBox.Yes:
            self.popup_button()

    def popup_button(self):
        self.ui.pushButton_capture.setEnabled(False)
        self.capture_image(select_cam = 0, tag = "_dorsal")
        self.capture_image(select_cam = 1, tag = "_lateral")
        self.capture_image(select_cam = 2, tag = "_label_1")
        self.capture_image(select_cam = 3, tag = "_label_2")
        self.capture_image(select_cam = 4, tag = "_label_3")
        self.capture_image(select_cam = 5, tag = "_label_4")
        self.ui.pushButton_capture.setEnabled(True)

    def capture_image(self, select_cam, tag):
        now = datetime.datetime.now()
        self.create_output_folders()
        file_name = str(self.output_location_folder.joinpath(self.ui.lineEdit_accession.text() + tag + self.file_format))
        self.FLIR.capture_image(select_cam, img_name = file_name)
        self.log_info("Captured " + str(self.ui.lineEdit_accession.text() + tag + self.file_format))

    def create_output_folders(self):
        self.output_location_folder = Path(self.output_location).joinpath(self.ui.lineEdit_project.text()).joinpath(self.ui.lineEdit_accession.text())
        if not os.path.exists(self.output_location_folder):
            os.makedirs(self.output_location_folder)
            self.log_info("Created folder: " + str(self.ui.lineEdit_project.text() + self.ui.lineEdit_accession.text()))

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
                QtWidgets.QMessageBox.critical(self, "Failed to load " + str(config_location.name), "The selected config file was generated for a different camera type!")
                return

            # project name
            self.ui.lineEdit_project.setText(config["general"]["project_name"])

            # camera_settings:
            if config["general"]["camera_type"] == "FLIR":
                self.ui.spinBox_camera_0_exposure.setValue(config["camera_settings"]["camera_0"]["exposure_time"])
                self.ui.doubleSpinBox_camera_0_gain.setValue(config["camera_settings"]["camera_0"]["gain_level"])
                self.ui.doubleSpinBox_camera_0_gamma.setValue(config["camera_settings"]["camera_0"]["gamma"])
                self.ui.spinBox_camera_1_exposure.setValue(config["camera_settings"]["camera_1"]["exposure_time"])
                self.ui.doubleSpinBox_camera_1_gain.setValue(config["camera_settings"]["camera_1"]["gain_level"])
                self.ui.doubleSpinBox_camera_1_gamma.setValue(config["camera_settings"]["camera_1"]["gamma"])
                self.ui.spinBox_camera_2_exposure.setValue(config["camera_settings"]["camera_2"]["exposure_time"])
                self.ui.doubleSpinBox_camera_2_gain.setValue(config["camera_settings"]["camera_2"]["gain_level"])
                self.ui.doubleSpinBox_camera_2_gamma.setValue(config["camera_settings"]["camera_2"]["gamma"])
                self.ui.spinBox_camera_3_exposure.setValue(config["camera_settings"]["camera_3"]["exposure_time"])
                self.ui.doubleSpinBox_camera_3_gain.setValue(config["camera_settings"]["camera_3"]["gain_level"])
                self.ui.doubleSpinBox_camera_3_gamma.setValue(config["camera_settings"]["camera_3"]["gamma"])
                self.ui.spinBox_camera_4_exposure.setValue(config["camera_settings"]["camera_4"]["exposure_time"])
                self.ui.doubleSpinBox_camera_4_gain.setValue(config["camera_settings"]["camera_4"]["gain_level"])
                self.ui.doubleSpinBox_camera_4_gamma.setValue(config["camera_settings"]["camera_4"]["gamma"])
                self.ui.spinBox_camera_5_exposure.setValue(config["camera_settings"]["camera_5"]["exposure_time"])
                self.ui.doubleSpinBox_camera_5_gain.setValue(config["camera_settings"]["camera_5"]["gain_level"])
                self.ui.doubleSpinBox_camera_5_gamma.setValue(config["camera_settings"]["camera_5"]["gamma"])

            # meta data (exif)
            self.exif_camera_0 = config["exif_data"]["camera_0"]
            self.exif_camera_1 = config["exif_data"]["camera_1"]
            self.exif_camera_2 = config["exif_data"]["camera_2"]
            self.exif_camera_3 = config["exif_data"]["camera_3"]
            self.exif_camera_4 = config["exif_data"]["camera_4"]
            self.exif_camera_5 = config["exif_data"]["camera_5"]

            self.loadedConfig = True
            self.log_info("Loaded config file successfully!")
            print(config)

    def writeConfig(self):
        self.output_location_folder = Path(self.output_location).joinpath(self.ui.lineEdit_project.text())
        if not os.path.exists(self.output_location_folder):
            os.makedirs(self.output_location_folder)
            self.log_info("Created folder: " + str(self.ui.lineEdit_project.text()))

        config = {'general': {'project_name': self.ui.lineEdit_project.text(),
                              'camera_type': self.camera_type,
                              'camera_0_model': self.camera_0_model,
                              'camera_1_model': self.camera_1_model,
                              'camera_2_model': self.camera_2_model,
                              'camera_3_model': self.camera_3_model,
                              'camera_4_model': self.camera_4_model,
                              'camera_5_model': self.camera_5_model,
                              },
                  'camera_settings': {'camera_0': {'exposure_time': self.ui.spinBox_camera_0_exposure.value(),
                                                  'gain_level': self.ui.doubleSpinBox_camera_0_gain.value(),
                                                  'gamma': self.ui.doubleSpinBox_camera_0_gamma.value(),
                                                  },
                                      'camera_1': {'exposure_time': self.ui.spinBox_camera_1_exposure.value(),
                                                  'gain_level': self.ui.doubleSpinBox_camera_1_gain.value(),
                                                  'gamma': self.ui.doubleSpinBox_camera_1_gamma.value(),
                                                  },
                                      'camera_2': {'exposure_time': self.ui.spinBox_camera_2_exposure.value(),
                                                  'gain_level': self.ui.doubleSpinBox_camera_2_gain.value(),
                                                  'gamma': self.ui.doubleSpinBox_camera_2_gamma.value(),
                                                  },
                                      'camera_3': {'exposure_time': self.ui.spinBox_camera_3_exposure.value(),
                                                  'gain_level': self.ui.doubleSpinBox_camera_3_gain.value(),
                                                  'gamma': self.ui.doubleSpinBox_camera_3_gamma.value(),
                                                  },
                                      'camera_4': {'exposure_time': self.ui.spinBox_camera_4_exposure.value(),
                                                  'gain_level': self.ui.doubleSpinBox_camera_4_gain.value(),
                                                  'gamma': self.ui.doubleSpinBox_camera_4_gamma.value(),
                                                  },
                                      'camera_5': {'exposure_time': self.ui.spinBox_camera_5_exposure.value(),
                                                  'gain_level': self.ui.doubleSpinBox_camera_5_gain.value(),
                                                  'gamma': self.ui.doubleSpinBox_camera_5_gamma.value(),
                                                  },    
                                      },
                  'exif_data': self.exif_data
                  }

        ymlRW.write_config_file(config, Path(self.output_location_folder))
        self.log_info("Exported config file successfully!")

    def get_default_values(self):
        # WARNING! THESE SETTINGS ARE SPECIFIC TO THE CAMERA USED DURING DEVELOPMENT
        # OF THE SCANNER AND WILL LIKELY NOT APPLY TO YOUR SETUP
        config = {'general': {'project_name': 'untitled_project'},
                       'exif_data': {'camera_0': {'Make': 'FLIR',
                                                  'Model': 'BFS-U3-200S6C-C',
                                                  'SerialNumber': '21188171',
                                                  'Lens': 'MPZ',
                                                  'CameraSerialNumber': '21188171',
                                                  'LensManufacturer': 'Computar',
                                                  'LensModel': '75.0 f / 3.1',
                                                  'FocalLength': '75.0',
                                                  'FocalLengthIn35mmFormat': '203.0'},
                                     'camera_1': {'Make': 'FLIR',
                                                  'Model': 'BFS-U3-200S6C-C',
                                                  'SerialNumber': '00000000',
                                                  'Lens': 'MPZ',
                                                  'CameraSerialNumber': '00000000',
                                                  'LensManufacturer': 'Computar',
                                                  'LensModel': '75.0 f / 3.1',
                                                  'FocalLength': '75.0',
                                                  'FocalLengthIn35mmFormat': '203.0'},
                                     'camera_2': {'Make': 'FLIR',
                                                  'Model': 'BFS-U3-200S6M-C',
                                                  'SerialNumber': '22491455',
                                                  'Lens': 'MPZ',
                                                  'CameraSerialNumber': '22491455',
                                                  'LensManufacturer': 'Computar',
                                                  'LensModel': '50.0 f / 2.4',
                                                  'FocalLength': '50.0',
                                                  'FocalLengthIn35mmFormat': '135.0'},
                                     'camera_3': {'Make': 'FLIR',
                                                  'Model': 'BFS-U3-200S6M-C',
                                                  'SerialNumber': '22497398',
                                                  'Lens': 'MPZ',
                                                  'CameraSerialNumber': '22497398',
                                                  'LensManufacturer': 'Computar',
                                                  'LensModel': '50.0 f / 2.4',
                                                  'FocalLength': '50.0',
                                                  'FocalLengthIn35mmFormat': '135.0'},
                                     'camera_4': {'Make': 'FLIR',
                                                  'Model': 'BFS-U3-200S6M-C',
                                                  'SerialNumber': '22457938',
                                                  'Lens': 'MPZ',
                                                  'CameraSerialNumber': '22457938',
                                                  'LensManufacturer': 'Computar',
                                                  'LensModel': '50.0 f / 2.4',
                                                  'FocalLength': '50.0',
                                                  'FocalLengthIn35mmFormat': '135.0'},
                                     'camera_5': {'Make': 'FLIR',
                                                  'Model': 'BFS-U3-200S6M-C',
                                                  'SerialNumber': '22385074',
                                                  'Lens': 'MPZ',
                                                  'CameraSerialNumber': '22385074',
                                                  'LensManufacturer': 'Computar',
                                                  'LensModel': '50.0 f / 2.4',
                                                  'FocalLength': '50.0',
                                                  'FocalLengthIn35mmFormat': '135.0'}
                                    }
                      }
        return config

    
    def disable_inputs(self, cam_id):
        self.ui.pushButton_camera_+cam_id.setEnabled(False)
        self.ui.spinBox_camera_+cam_id+_exposure.setEnabled(False)
        self.ui.doubleSpinBox_camera_+cam_id+_gain.setEnabled(False)
        self.ui.doubleSpinBox_camera_+cam_id+_gamma.setEnabled(False)
        self.ui.pushButton_capture.setEnabled(False)
        self.ui.pushButton_outputFolder.setEnabled(False)
        self.ui.pushButton_load_config.setEnabled(False)

    def enable_inputs(self, cam_id):
        self.ui.pushButton_camera_+cam_id.setEnabled(True)
        self.ui.spinBox_camera_+cam_id+_exposure.setEnabled(True)
        self.ui.doubleSpinBox_camera_+cam_id+_gain.setEnabled(True)
        self.ui.doubleSpinBox_camera_+cam_id+_gamma.setEnabled(True)
        self.ui.pushButton_capture.setEnabled(True)
        self.ui.pushButton_outputFolder.setEnabled(True)
        self.ui.pushButton_load_config.setEnabled(True)

    def closeApp(self):
        self.FLIR0_found = False
        self.FLIR1_found = False
        self.FLIR2_found = False
        self.FLIR3_found = False
        self.FLIR4_found = False
        self.FLIR5_found = False
        sys.exit()

    def closeEvent(self, event):
        # report the program is to be closed so threads can be exited
        self.exit_program = True

        # stop the live view if currently in use
        if self.liveView[0]:
            self.begin_live_view(cam_id = self.ui.camera_0, select_cam = 0, button_id = self.ui.pushButton_camera_0)  # sets live view false if already running
        if self.liveView[1]:
            self.begin_live_view(cam_id = self.ui.camera_1, select_cam = 1, button_id = self.ui.pushButton_camera_1)
        if self.liveView[2]:
            self.begin_live_view(cam_id = self.ui.camera_2, select_cam = 2, button_id = self.ui.pushButton_camera_2)
        if self.liveView[3]:
            self.begin_live_view(cam_id = self.ui.camera_3, select_cam = 3, button_id = self.ui.pushButton_camera_3)
        if self.liveView[4]:
            self.begin_live_view(cam_id = self.ui.camera_4, select_cam = 4, button_id = self.ui.pushButton_camera_4)
        if self.liveView[5]:
            self.begin_live_view(cam_id = self.ui.camera_5, select_cam = 5, button_id = self.ui.pushButton_camera_5)

        # release cameras
        if self.FLIR0_found:
            self.FLIR.exit_cam(0)
        if self.FLIR1_found:
            self.FLIR.exit_cam(1)
        if self.FLIR2_found:
            self.FLIR.exit_cam(2)
        if self.FLIR3_found:
            self.FLIR.exit_cam(3)
        if self.FLIR4_found:
            self.FLIR.exit_cam(4)
        if self.FLIR5_found:
            self.FLIR.exit_cam(5)

        self.FLIR.releasePySpin()

        print("Application Closed!")

# Initialise the app
app = QApplication(sys.argv)
UIWindow = UI()
apply_stylesheet(app, theme = 'dark_teal.xml')
app.exec_()