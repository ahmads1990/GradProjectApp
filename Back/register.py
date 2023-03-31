from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sqlite3
import sys


class Register(QDockWidget):
    def __init__(self,):
        super(Register, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/Register.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/Main1.jpg);") 
        # Assign functions
        self.pushbtnRegister.clicked.connect(self.clicker)
        
    # change windo   
    def clicker(self):
        widget.setCurrentWidget(MainWindow)
        

class Main(QDockWidget):
    def __init__(self,):
        super(Main, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/MainPage.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/Main2.jpg);") 
        
        self.pushbtnShowAllData.clicked.connect(self.clicker)
    # change windo   
    def clicker(self):
        widget.setCurrentWidget(AllDataWindow)

class AllData(QDockWidget):
    def __init__(self,):
        super(AllData, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/AllData.ui", self)
        
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Status"])
        c = con.cursor()
        c.execute("SELECT * FROM patient;")
        for i,row  in enumerate(c):
            rows = self.table.rowCount()
            self.table.setRowCount(rows + 1)
            self.table.setItem(i, 0,  QTableWidgetItem(str(row[0])))
            self.table.setItem(i, 1,  QTableWidgetItem(str(row[1])))
            self.table.setItem(i, 2,  QTableWidgetItem(str(row[2])))
            self.table.setItem(i, 3,  QTableWidgetItem(str(row[3])))
        #self.table.resizeColumnsToContents()
        
        self.pushbtnGoMain.clicked.connect(self.clicker)
    # change windo   
    def clicker(self):
        widget.setCurrentWidget(MainWindow)


# init the app
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

con = sqlite3.connect('PatientDatabase') 

# first page register
RegisterWindow = Register()
widget.addWidget(RegisterWindow)

# second page main window
MainWindow = Main()
widget.addWidget(MainWindow)

# third page
AllDataWindow = AllData()
widget.addWidget(AllDataWindow)

# set first page to register
widget.setCurrentWidget(RegisterWindow)
# show the app
widget.show()
sys.exit(app.exec_())