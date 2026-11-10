import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout,
    QLabel, QLineEdit, QPushButton, QComboBox,
    QCheckBox, QRadioButton, QGroupBox, QMessageBox,QSizePolicy
)
class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(400, 600)  # Ancho, Alto

        # 1. Layout Principal donde irá todo
        layout_principal = QVBoxLayout()

        # 2. Widget Contenedor Central (OBLIGATORIO en QMainWindow)
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # SECCIÓN 1
        self.sec_superior = QLineEdit("0")
            # 1. Fijar la altura de la caja de texto
        self.sec_superior.setFixedHeight(150)  # Alto en píxeles

            # 2. Alinear el texto a la derecha (como una calculadora real)
        self.sec_superior.setAlignment(Qt.AlignmentFlag.AlignRight)

            # 3. Hacer los números más grandes (Fuente)
        fuente = self.sec_superior.font()
        fuente.setPointSize(28)  # Tamaño de la letra
        self.sec_superior.setFont(fuente)

        layout_principal.addWidget(self.sec_superior,1)

        # SECCIÓN 2
        grid_central = QGridLayout()
        grid_central.addWidget(QPushButton("MC"), 0, 0)
        grid_central.addWidget(QPushButton("MR"), 0, 1)
        grid_central.addWidget(QPushButton("M+"), 0, 2)
        grid_central.addWidget(QPushButton("M-"), 0, 3)
        grid_central.addWidget(QPushButton("Ms"), 0, 4)
        grid_central.addWidget(QPushButton("M"), 0, 5)
        layout_principal.addLayout(grid_central, 2)

        # SECCIÓN 3
        grid_bottom = QGridLayout()
        # Fila1
        grid_bottom.addWidget(QPushButton("%"), 0, 0)
        grid_bottom.addWidget(QPushButton("CE"), 0, 1)
        grid_bottom.addWidget(QPushButton("C"), 0, 2)
        grid_bottom.addWidget(QPushButton("⌫"), 0, 3)

        # Fila2
        grid_bottom.addWidget(QPushButton("1/x"), 1, 0)
        grid_bottom.addWidget(QPushButton("x²"), 1, 1)
        grid_bottom.addWidget(QPushButton("²√x"), 1, 2)
        grid_bottom.addWidget(QPushButton("÷"), 1, 3)

        # Fila3
        btn_7 = QPushButton("7")
        btn_7.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_7, 2, 0)
        btn_8 = QPushButton("8")
        btn_8.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_8, 2, 1)
        btn_9 = QPushButton("9")
        btn_9.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_9, 2, 2)
        grid_bottom.addWidget(QPushButton("x"), 2, 3)

        # Fila4
        btn_4 = QPushButton("4")
        btn_4.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_4, 3, 0)
        btn_5 = QPushButton("5")
        btn_5.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_5, 3, 1)
        btn_6 = QPushButton("6")
        btn_6.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_6, 3, 2)
        grid_bottom.addWidget(QPushButton("-"), 3, 3)

        #Fila5
        btn_1 = QPushButton("1")
        btn_1.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_1, 4, 0)
        btn_2 = QPushButton("2")
        btn_2.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_2, 4, 1)
        btn_3 = QPushButton("3")
        btn_3.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_3, 4, 2)
        grid_bottom.addWidget(QPushButton("+"), 4, 3)

        #Fila6
        btn_mm = QPushButton("+ / -")
        btn_mm.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_mm, 5, 0)
        btn_0 = QPushButton("0")
        btn_0.setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_0, 5, 1)
        btn_punto = QPushButton(".")
        btn_punto .setStyleSheet("background-color: grey; color: white;")
        grid_bottom.addWidget(btn_punto , 5, 2)
        btn_igual = QPushButton("=")
        btn_igual.setStyleSheet("background-color: lightblue; color: black;")
        grid_bottom.addWidget( btn_igual, 5, 3)

        for i in range(grid_bottom.count()):
            grid_bottom.itemAt(i).widget().setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
            )
            grid_bottom.itemAt(i).widget().clicked.connect(self.al_pulsar_boton)

        layout_principal.addLayout(grid_bottom, 3)
    #Sepuede hacer mediante una mantriz de botones y un bucle
        # Matriz de botones (Fila por fila)
        # botones = [
        #    ["%", "CE", "C", "⌫"],  # Fila 0
        #    ["1/x", "x²", "²√x", "÷"],  # Fila 1
        #   ["7", "8", "9", "x"],  # Fila 2
        #    ["4", "5", "6", "-"],  # Fila 3
        #    ["1", "2", "3", "+"],  # Fila 4
        #    ["+ / -", "0", ".", "="]  # Fila 5 (Corregido índice a 5)
        #]

        # Añadir botones a la rejilla
        #for fila, lista_filas in enumerate(botones):
        #    for col, texto in enumerate(lista_filas):
        #       btn = QPushButton(texto)
                #  Hacer que el botón se expanda en vertical y horizontal
        #       btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #       btn.clicked.connect(self.al_pulsar_boton)
        #       grid_bottom.addWidget(btn, fila, col)

    def al_pulsar_boton(self):
        boton = self.sender()  # Detecta qué botón disparó el evento
        texto_pulsado = boton.text()
        texto_actual = self.sec_superior.text()  # Selecciona el texto escrito

        # 1. Limpiar pantalla (C o CE)
        if texto_pulsado in ("C", "CE"):
            self.sec_superior.setText("0")

        # 2. Borrar último carácter (⌫)
        elif texto_pulsado == "⌫":
            if len(texto_actual) > 1 and texto_actual != "Error":
                self.sec_superior.setText(texto_actual[:-1])
            else:
                self.sec_superior.setText("0")

        # 3. Calcular la operación completa (=)
        elif texto_pulsado == "=":
            try:
                # Reemplazamos los símbolos visuales por los que entiende Python
                expresion = texto_actual.replace("x", "*").replace("÷", "/")
                resultado = eval(expresion)
                self.sec_superior.setText(str(resultado))
            except Exception:
                self.sec_superior.setText("Error")

        # 4. Escribir números y operadores
        else:
            # Si hay un '0' o 'Error', lo sobrescribe con el nuevo número
            if texto_actual in ("0", "Error"):
                self.sec_superior.setText(texto_pulsado)
            else:
                self.sec_superior.setText(texto_actual + texto_pulsado)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec())