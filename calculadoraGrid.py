import math
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QColor, QPalette

class CaixaCor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid")

        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 400)

        maia = QGridLayout()

        self.etiqueta = QLabel("0")
        self.etiqueta.setMaximumSize(600, 200)

        self.num1 = "0"
        self.operador = ""
        self.num2 = ""

        botonDelet = QPushButton("⌫")
        botonParentesis1 = QPushButton("(")
        botonParentesis2 = QPushButton(")")
        botonAC = QPushButton("AC")
        botonPi = QPushButton("π")

        boton7 = QPushButton("7")
        boton8 = QPushButton("8")
        boton9 = QPushButton("9")
        botonDiv = QPushButton("÷")
        botonRaiz = QPushButton("√")

        boton4 = QPushButton("4")
        boton5 = QPushButton("5")
        boton6 = QPushButton("6")
        botonPor = QPushButton("×")
        botonElevado = QPushButton("x²")

        boton1 = QPushButton("1")
        boton2 = QPushButton("2")
        boton3 = QPushButton("3")
        botonMenos = QPushButton("-")
        botonIgual = QPushButton("=")
        botonIgual.setFixedSize(70, 60)
        botonIgual.setStyleSheet("background-color: #FF7700;")


        boton0 = QPushButton("0")
        botonPunto = QPushButton(".")
        botonPorciento = QPushButton("%")
        botonMas = QPushButton("+")

        maia.addWidget(self.etiqueta,1,0,1,4)

        maia.addWidget(botonDelet, 2, 0)
        maia.addWidget(botonParentesis1, 2, 1)
        maia.addWidget(botonParentesis2, 2, 2)
        maia.addWidget(botonAC, 2, 3)
        maia.addWidget(botonPi, 2, 4)

        maia.addWidget(boton7, 3, 0)
        maia.addWidget(boton8, 3, 1)
        maia.addWidget(boton9, 3, 2)
        maia.addWidget(botonDiv, 3, 3)
        maia.addWidget(botonRaiz, 3, 4)

        maia.addWidget(boton4, 4, 0)
        maia.addWidget(boton5, 4, 1)
        maia.addWidget(boton6, 4, 2)
        maia.addWidget(botonPor, 4,3)
        maia.addWidget(botonElevado, 4, 4)

        maia.addWidget(boton1, 5, 0)
        maia.addWidget(boton2, 5, 1)
        maia.addWidget(boton3, 5, 2)
        maia.addWidget(botonMenos, 5, 3)
        maia.addWidget(botonIgual, 5, 4, 2, 1)

        maia.addWidget(boton0, 6, 0)
        maia.addWidget(botonPunto, 6, 1)
        maia.addWidget(botonPorciento, 6, 2)
        maia.addWidget(botonMas, 6, 3)

        boton0.clicked.connect(self.numeroPulsado)
        boton1.clicked.connect(self.numeroPulsado)
        boton2.clicked.connect(self.numeroPulsado)
        boton3.clicked.connect(self.numeroPulsado)
        boton4.clicked.connect(self.numeroPulsado)
        boton5.clicked.connect(self.numeroPulsado)
        boton6.clicked.connect(self.numeroPulsado)
        boton7.clicked.connect(self.numeroPulsado)
        boton8.clicked.connect(self.numeroPulsado)
        boton9.clicked.connect(self.numeroPulsado)

        botonPi.clicked.connect(self.mathPi)

        botonMas.clicked.connect(self.operadorPulsado)
        botonMenos.clicked.connect(self.operadorPulsado)
        botonPor.clicked.connect(self.operadorPulsado)
        botonDiv.clicked.connect(self.operadorPulsado)

        botonIgual.clicked.connect(self.igualPulsado)
        botonAC.clicked.connect(self.ac)



        contenedor = QWidget()
        contenedor.setLayout(maia)

        contenedor.setStyleSheet("""
            QPushButton {
                background-color: #eeeeee;
                border-radius: 10px;
                border: 2px solid black;
            }
            QPushButton:pressed {
                background-color: #cccccc;
    }
        """)

        self.setCentralWidget(contenedor)

        self.show()

    def numeroPulsado(self):
        boton = self.sender()
        num = boton.text()

        if self.operador == "":
            if self.num1 == "0":
                self.num1 = num
            else:
                self.num1 = self.num1 + num

            self.etiqueta.setText(self.num1)

        else:
            self.num2 = self.num2 + num
            self.etiqueta.setText(self.num2)

        print("Numero 1:", self.num1)
        print("Operador:", self.operador)
        print("Numero 2:", self.num2)
        print()

    def operadorPulsado(self):
        boton = self.sender()
        operador = boton.text()

        self.operador = operador

        print("Numero 1:", self.num1)
        print("Operador:", self.operador)
        print("Numero 2:", self.num2)
        print()

    def igualPulsado(self):
        if self.operador == "+":
            self.num1 = str(float(self.num1) + float(self.num2))
            self.etiqueta.setText(self.num1)
        elif self.operador == "-":
            self.num1 = str(float(self.num1) - float(self.num2))
            self.etiqueta.setText(self.num1)
        elif self.operador == "×":
            self.num1 = str(float(self.num1) * float(self.num2))
            self.etiqueta.setText(self.num1)
        elif self.operador == "÷":
            self.num1 = str(float(self.num1) / float(self.num2))
            self.etiqueta.setText(self.num1)
        self.num2 = ""
        self.operador = ""

    def ac(self):
        self.etiqueta.setText("0")
        self.operador = ""
        self.num1 = "0"
        self.num2 = ""

    def mathPi(self):
        if self.operador == "":
            self.num1 = str(float(math.pi))
            self.etiqueta.setText(self.num1)
        else:
            self.num2 = str(float(math.pi))
            self.etiqueta.setText(self.num2)





if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()