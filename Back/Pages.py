from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (
    QDockWidget,
    QApplication,
    QLabel,
    QTextEdit,
    QPushButton,
    QTableWidgetItem,
)

from AudioRecorder import Recorder
import threading


class mainWindow(QDockWidget):
    def __init__(self, widgetManager, changeWindow):
        super(mainWindow, self).__init__()
        self.widgetManager = widgetManager
        self.changeWindow = changeWindow
        # load the ui file
        uic.loadUi("../Front/main.ui", self)

        # set background image
        self.background.setStyleSheet(
            f"background-image: url(../Front/Images/Main.png);"
        )

        # Assign functions
        self.StartSession.clicked.connect(self.switchWindow)

    # change window
    def switchWindow(self):
        newWindow = registerWindow(self.widgetManager, self.changeWindow)
        self.changeWindow(self.widgetManager, newWindow)


class registerWindow(QDockWidget):
    def __init__(self, widgetManager, changeWindow):
        super(registerWindow, self).__init__()
        self.widgetManager = widgetManager
        self.changeWindow = changeWindow

        #todo gen error message
        self.msg_Error.setText("")
        # load the ui file
        uic.loadUi("../Front/register.ui", self)

        # set background image
        self.background.setStyleSheet(
            f"background-image: url(../Front/Images/Register.png);"
        )

        # Assign functions
        self.btn_Cancel.clicked.connect(self.cancelSession)
        self.btn_Clear.clicked.connect(self.clearSesssion)
        self.btn_StartRecord.clicked.connect(self.startRecordSession)

    # change window
    def cancelSession(self):
        # go back
        self.widgetManager.removeWidget(self)

        print("go back")

    # isChecked

    def clearSesssion(self):
        self.txtEdit_Name.clear()
        self.txtEdit_Email.clear()
        self.txtEdit_Phone.clear()
        self.txtEdit_Age.clear()

        self.radbtn_male.setChecked(False)
        self.radbtn_female.setChecked(False)
        print("clear")

    def startRecordSession(self):

        # check all fields
        name = self.txtEdit_Name.toPlainText()
        email = self.txtEdit_Email.toPlainText()
        phone = self.txtEdit_Phone.toPlainText()
        age = self.txtEdit_Age.toPlainText()

        # Todo: add more validation
        if self.radbtn_male.isChecked() and self.radbtn_female.isChecked():
            return

        gender = self.radbtn_male.isChecked() or self.radbtn_female.isChecked()

        # database

        # all good then start recording

        newWindow = SessionWindow(self.widgetManager, self.changeWindow)
        self.changeWindow(self.widgetManager, newWindow)
        print("start recording")


class SessionWindow(QDockWidget):
    def __init__(self, widgetManager):
        super(SessionWindow, self).__init__()
        self.widgetManager = widgetManager
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
        if self.part1_IsRecorded and self.part2_IsRecorded:
            self.widgetManager.setCurrentWidget()
