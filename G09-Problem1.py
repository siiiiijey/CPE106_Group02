import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def window():
           
        app = QApplication(sys.argv)
        win = QWidget()
        grid = QGridLayout()
        
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
   
        l2 = QLabel()
        l2.setText("Fahrenheit")
   
        l3 = QLabel()
        l3.setText("Celsius")

        l2.setFont(font)
        l3.setFont(font)
   
        fahrenheit = 32.00
        celsius = 0.0
   
        le1 = QLineEdit()
        le1.setValidator(QDoubleValidator(0.99,99.99,2))
        le1.setText(str(fahrenheit))
        le2 = QLineEdit()
        le2.setValidator(QDoubleValidator(0.99,99.99,2))
        le2.setText(str(celsius))
   
        b1 = QPushButton(">>>>")
        b2 = QPushButton("<<<<")
        
        def fahToCel(self):
            inputvar = le1.text()
            fahrenheit = float(inputvar)
            newCelsius = (5/9)*(32-fahrenheit)
            le2.setText(str(newCelsius))
            return self
   
        def celToFah(self):
            inputvar1 = le2.text()
            celsius = float(inputvar1)
            newFahrenheit = (celsius*(9/5))+32
            le1.setText(str(newFahrenheit))
            return self
        
        b1.clicked.connect(fahToCel)
        b2.clicked.connect(celToFah)
        
        grid.addWidget(l2,1,1)
        grid.addWidget(l3,1,2)
        grid.addWidget(le1,2,1)
        grid.addWidget(le2,2,2)
        grid.addWidget(b1,3,1)
        grid.addWidget(b2,3,2)
   	
        win.setLayout(grid)
        win.setGeometry(300,100,300,100)
        win.setWindowTitle("Temperature Converter")
        win.show()
        sys.exit(app.exec_())
   
if __name__ == '__main__':
   window()