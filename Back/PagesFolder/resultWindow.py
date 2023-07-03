from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from ModelHandler import ModelHandler
from Model.test_binary_model import load_model, test_model
import threading
import keras

class resultWindow(QDockWidget):
    def __init__(self, windowManager, modelHandler):
        super(resultWindow, self).__init__()
        self.windowManager = windowManager
        self.modelHandler = modelHandler

        self.sessionDto = None
        self.audioPath = "Audio/105-iau.wav"

        # load the ui file
        uic.loadUi("../Front/result.ui", self)
        
        # set background image
        self.background.setStyleSheet(
            f"background-image: url(../Front/Images/Results.png);"
        )
        
        # Assign functions
        self.GoBack.clicked.connect(self.switchWindowToMain)

    def setSessionDto(self, sessionDto):
        self.sessionDto = sessionDto
        
    def sendToModelPredict(self):
        print("-------------------")
        print(self.modelHandler.model)

        self.result = self.modelHandler.modelPredict(self.sessionDto)
        if(self.result == "pathology"):
            self.background.setStyleSheet(
            f"background-image: url(../Front/Images/ResultsPathology.png);")
        else:
            self.background.setStyleSheet(
            f"background-image: url(../Front/Images/ResultsHealthy.png);")

    # change window
    def switchWindowToMain(self):
        self.widgetManager.GoToMain()