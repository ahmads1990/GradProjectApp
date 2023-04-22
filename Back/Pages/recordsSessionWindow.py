from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem

class recordsSessionWindow(QDockWidget):
    def __init__(self,):
        super(recordsSessionWindow, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/recordsSession.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/ShowRecordsSession.png);") 

        # Assign functions
        #self.StartSession.clicked.connect(self.clicker)
        
    # change window   
    def clicker(self):
        #widget.setCurrentWidget(MainWindow)
        print("main")