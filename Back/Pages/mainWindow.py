from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem

class mainWindow(QDockWidget):
    def __init__(self,WidgetManager):
        super(mainWindow, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/main.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/Main.png);") 

        # Assign functions
        self.StartSession.clicked.connect(self.clicker)
        
    # change window   
    def clicker(self):
        #widget.setCurrentWidget(MainWindow)
        print("main")