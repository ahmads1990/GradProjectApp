import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from Pages import mainWindow

def changeWindow(widgetManager, newWindow):
    print(widgetManager.count())
    widgetManager.addWidget(newWindow)
    print(widgetManager.count())
    widgetManager.setCurrentWidget(newWindow)
    print("Debug: added Window")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widgetManager = QtWidgets.QStackedWidget()

    startWindow = mainWindow(widgetManager, changeWindow)

    changeWindow(widgetManager,startWindow)
    
    widgetManager.show()
    sys.exit(app.exec_())