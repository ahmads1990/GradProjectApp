import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from Pages import mainWindow
from Model import test_binary_model
import threading

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
    
    print("path: ")
    print(test_binary_model.path)
    # load model
    model = threading.Thread(
                target=test_binary_model.load_model,
                args=(
                    #test_binary_model.path
                ),
            ).start()
    
    sys.exit(app.exec_())