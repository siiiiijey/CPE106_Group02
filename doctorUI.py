
from sys import argv
import pandas as pd
import random
import sqlite3
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSql

conn = sqlite3.connect('doctor.db')

c = conn.cursor()

class Ui_OtherWindow(object):

    def __init__(self, firstName, lastName, history):
        self.firstName = firstName
        self.lastName = lastName  
        self.history = history

    hedges = ("Please tell me more.",
            "Many of my patients tell me the same thing.",
            "Please continue.")

    qualifiers = ("Why do you say that ",
                "You seem to think that ",
                "Can you explain why ")

    replacements = {"I":"you", "me":"you", "my":"your",
                    "we":"you", "us":"you", "mine":"yours"} 

    def reply(self, sentence):
        """Implements two different reply strategies."""
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(self.hedges)
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.replacements.get(word, word))
        return " ".join(replyWords) 

    def chat(self,sentence):
        if sentence.upper() == "QUIT":
            self.listView.addItem("Doctor: Have a nice day!")
        response = self.reply(sentence)
        self.listView.addItem("Doctor: " + response)
        c.execute("UPDATE doctor SET history=? WHERE lastName ==?",(response, self.lastName,)) 
        conn.commit()
    @QtCore.pyqtSlot()
    def setupUi(self, MainWindow):
        
        @QtCore.pyqtSlot()
        def sendAnsToList():
            ans = self.lineEdit.text()
            self.listView.addItem("You: " + str(ans))
            self.lineEdit.clear()
            self.chat(ans)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 101, 101))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 311, 81))
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("title.png"))
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 190, 451, 271))
        self.listView.setObjectName("listView")
        self.listView.addItem("Doctor: Hi, " + self.firstName + "! Here are my responses from our last meeting:\n" + self.history + "\nDoctor: What can I do for you today?")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 470, 341, 41))
        self.lineEdit.setObjectName("lineEdit")            
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(374, 470, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Send")
        self.pushButton.clicked.connect(sendAnsToList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Doctor"))


