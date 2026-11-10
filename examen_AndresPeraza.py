import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QLineEdit, QCheckBox,
    QPushButton, QComboBox, QStackedWidget, QDial,
    QGroupBox, QRadioButton, QTextEdit
)


class ExamenVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-11-2026 grupo A")
        self.resize(600, 500)
        self.initUI()

    def initUI(self):
        # 1. Widget central para QMainWindow (Soluciona el error de setLayout)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layaut_principal = QVBoxLayout(central_widget)

        # 2. Selector de pestañas con opciones separadas
        self.selector = QComboBox()
        self.selector.addItems(["Configuración Zoa 1", "Zoa 2", "Consola"])
        layaut_principal.addWidget(self.selector)

        # 3. StackedWidget para alternar entre las zonas
        self.stacked_widget = QStackedWidget()
        layaut_principal.addWidget(self.stacked_widget)

        # --- ZOA 1 ---
        self.zoa1 = QWidget()
        l_zoa1 = QVBoxLayout(self.zoa1)

        # Checkbox activada
        chk_activada = QCheckBox("Zoa activada")
        chk_activada.setChecked(True)
        l_zoa1.addWidget(chk_activada)

        # Hora
        l_hora = QHBoxLayout()
        l_hora.addWidget(QLabel("Hora de comezo de rego:"))
        self.txt_Hora = QLineEdit()
        self.txt_Hora.setPlaceholderText("hh:mm")
        l_hora.addWidget(self.txt_Hora)
        l_zoa1.addLayout(l_hora)

        # Dial / Duración
        l_dial = QHBoxLayout()
        self.lbl_duracion = QLabel("Duracion de rego: 0 min")
        self.dial = QDial()
        self.dial.setRange(0, 400)
        self.dial.setValue(0)
        l_dial.addWidget(self.lbl_duracion)
        l_dial.addWidget(self.dial)
        l_zoa1.addLayout(l_dial)

        g_opc = QGroupBox("Opcións")
        l_opc = QVBoxLayout(g_opc)
        self.rb_diario = QRadioButton("Diario")
        self.rb_semanal = QRadioButton("Semanal")
        self.rb_antixiada = QRadioButton("Antixia")
        self.rb_chuvia = QRadioButton("Chuvia")
        l_opc.addWidget(self.rb_diario)
        l_opc.addWidget(self.rb_semanal)
        l_opc.addWidget(self.rb_antixiada)
        l_opc.addWidget(self.rb_chuvia)
        l_zoa1.addWidget(g_opc)

        g_dias = QGroupBox("Días")
        l_dias = QHBoxLayout(g_dias)
        self.dias_checks = []
        for d in ["Luns", "Martes", "Mércores", "Xoves", "Venres", "Sábado", "Domingo"]:
            chk = QCheckBox(d)
            self.dias_checks.append(chk)
            l_dias.addWidget(chk)

        # Se añade el GroupBox fuera del bucle for
        l_zoa1.addWidget(g_dias)

        # Botón Aceptar
        self.btn_aceptar = QPushButton("Aceptar")
        l_zoa1.addWidget(self.btn_aceptar)

        # --- ZOA 2 ---
        self.zoa2 = QWidget()
        l_zoa2 = QVBoxLayout(self.zoa2)
        l_zoa2.addWidget(QLabel("Zoa 2"))

        # --- CONSOLA (ZOA 3) ---
        self.zoa3 = QWidget()
        l_zoa3 = QVBoxLayout(self.zoa3)
        self.txt_consola = QTextEdit()
        self.txt_consola.setReadOnly(True)
        l_zoa3.addWidget(self.txt_consola)

        # Añadir las vistas al StackedWidget
        self.stacked_widget.addWidget(self.zoa1)
        self.stacked_widget.addWidget(self.zoa2)
        self.stacked_widget.addWidget(self.zoa3)

        # Conectar el selector con el cambio de vista
        self.selector.currentIndexChanged.connect(self.stacked_widget.setCurrentIndex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ExamenVentana()
    ventana.show()
    sys.exit(app.exec())