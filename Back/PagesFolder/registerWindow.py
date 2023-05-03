from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QLabel, QTextEdit, QPushButton,QTableWidgetItem
from PagesFolder.BaseWindow import BaseWindow
from Database.dtos import Patient
class registerWindow(QDockWidget):
    def __init__(self, windowManager, databaseHandler):
        super(registerWindow, self).__init__()
        self.windowManager = windowManager
        self.databaseHandler = databaseHandler
        
        # load the ui file
        uic.loadUi("../Front/register.ui", self)

        # set background image
        self.background.setStyleSheet(
            f"background-image: url(../Front/Images/Register.png);"
        )
        self.clearSesssion()
        # Assign functions
        self.btn_Cancel.clicked.connect(self.cancelSession)
        self.btn_Clear.clicked.connect(self.clearSesssion)
        self.btn_StartRecord.clicked.connect(self.startRecordSession)

    # change window go back to the main window
    def cancelSession(self):
        # go back
        self.windowManager.GoToMain()
        print("-- go back to main")
        
    # clear all the input fields
    def clearSesssion(self):
        self.txtEdit_Name.clear()
        self.txtEdit_Email.clear()
        self.txtEdit_Phone.clear()
        self.txtEdit_Age.clear()
        self.txtEdit_ID.clear()
        self.radbtn_male.setChecked(False)
        self.radbtn_female.setChecked(False)

    def startRecordSession(self):  
        # check all fields     
       
        patientID=0   
        name = self.txtEdit_Name.toPlainText()
        email = self.txtEdit_Email.toPlainText()
        phone = self.txtEdit_Phone.toPlainText()
        age = 0
        
        try: 
            age = self.txtEdit_Age.toPlainText()
        except:
            self.msg_Error.setText("Enter Age Correctly")
            
        try: 
            patientID = int(self.txtEdit_ID.toPlainText())
        except:
            self.msg_Error.setText("Enter ID Correctly")
            
        # Todo: add more validation
        if self.radbtn_male.isChecked() and self.radbtn_female.isChecked():
            return
        if not self.radbtn_male.isChecked() and not self.radbtn_female.isChecked():
            return
        
        gender = ""
        gender = "m" if self.radbtn_male.isChecked() else "f"
        
        if name=="" or email==""or phone==""or phone==""or age=="" or gender == "":
            print("Enter data Correctly")
            self.msg_Error.setText("Enter data Correctly")
            return
        
        # database
        newPatient = Patient(patientID,name,email,phone,age, gender)
        try:
            self.databaseHandler.insert_patient(newPatient)
        except:
            print("ID repeated")
            self.msg_Error.setText("ID repeated")
            return
        # all good then start recording
        self.windowManager.ReturnStartSession(patientID)
        self.windowManager.GoToStartSession()
        
        print("Start recording")
