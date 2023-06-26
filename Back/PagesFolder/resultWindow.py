from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from ModelHandler import ModelHandler
from Model.test_binary_model import load_model, test_model
import threading
import keras

class resultWindow(QDockWidget):
    def __init__(self, windowManager, patientID):
        super(resultWindow, self).__init__()
        self.windowManager = windowManager
        self.modelHandler = None
        
        
        # load the ui file
        uic.loadUi("../Front/result.ui", self)
        
        # set background image
        self.background.setStyleSheet(
            f"background-image: url(../Front/Images/Results.png);"
        )
        
        # Assign functions
        self.GoBack.clicked.connect(self.switchWindowToMain)
        
        self.path = "./Model/Models/iau_phrase 99/model.h5"
        self.audioPath = "Audio/105-iau.wav"
        
        """
        self.model = threading.Thread(
                target= keras.models.load_model,
                args=(
                    self.path,
                ),
            ).start()
        print(self.model)
        """
        #self.model = load_model(path = "./Model/Models/iau_phrase 99/model.h5")
        
    def addModel(self):
        """
        self.modelHandler = ModelHandler()
        self.modelHandler.loadModel()
        """
        
    def startModel(self):
        
        print("-------------------")
        print(self.model)
        self.result = test_model(self.model, self.audioPath)
        if(self.result == "pathology"):
            self.background.setStyleSheet(
            f"background-image: url(../Front/Images/ResultsPathology.png);"
            )
        else:
            self.background.setStyleSheet(
            f"background-image: url(../Front/Images/ResultsHealthy.png);"
            )
    # change window
    def switchWindowToMain(self):
        self.widgetManager.GoToMain()