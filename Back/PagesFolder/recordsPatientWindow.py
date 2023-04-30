from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from Database.database import all_data_patients

class recordsPatientsWindow(QDockWidget):
    def __init__(self, widgetManager, changeWindow):
        super(recordsPatientsWindow, self).__init__()
        self.widgetManager = widgetManager
        self.changeWindow = changeWindow          
           
        # load the ui file 
        uic.loadUi("../Front/recordsPatient.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/ShowRecordsPatient.png);") 
        self.tableWidget.setColumnWidth(0,51)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,140)
        self.tableWidget.setColumnWidth(4,240)

        self.load_data()

    def load_data(self):
        data = all_data_patients()
        print(data)
        row = 0
        self.tableWidget.setRowCount(len(data))
        for patient in data:
            id = f'{patient[0]}'
            self.tableWidget.setItem(row , 0 , QTableWidgetItem(id))
            self.tableWidget.setItem(row , 1 , QTableWidgetItem(patient[1]))
            self.tableWidget.setItem(row , 2 , QTableWidgetItem(patient[2]))
            self.tableWidget.setItem(row , 3 , QTableWidgetItem(patient[3]))
            self.tableWidget.setItem(row , 4 , QTableWidgetItem(patient[4]))
            row=row+1




        # Assign functions
        #self.StartSession.clicked.connect(self.clicker)
        
    # change window
    def clicker(self):
        #widget.setCurrentWidget(MainWindow)
        print("main")