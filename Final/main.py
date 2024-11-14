import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot
import serial
from ui_Proyecto_final import Ui_MainWindow

class FuncionesWindow(QWidget):
    def __init__(self, arduino):
        super().__init__()
        self.setWindowTitle("Funciones")
        self.setGeometry(0, 0, 1920, 1080)
        layout = QVBoxLayout()
        self.setLayout(layout)
        button_layout = QHBoxLayout()
        self.arduino = arduino
        
        self.pushButton_4 = QPushButton("Botón 4")
        self.pushButton_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_4.setFixedHeight(100)
        
        self.pushButton_5 = QPushButton("Botón 5")
        self.pushButton_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_5.setFixedHeight(100)
        
        button_layout.addWidget(self.pushButton_4)
        button_layout.addWidget(self.pushButton_5)
        layout.addLayout(button_layout)

        self.pushButton_4.clicked.connect(self.enviar_senal_a)
        self.pushButton_5.clicked.connect(self.enviar_senal_b)
        
    def enviar_senal_a(self):
        self.arduino.write('A')
        
        print("No se pudo enviar la señal: Puerto cerrado.")
    def enviar_senal_b(self):
        self.arduino.write('B')
        print("No se pudo enviar la señal: Puerto cerrado.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(0,0,1920,1080)
        
        layout_botones = QHBoxLayout()
        
        self.ui.pushButton_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.ui.pushButton_2.setFixedHeight(100)
        self.ui.pushButton_3.setFixedHeight(100)
        
        layout_botones.addWidget(self.ui.pushButton_2)
        layout_botones.addWidget(self.ui.pushButton_3)
        
        central_widget = QWidget()
        central_widget.setLayout(layout_botones)
        self.setCentralWidget(central_widget)
        
        self.ui.pushButton_3.clicked.connect(self.inicio)
        try:
            self.arduino = serial.Serial('COM3', 9600)  # Cambia 'COM3' por tu puerto correcto
            print("Conexión establecida con el Arduino.")
        except serial.SerialException as e:
            print(f"No se pudo conectar al Arduino: {e}")
            self.arduino = None
        
        self.funciones_window = FuncionesWindow(self.arduino)

    @Slot()
    def inicio(self):
        self.funciones_window.show()
        self.hide()
    
    def informacion(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())