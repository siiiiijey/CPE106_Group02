from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import doctorUI

conn = sqlite3.connect('doctor.db')

c = conn.cursor()

class Ui_MainWindow(object):

    def openWindow(self, first, last, hist):
        self.window = QtWidgets.QMainWindow()
        self.ui = doctorUI.Ui_OtherWindow(first, last, hist)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):

        def getInfo():
            inputLN = self.lineEdit_2.text()
            c.execute("SELECT * FROM doctor WHERE lastName == ?",(inputLN,))
            data = c.fetchall()
            for entry in data:
                fn = entry[0]
                ln = entry[1]
                history = entry[2]
            self.openWindow(fn, ln, history)

        def register():
                inputFN = self.lineEdit.text()
                inputLN = self.lineEdit_2.text()
                c.execute("INSERT INTO doctor(firstName,lastName, history) VALUES (?,?,'None')",(inputFN, inputLN))
                conn.commit()
                self.lineEdit.clear()
                self.lineEdit_2.clear()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 201, 201))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 281, 111))
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setPixmap(QtGui.QPixmap("title.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 340, 311, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 310, 51, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 410, 311, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 380, 51, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(getInfo)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 470, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(register)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Doctor -  Home"))
        self.label_5.setText(_translate("MainWindow", "First Name"))
        self.label_6.setText(_translate("MainWindow", "Last Name"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

