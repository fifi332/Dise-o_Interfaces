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

        self.etiqueta = QLabel("")
        self.etiqueta.setMaximumSize(600, 200)

        self.nums = []
        self.operador = []

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

        if len(self.operador) == len(self.nums):
            self.nums.append(num)
        elif len(self.operador) == len(self.nums)-1:

            self.nums[len(self.nums)-1] = self.nums[len(self.nums)-1] + num

        print("Numeros: ", self.nums)
        print("Operadores: ", self.operador)
        print()

        self.etiqueta.setText(self.etiqueta.text() + boton.text())

    def operadorPulsado(self):
        boton = self.sender()
        operador = boton.text()

        self.operador.append(operador)

        print("Numeros :", self.nums)
        print("Operadores :", self.operador)
        print()

        self.etiqueta.setText(self.etiqueta.text() + boton.text())



    def igualPulsado(self):

        por = self.operador.count("×")
        div =self.operador.count("÷")
        mas = self.operador.count("+")
        men = self.operador.count("-")

        while por > 0:
            posicion = self.operador.index("×")

            self.nums[posicion] = str(
                float(self.nums[posicion]) * float(self.nums[posicion + 1])
            )

            self.nums.pop(posicion + 1)
            self.operador.pop(posicion)

            por -= 1

            print("Numeros :", self.nums)
            print("Operadores:", self.operador)

        while div > 0:
            posicion = self.operador.index("÷")

            self.nums[posicion] = str(
                float(self.nums[posicion]) / float(self.nums[posicion + 1])
            )

            self.nums.pop(posicion + 1)
            self.operador.pop(posicion)

            div -= 1

            print("Numeros :", self.nums)
            print("Operadores:", self.operador)

        while mas > 0:
            posicion = self.operador.index("+")

            self.nums[posicion] = str(
                float(self.nums[posicion]) + float(self.nums[posicion + 1])
            )

            self.nums.pop(posicion + 1)
            self.operador.pop(posicion)

            mas -= 1

            print("Numeros :", self.nums)
            print("Operadores:", self.operador)

        while men > 0:
            posicion = self.operador.index("-")

            self.nums[posicion] = str(
                float(self.nums[posicion]) - float(self.nums[posicion + 1])
            )

            self.nums.pop(posicion + 1)
            self.operador.pop(posicion)

            men -= 1

            print("Numeros :", self.nums)
            print("Operadores:", self.operador)


        self.etiqueta.setText(self.nums[0])


    def ac(self):
        self.etiqueta.setText("")
        self.operador = []
        self.nums = []

    def mathPi(self):

        self.nums.append(str(math.pi))
        self.etiqueta.setText(self.etiqueta.text() + str(math.pi))





if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()