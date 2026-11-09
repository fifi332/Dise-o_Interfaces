#ollama run qwen2.5-coder:3b

import sys
from PyQt6.QtWidgets import (QApplication,QCheckBox,QComboBox,QFormLayout,QGridLayout,QLabel,QLineEdit,QMainWindow,QRadioButton,QStackedLayout,QTimeEdit,QVBoxLayout,QWidget,)


class FiestraPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QStackedLayout")

        # Layout principal vertical
        caixaV = QVBoxLayout()

        # ComboBox con texto explicativo inicial
        cmbTipo = QComboBox()
        cmbTipo.setPlaceholderText("Selecciona una opción...")
        cmbTipo.addItems(["Profesor", "Alumno", "PAS"])
        caixaV.addWidget(cmbTipo)

        # QStackedLayout para las tarjetas
        tarxetas = QStackedLayout()

        # --- 0. PANEL VACÍO (Para el inicio) ---
        panelVacio = QWidget()

        # --- 1. PANEL PROFESOR (Índice 1 en tarxetas) ---
        panelProfesor = QWidget()
        layoutProfesor = QVBoxLayout()

        # Selección de Curro (Tutor / No tutor)
        lblCurro = QLabel("Curro:")
        rbtTutor = QRadioButton("Tutor")
        rbtNoTutor = QRadioButton("No tutor")

        layoutProfesor.addWidget(lblCurro)
        layoutProfesor.addWidget(rbtTutor)
        layoutProfesor.addWidget(rbtNoTutor)

        # Selección de Nivel
        lblNivel = QLabel("Nivel:")
        chkBasico = QCheckBox("Básico")
        chkMedio = QCheckBox("Medio")
        chkSuperior = QCheckBox("Superior")

        layoutProfesor.addWidget(lblNivel)
        layoutProfesor.addWidget(chkBasico)
        layoutProfesor.addWidget(chkMedio)
        layoutProfesor.addWidget(chkSuperior)

        panelProfesor.setLayout(layoutProfesor)

        # --- 2. PANEL ALUMNO (Índice 2 en tarxetas) ---
        panelAlumno = QWidget()
        maiaAlumno = QGridLayout()

        lblCiclo = QLabel("Ciclo")
        cmbCiclo = QComboBox()
        ciclos = ("DAM", "ASIR", "SMR", "IEA", "ADF")
        cmbCiclo.addItems(ciclos)
        cmbCiclo.setCurrentIndex(-1)

        rbtPrimeiro = QRadioButton("Primeiro")
        rbtSegundo = QRadioButton("Segundo")

        cmbAnoMatricula = QComboBox()
        cursosMatricula = ("25/26", "26/27")
        cmbAnoMatricula.addItems(cursosMatricula)

        lblNomeNai = QLabel("Nome Nai")
        txtNomeNai = QLineEdit()
        lblNomePai = QLabel("Nome Pai")
        txtNomePai = QLineEdit()

        maiaAlumno.addWidget(lblCiclo, 0, 0)
        maiaAlumno.addWidget(cmbCiclo, 0, 1)
        maiaAlumno.addWidget(rbtPrimeiro, 1, 0)
        maiaAlumno.addWidget(rbtSegundo, 1, 1)
        maiaAlumno.addWidget(cmbAnoMatricula, 2, 1)
        maiaAlumno.addWidget(lblNomeNai, 3, 0)
        maiaAlumno.addWidget(txtNomeNai, 3, 1)
        maiaAlumno.addWidget(lblNomePai, 4, 0)
        maiaAlumno.addWidget(txtNomePai, 4, 1)

        panelAlumno.setLayout(maiaAlumno)

        # --- 3. PANEL PAS (Índice 3 en tarxetas) ---
        panelPAS = QWidget()
        layoutPAS = QFormLayout()
        txtOcupacion = QLineEdit()
        txtOcupacion.setPlaceholderText("Introduce la ocupación")
        hora = QTimeEdit()
        hora.setDisplayFormat("HH:mm")
        horaSalida = QTimeEdit()
        horaSalida.setDisplayFormat("HH:mm")
        layoutPAS.addRow("Ocupación:", txtOcupacion)
        layoutPAS.addRow("Hora:", hora)
        layoutPAS.addRow("Hora de salida:", horaSalida)
        panelPAS.setLayout(layoutPAS)

        # Añadimos los paneles en orden
        tarxetas.addWidget(panelVacio)  # Índice 0 (Inicio sin nada)
        tarxetas.addWidget(panelProfesor)  # Índice 1
        tarxetas.addWidget(panelAlumno)  # Índice 2
        tarxetas.addWidget(panelPAS)  # Índice 3

        # Función para cambiar de tarjeta según la opción seleccionada
        def cambiar_tarjeta(index):
            if index >= 0:
                tarxetas.setCurrentIndex(index + 1)
            else:
                tarxetas.setCurrentIndex(0)

        cmbTipo.currentIndexChanged.connect(cambiar_tarjeta)

        # Forzamos que al iniciar no haya ninguna opción seleccionada del combo
        cmbTipo.setCurrentIndex(-1)

        # Añadimos el QStackedLayout al layout principal
        caixaV.addLayout(tarxetas)

        # Configuramos el widget central
        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

        self.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    sys.exit(app.exec())