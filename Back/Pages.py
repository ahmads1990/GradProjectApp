from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem

from AudioRecorder import Recorder
import threading


class mainWindow(QDockWidget):
    def __init__(self, widgetManager):
        super(mainWindow, self).__init__()
        self.widgetManager = widgetManager
        # load the ui file 
        uic.loadUi("../Front/main.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/Main.png);") 

        # Assign functions
        self.StartSession.clicked.connect(self.switchWindow)
        
    # change window   
    def switchWindow(self):
        newWindow = SessionWindow(widgetManager=self.widgetManager)
        print(self.widgetManager.count())
        self.widgetManager.addWidget(newWindow)
        print(self.widgetManager.count())
        self.widgetManager.setCurrentWidget(newWindow)
        


class SessionWindow(QDockWidget):
    def __init__(self,widgetManager):
        super(SessionWindow, self).__init__()
        self.widgetManager = widgetManager
        self.AudioRecorder = Recorder()

        # data
        self.part1_IsRecorded=False
        self.part1_Type='Letters'

        self.part2_IsRecorded=False
        self.part2_Type='Phrases'
        
        
        # load the ui file 
        uic.loadUi("../Front/Session.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/StartSession.png);") 

        # Assign functions
        self.RecordPart1_Btn.clicked.connect(self.recordPart1)
        self.RecordPart2_Btn.clicked.connect(self.recordPart2)

        self.EndSession_btn.clicked.connect(self.switchWindow)
        
    # Start recording 
    def recordPart1(self):
        if(not self.AudioRecorder.is_recording):
            threading.Thread(target=self.AudioRecorder.start_recording, 
                            args=(self.part1_Type,self.RecordPart1_Bar_Label,self.RecordPart1_Slider)).start()
        else:
            self.AudioRecorder.stop_recording()
    
    # Start recording   
    def recordPart2(self):
        if(not self.AudioRecorder.is_recording):
            threading.Thread(target=self.AudioRecorder.start_recording, 
                            args=(self.part2_Type,self.RecordPart2_Bar_Label,self.RecordPart2_Slider)).start()
        else:
            self.AudioRecorder.stop_recording()
    
    def switchWindow(self):
        if(self.part1_IsRecorded and self.part2_IsRecorded):
            self.widgetManager.setCurrentWidget()