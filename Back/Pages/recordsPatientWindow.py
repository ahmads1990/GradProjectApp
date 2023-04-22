from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem

class recordsPatientsWindow(QDockWidget):
    def __init__(self,):
        super(recordsPatientsWindow, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/recordsPatient.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/ShowRecordsPatient.png);") 

        # Assign functions
        #self.StartSession.clicked.connect(self.clicker)
        
    # change window   
    def clicker(self):
        #widget.setCurrentWidget(MainWindow)
        print("main")