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

    # change window
    def switchWindow(self):
        newWindow = registerWindow(self.widgetManager, self.changeWindow)
        self.changeWindow(self.widgetManager, newWindow)