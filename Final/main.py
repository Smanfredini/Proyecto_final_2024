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

"""import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, QTimer
import serial
from ui_Proyecto_final import Ui_MainWindow

class FuncionesWindow(QWidget):
    def __init__(self, arduino, main_window):
        super().__init__()
        self.setWindowTitle("Funciones")
        self.arduino = arduino
        self.main_window = main_window

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.setSpacing(10)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)
        
        self.pushButton_4 = QPushButton("Encender Sistema")
        self.pushButton_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_4.setFixedHeight(100)

        self.pushButton_5 = QPushButton("Apagar Sistema")
        self.pushButton_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_5.setFixedHeight(100)

        button_layout.addWidget(self.pushButton_4)
        button_layout.addWidget(self.pushButton_5)

        main_layout.addLayout(button_layout)

        self.boton_volver = QPushButton("Volver a Principal")
        self.boton_volver.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.boton_volver.setFixedHeight(100)

        main_layout.addWidget(self.boton_volver)

        self.setLayout(main_layout)

        self.pushButton_4.clicked.connect(self.enviar_senal_b)
        self.pushButton_5.clicked.connect(self.enviar_senal_a)
        self.boton_volver.clicked.connect(self.volver_a_principal)

    def enviar_senal_a(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'A')
            print("Señal 'A' enviada: Sistema apagado.")
        else:
            print("No se pudo enviar la señal: Puerto cerrado.")

    def enviar_senal_b(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'B')
            print("Señal 'B' enviada: Sistema encendido.")
        else:
            print("No se pudo enviar la señal: Puerto cerrado.")

    def volver_a_principal(self):
        self.hide()
        self.main_window.show()


class EstadisticasWindow(QWidget):
    def __init__(self, arduino, main_window):
        pass
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        layout_botones = QVBoxLayout()

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout_botones.addItem(spacer)

        self.ui.pushButton_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_2.setFixedHeight(100)
        self.ui.pushButton_3.setFixedHeight(100)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ui.pushButton_2)
        button_layout.addWidget(self.ui.pushButton_3)

        layout_botones.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout_botones)
        self.setCentralWidget(central_widget)

        self.ui.pushButton_3.clicked.connect(self.inicio)

        try:
            self.arduino = serial.Serial('COM7', 9600)
            print("Conexión establecida con el Arduino.")
        except serial.SerialException as e:
            print(f"No se pudo conectar al Arduino: {e}")
            self.arduino = None

        self.funciones_window = FuncionesWindow(self.arduino, self)
        self.estadisticas_window = EstadisticasWindow(self.arduino, self)

    @Slot()
    def inicio(self):
        self.funciones_window.showMaximized()
        self.hide()

    def informacion(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
"""
"""import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, QTimer
import serial
from ui_Proyecto_final import Ui_MainWindow

class FuncionesWindow(QWidget):
    def __init__(self, arduino, main_window):
        super().__init__()
        self.setWindowTitle("Funciones")
        self.arduino = arduino
        self.main_window = main_window

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.setSpacing(10)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)
        
        self.pushButton_4 = QPushButton("Encender Sistema")
        self.pushButton_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_4.setFixedHeight(100)

        self.pushButton_5 = QPushButton("Apagar Sistema")
        self.pushButton_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_5.setFixedHeight(100)

        button_layout.addWidget(self.pushButton_4)
        button_layout.addWidget(self.pushButton_5)

        main_layout.addLayout(button_layout)

        self.boton_volver = QPushButton("Volver a Principal")
        self.boton_volver.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.boton_volver.setFixedHeight(100)

        main_layout.addWidget(self.boton_volver)

        self.setLayout(main_layout)

        self.pushButton_4.clicked.connect(self.enviar_senal_b)
        self.pushButton_5.clicked.connect(self.enviar_senal_a)
        self.boton_volver.clicked.connect(self.volver_a_principal)

    def enviar_senal_a(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'A')
            print("Señal 'A' enviada: Sistema apagado.")
        else:
            print("No se pudo enviar la señal: Puerto cerrado.")

    def enviar_senal_b(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'B')
            print("Señal 'B' enviada: Sistema encendido.")
        else:
            print("No se pudo enviar la señal: Puerto cerrado.")

    def volver_a_principal(self):
        self.hide()
        self.main_window.show()


class EstadisticasWindow(QWidget):
    def __init__(self, arduino, main_window):
        super().__init__()
        self.setWindowTitle("Estadisticas")
        self.arduino = arduino
        self.main_window = main_window

        # Layout principal
        self.layout = QVBoxLayout()

        # Crear el QComboBox (menú desplegable)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Seleccione una opción")
        self.comboBox.addItem("Contador")
        self.comboBox.addItem("Matriz")
        self.comboBox.addItem("La mejor semana")
        self.comboBox.addItem("La peor semana")
        self.comboBox.addItem("Promedio mensual")
        self.comboBox.addItem("Promedio diario")

        # Conectar la selección del ComboBox a la función que actualiza el contenido
        self.comboBox.currentIndexChanged.connect(self.mostrar_datos)

        # Añadir el QComboBox al layout
        self.layout.addWidget(self.comboBox)

        # Crear un área de texto para mostrar los datos
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)  # Hacer que el área de texto no sea editable
        self.layout.addWidget(self.text_area)

        # Establecer el layout del widget
        self.setLayout(self.layout)

    def mostrar_datos(self):
        # Obtener el texto de la opción seleccionada
        selected_option = self.comboBox.currentText()

        if selected_option == "Contador":
            self.text_area.setText("Aquí van los datos del contador...")
            # Aquí puedes agregar la lógica para mostrar el contador
        elif selected_option == "Matriz":
            self.text_area.setText("Aquí va la matriz...")
            # Aquí puedes agregar la lógica para mostrar la matriz
        elif selected_option == "La mejor semana":
            self.text_area.setText("Aquí va la mejor semana...")
            # Aquí puedes agregar la lógica para mostrar la mejor semana
        elif selected_option == "La peor semana":
            self.text_area.setText("Aquí va la peor semana...")
            # Aquí puedes agregar la lógica para mostrar la peor semana
        elif selected_option == "Promedio mensual":
            self.text_area.setText("Aquí va el promedio mensual...")
            # Aquí puedes agregar la lógica para mostrar el promedio mensual
        elif selected_option == "Promedio diario":
            self.text_area.setText("Aquí va el promedio diario...")
            # Aquí puedes agregar la lógica para mostrar el promedio diario

    def volver_a_principal(self):
        self.hide()
        self.main_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        layout_botones = QVBoxLayout()

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout_botones.addItem(spacer)

        self.ui.pushButton_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_2.setFixedHeight(100)
        self.ui.pushButton_3.setFixedHeight(100)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ui.pushButton_2)
        button_layout.addWidget(self.ui.pushButton_3)

        layout_botones.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout_botones)
        self.setCentralWidget(central_widget)

        self.ui.pushButton_3.clicked.connect(self.inicio)

        try:
            self.arduino = serial.Serial('COM7', 9600)
            print("Conexión establecida con el Arduino.")
        except serial.SerialException as e:
            print(f"No se pudo conectar al Arduino: {e}")
            self.arduino = None

        self.funciones_window = FuncionesWindow(self.arduino, self)
        self.estadisticas_window = EstadisticasWindow(self.arduino, self)

    @Slot()
    def inicio(self):
        self.funciones_window.showMaximized()
        self.hide()

    def informacion(self):
        self.estadisticas_window.showMaximized()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
"""
"""import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, QTimer
import serial
from ui_Proyecto_final import Ui_MainWindow

class FuncionesWindow(QWidget):
    def __init__(self, arduino, main_window):
        super().__init__()
        self.setWindowTitle("Funciones")
        self.arduino = arduino
        self.main_window = main_window

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.setSpacing(10)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)
        
        self.pushButton_4 = QPushButton("Encender Sistema")
        self.pushButton_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_4.setFixedHeight(100)

        self.pushButton_5 = QPushButton("Apagar Sistema")
        self.pushButton_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pushButton_5.setFixedHeight(100)

        button_layout.addWidget(self.pushButton_4)
        button_layout.addWidget(self.pushButton_5)

        main_layout.addLayout(button_layout)

        self.boton_volver = QPushButton("Volver a Principal")
        self.boton_volver.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.boton_volver.setFixedHeight(100)

        main_layout.addWidget(self.boton_volver)

        self.setLayout(main_layout)

        self.pushButton_4.clicked.connect(self.enviar_senal_b)
        self.pushButton_5.clicked.connect(self.enviar_senal_a)
        self.boton_volver.clicked.connect(self.volver_a_principal)

    def enviar_senal_a(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'A')
            print("Señal 'A' enviada: Sistema apagado.")
        else:
            print("No se pudo enviar la señal: Puerto cerrado.")

    def enviar_senal_b(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(b'B')
            print("Señal 'B' enviada: Sistema encendido.")
        else:
            print("No se pudo enviar la señal: Puerto cerrado.")

    def volver_a_principal(self):
        self.hide()
        self.main_window.show()


class EstadisticasWindow(QWidget):
    def __init__(self, arduino, main_window):
        super().__init__()
        self.setWindowTitle("Estadísticas")
        self.arduino = arduino
        self.main_window = main_window

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Botón de menú para mostrar/ocultar el sidebar
        self.menu_button = QPushButton("Menú")
        self.menu_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.menu_button.setFixedHeight(40)
        self.menu_button.clicked.connect(self.toggle_sidebar)

        # Layout para el botón de menú
        main_layout.addWidget(self.menu_button)

        # Contenedor para el contenido principal
        self.content_layout = QVBoxLayout()

        # Crear las opciones del menú
        self.menu_widget = QWidget()
        self.menu_widget.setFixedWidth(200)
        self.menu_layout = QVBoxLayout(self.menu_widget)

        self.contador_button = QPushButton("Contador")
        self.matriz_button = QPushButton("Matriz")
        self.la_mejor_semana_button = QPushButton("La Mejor Semana")
        self.la_peor_semana_button = QPushButton("La Peor Semana")
        self.promedio_mensual_button = QPushButton("Promedio Mensual")
        self.promedio_diario_button = QPushButton("Promedio Diario")

        # Agregar las opciones al menú
        self.menu_layout.addWidget(self.contador_button)
        self.menu_layout.addWidget(self.matriz_button)
        self.menu_layout.addWidget(self.la_mejor_semana_button)
        self.menu_layout.addWidget(self.la_peor_semana_button)
        self.menu_layout.addWidget(self.promedio_mensual_button)
        self.menu_layout.addWidget(self.promedio_diario_button)

        # Hacer que el menú sea inicialmente invisible
        self.menu_widget.setVisible(False)

        # Agregar el menú y el contenido al layout principal
        main_layout.addWidget(self.menu_widget)
        main_layout.addLayout(self.content_layout)

        # Conectar botones del menú a funciones (aquí las definirás como desees)
        self.contador_button.clicked.connect(self.mostrar_contador)
        self.matriz_button.clicked.connect(self.mostrar_matriz)
        self.la_mejor_semana_button.clicked.connect(self.mostrar_la_mejor_semana)
        self.la_peor_semana_button.clicked.connect(self.mostrar_la_peor_semana)
        self.promedio_mensual_button.clicked.connect(self.mostrar_promedio_mensual)
        self.promedio_diario_button.clicked.connect(self.mostrar_promedio_diario)

    def toggle_sidebar(self):
        # Alternar la visibilidad del sidebar
        current_visible = self.menu_widget.isVisible()
        self.menu_widget.setVisible(not current_visible)

    def mostrar_contador(self):
        print("Mostrar contador")

    def mostrar_matriz(self):
        print("Mostrar matriz")

    def mostrar_la_mejor_semana(self):
        print("Mostrar la mejor semana")

    def mostrar_la_peor_semana(self):
        print("Mostrar la peor semana")

    def mostrar_promedio_mensual(self):
        print("Mostrar promedio mensual")

    def mostrar_promedio_diario(self):
        print("Mostrar promedio diario")

    def volver_a_principal(self):
        self.hide()
        self.main_window.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        layout_botones = QVBoxLayout()

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout_botones.addItem(spacer)

        self.ui.pushButton_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ui.pushButton_2.setFixedHeight(100)
        self.ui.pushButton_3.setFixedHeight(100)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ui.pushButton_2)
        button_layout.addWidget(self.ui.pushButton_3)

        layout_botones.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout_botones)
        self.setCentralWidget(central_widget)

        self.ui.pushButton_3.clicked.connect(self.inicio)

        try:
            self.arduino = serial.Serial('COM7', 9600)
            print("Conexión establecida con el Arduino.")
        except serial.SerialException as e:
            print(f"No se pudo conectar al Arduino: {e}")
            self.arduino = None

        self.funciones_window = FuncionesWindow(self.arduino, self)
        self.estadisticas_window = EstadisticasWindow(self.arduino, self)

    @Slot()
    def inicio(self):
        self.funciones_window.showMaximized()
        self.hide()

    def informacion(self):
        self.estadisticas_window.showMaximized()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
"""