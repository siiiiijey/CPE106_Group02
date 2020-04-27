from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys

conn = sqlite3.connect('atm.db')

c = conn.cursor()

class Ui_OtherWindow(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)

    def convert(self, ans):
        bad_chars = [';', ':', '!', "*",'?','.',',']
        test_string = ans
        test_string = filter(lambda i: i not in bad_chars, test_string)  
        return ''.join(test_string).split()
    
    def checkAns(self, converted):
        if converted[0] == "withdraw":
            self.listView.addItem("ATM: Withdrawing " + str(converted[1]) + "...")
            newBalance = self.balance - int(converted[1])
            self.balance = newBalance
            c.execute("UPDATE atm SET balance=? WHERE name ==?",(newBalance, self.name,)) 
            conn.commit()
            self.listView.addItem("ATM: Success! New balance is " + str(newBalance))
        if converted[0] == "deposit":
            self.listView.addItem("ATM: Depositing " + str(converted[1]) + "...")
            newBalance = self.balance + int(converted[1])
            self.balance = newBalance
            c.execute("UPDATE atm SET balance=? WHERE name ==?",(newBalance, self.name,)) 
            conn.commit()
            self.listView.addItem("ATM: Success! New balance is " + str(newBalance))
        if converted[0] == "check" or converted[0] == "balance":
            self.listView.addItem("ATM: Current balance is " + str(self.balance))

    @QtCore.pyqtSlot()
    def setupUi(self, MainWindow):
        
        @QtCore.pyqtSlot()
        def sendAnsToList():
            ans = self.lineEdit.text()
            self.listView.addItem(self.name + ": " + str(ans))
            self.lineEdit.clear()
            converted = self.convert(ans.lower())
            self.checkAns(converted)

        def closeWindow():
            sys.exit()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 131))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("ATMchat.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 180, 361, 201))
        self.listView.setObjectName("listView")
        self.listView.addItem("ATM: Hi! What would you like to do?")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 390, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 390, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(sendAnsToList)
        self.pushButton.clicked.connect(closeWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATMchat"))
        self.pushButton.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter"))