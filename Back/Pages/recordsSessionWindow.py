from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from Database.database import all_data_sessions

class recordsSessionWindow(QDockWidget):
    def __init__(self,):
        super(recordsSessionWindow, self).__init__()
        
        # load the ui file 
        uic.loadUi("../Front/recordsSession.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/ShowRecordsSession.png);")
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(3, 90)
        # self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 300)
        # self.tableWidget.setColumnWidth(3, 140)
        # self.tableWidget.setColumnWidth(4, 240)

        self.load_data()

    def load_data(self):
        data = all_data_sessions()
        print(data)
        row = 0
        self.tableWidget.setRowCount(len(data))
        for session in data:
            id_patient = f'{session[0]}'
            id_session = f'{session[1]}'
            id_pathology = f'{session[3]}'

            self.tableWidget.setItem(row, 0, QTableWidgetItem(id_patient))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(id_session))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(session[2]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(id_pathology))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(session[4]))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(session[4]))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(session[4]))
            row = row + 1

        # Assign functions
        #self.StartSession.clicked.connect(self.clicker)
        
    # change window   
    def clicker(self):
        #widget.setCurrentWidget(MainWindow)
        print("main")