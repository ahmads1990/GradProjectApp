from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from AudioRecorder import Recorder
import threading

class startSessionWindow(QDockWidget):
    def __init__(self,):
        super(startSessionWindow, self).__init__()
        # data
        self.part1_IsRecorded=False
        self.part1_Type='Letters'
        #self.isRecordedPart2=False
        self.AudioRecorder = Recorder()
        
        # load the ui file 
        uic.loadUi("../Front/startSession.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/StartSession.png);") 

        # Assign functions
        self.RecordPart1_Btn.clicked.connect(self.recordPart1)
        
    # change window   
    def recordPart1(self):
        if(not self.AudioRecorder.is_recording):
            threading.Thread(target=self.AudioRecorder.start_recording, 
                            args=(self.part1_Type,self.RecordPart1_Txt,self.horizontalSlider)).start()
        else:
            self.AudioRecorder.stop_recording()