from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from Pages.registerWindow import registerWindow

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
        
        # Side
        self.btn_main.clicked.connect(self.switchWindowToRegister)
        self.btn_records_session.clicked.connect(self.switchWindowToRecordsSession)
        self.btn_records_patient.clicked.connect(self.switchWindowToRecordsPatient)

    # change window
    def switchWindowToRegister(self):
        newWindow = registerWindow(self.widgetManager, self.changeWindow)
        self.changeWindow(self.widgetManager, newWindow)
        
    def switchWindowToRecordsSession(self):
        newWindow = registerWindow(self.widgetManager, self.changeWindow)
        self.changeWindow(self.widgetManager, newWindow)
        
    def switchWindowToRecordsPatient(self):
        newWindow = registerWindow(self.widgetManager, self.changeWindow)
        self.changeWindow(self.widgetManager, newWindow)