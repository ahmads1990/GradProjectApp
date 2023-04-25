from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem

class registerWindow(QDockWidget):
    def __init__(self, widgetManager, changeWindow):
        super(registerWindow, self).__init__()
        self.widgetManager = widgetManager
        self.changeWindow = changeWindow

        # load the ui file 
        uic.loadUi("../Front/register.ui", self)
        
        # set background image
        self.background.setStyleSheet(f"background-image: url(../Front/Images/Register.png);") 

        # Assign functions
        self.btn_Cancel.clicked.connect(self.cancelSession)
        self.btn_Clear.clicked.connect(self.clearSesssion)
        self.btn_StartRecord.clicked.connect(self.startRecordSession)
        
    # change window   
    def cancelSession(self):
        # go back
        self.widgetManager.removeWidget(self)
        self.widgetManager.currentWidget(self.widgetManager.widget(self.widgetManager.count()-1))

        print("go back")
    
    #isChecked

    def clearSesssion(self):
        self.txtEdit_Name.clear()
        self.txtEdit_Email.clear()
        self.txtEdit_Phone.clear()
        self.txtEdit_Age.clear()

        self.radbtn_male.setChecked(False)
        self.radbtn_female.setChecked(False)
        print("clear")

    def startRecordSession(self):

        # check all fields
        name = self.txtEdit_Name.toPlainText()
        email = self.txtEdit_Email.toPlainText()
        phone = self.txtEdit_Phone.toPlainText()
        age = self.txtEdit_Age.toPlainText()

        # Todo: add more validation
        if(self.radbtn_male.isChecked() and self.radbtn_female.isChecked() ):
            return
        
        gender = self.radbtn_male.isChecked() or self.radbtn_female.isChecked()

        # database

        # all good then start recording
        self.changeWindow()
        print("start recording")