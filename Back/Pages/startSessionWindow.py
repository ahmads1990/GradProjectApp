from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from AudioRecorder import Recorder
import threading

class SessionWindow(QDockWidget):
    def __init__(self, widgetManager, changeWindow):
        super(SessionWindow, self).__init__()
        self.widgetManager = widgetManager
        self.changeWindow = changeWindow
        self.AudioRecorder = Recorder()

        # data
        self.part1_IsRecorded = False
        self.part1_Type = "Letters"

        self.part2_IsRecorded = False
        self.part2_Type = "Phrases"

        # load the ui file
        uic.loadUi("../Front/Session.ui", self)

        # set background image
        self.background.setStyleSheet(
            f"background-image: url(../Front/Images/StartSession.png);"
        )

        # Assign functions
        self.RecordPart1_Btn.clicked.connect(self.recordPart1)
        self.RecordPart2_Btn.clicked.connect(self.recordPart2)

        self.EndSession_btn.clicked.connect(self.switchWindow)

    # Start recording
    def recordPart1(self):
        self.RecordPart1_Slider.setValue(int(0))
        if not self.AudioRecorder.is_recording:
            threading.Thread(
                target=self.AudioRecorder.start_recording,
                args=(
                    self.part1_Type,
                    self.RecordPart1_Bar_Label,
                    self.RecordPart1_Slider,
                ),
            ).start()
        else:
            self.AudioRecorder.stop_recording()

    # Start recording
    def recordPart2(self):
        self.RecordPart2_Slider.setValue(int(0))
        if not self.AudioRecorder.is_recording:
            threading.Thread(
                target=self.AudioRecorder.start_recording,
                args=(
                    self.part2_Type,
                    self.RecordPart2_Bar_Label,
                    self.RecordPart2_Slider,
                ),
            ).start()
        else:
            self.AudioRecorder.stop_recording()

    def switchWindow(self):
        #if self.part1_IsRecorded and self.part2_IsRecorded:
        self.widgetManager.removeWidget(self)
        self.widgetManager.removeWidget(int(self.widgetManager.count())-1)
