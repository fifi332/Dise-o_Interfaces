import math
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QGridLayout, QComboBox, QStackedLayout, QRadioButton)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QstakedLayout")

        caixaV = QVBoxLayout()

        self.cmbTipo = QComboBox()
        self.cmbTipo.addItem("Alumno")
        self.cmbTipo.addItems(["Profesores", "Pas"])
        self.cmbTipo.setCurrentIndex(-1)
        self.cmbTipo.currentIndexChanged.connect(self.on_cmbTipo_currentIndexChanged)

        caixaV.addWidget(self.cmbTipo)

        self.tarxetas = QStackedLayout()

        maiaAlumno = QGridLayout()
        lblCiclo = QLabel("Ciclo")
        cmbCiclo = QComboBox()
        ciclos = ("DAM", "Asir", "SMR", "IEA", "ADF")
        cmbCiclo.addItems(ciclos)
        cmbCiclo.setCurrentIndex(-1)
        rbtPrimeiro = QRadioButton("Primeiro")
        rbtSegundo = QRadioButton("Segundo",rbtPrimeiro)
        cmbAnoMatricula = QComboBox()
        cursosMatricula = ("25/26","26/27","27/28")
        lblNomeNai = QLabel("Nome Nai")
        txtNomeNai = QLineEdit()
        lblNomePai = QLabel("Nome Pai")
        txtNomePai = QLineEdit()

        maiaAlumno.addWidget(lblCiclo, 0, 0)
        maiaAlumno.addWidget(cmbCiclo, 0, 1)

        layoutRadio = QHBoxLayout()
        layoutRadio.addWidget(rbtPrimeiro)
        layoutRadio.addWidget(rbtSegundo)
        maiaAlumno.addLayout(layoutRadio, 1, 0, 1, 2)
        maiaAlumno.addWidget(cmbAnoMatricula, 2, 0, 1, 2)
        maiaAlumno.addWidget(lblNomeNai, 3, 0)
        maiaAlumno.addWidget(txtNomeNai, 3, 1)
        maiaAlumno.addWidget(lblNomePai, 3, 0, 1, 1)
        maiaAlumno.addWidget(txtNomePai, 3, 1, 1, 3)

        widgetAlumno = QWidget()
        widgetAlumno.setLayout(maiaAlumno)
        self.tarxetas.addWidget(widgetAlumno)

        caixaV.addLayout(self.tarxetas)

        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

    def on_cmbTipo_currentIndexChanged(self, index):
        self.tarxetas.setCurrentIndex(index)

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        fiestra = FiestraPrincipal()
        fiestra.show()
        sys.exit(app.exec())