import sys
import time
import pyaudio
import wave
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from AudioRecorder import Recorder 
from Pages.mainWindow import mainWindow
from Pages.registerWindow import registerWindow
from Pages.recordsPatientWindow import recordsPatientsWindow
from Pages.recordsSessionWindow import recordsSessionWindow
from Pages.startSessionWindow import startSessionWindow
class AudioRecorderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.recorder = Recorder()
        self.initUI()
        
        
        
    def initUI(self):
        self.start_button = QPushButton('Start Recording', self)
        self.start_button.clicked.connect(self.click)

        self.stop_button = QPushButton('Stop Recording', self)
        self.stop_button.clicked.connect(self.recorder.stop_recording)

        vbox = QVBoxLayout()
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)

        self.setLayout(vbox)
        self.setWindowTitle('Audio Recorder')
        self.show()

    def click(self):
        
        threading.Thread(target=self.recorder.start_recording, args=('Letters')).start()
            
    
        

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #recorderi = AudioRecorderWindow()
    #x = mainWindow()
    #x = registerWindow()
    #x = recordsSessionWindow()
    #x = recordsSessionWindow()
    x = startSessionWindow()
    
    x.show()
    sys.exit(app.exec_())