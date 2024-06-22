import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLineEdit, QLabel, QTextEdit
from quantum_control.hardware.galvo_mirror import GalvoMirror
from quantum_control.hardware.photodiode import Photodiode

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quantum Lab Control - Galvo Mirrors & Photodiode')
        self.galvo = GalvoMirror('Dev1', 'ao0', 'ao1')
        self.photodiode = Photodiode('Dev1', 'ai0')
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        self.x_input = QLineEdit(self)
        self.x_input.setPlaceholderText('Enter X Voltage')
        layout.addWidget(QLabel('X Voltage:'))
        layout.addWidget(self.x_input)
        
        self.y_input = QLineEdit(self)
        self.y_input.setPlaceholderText('Enter Y Voltage')
        layout.addWidget(QLabel('Y Voltage:'))
        layout.addWidget(self.y_input)
        
        move_button = QPushButton('Move', self)
        move_button.clicked.connect(self.move_galvo)
        layout.addWidget(move_button)

        start_button = QPushButton('Start', self)
        start_button.clicked.connect(self.start_galvo)
        layout.addWidget(start_button)

        stop_button = QPushButton('Stop', self)
        stop_button.clicked.connect(self.stop_galvo)
        layout.addWidget(stop_button)
        
        self.data_display = QTextEdit(self)
        self.data_display.setReadOnly(True)
        layout.addWidget(QLabel('Photodiode Data:'))
        layout.addWidget(self.data_display)
        
        measure_button = QPushButton('Measure Photodiode', self)
        measure_button.clicked.connect(self.measure_photodiode)
        layout.addWidget(measure_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def move_galvo(self):
        x_voltage = float(self.x_input.text())
        y_voltage = float(self.y_input.text())
        self.galvo.move_to(x_voltage, y_voltage)

    def start_galvo(self):
        self.galvo.start()

    def stop_galvo(self):
        self.galvo.stop()

    def measure_photodiode(self):
        self.photodiode.start_measurement()
        data = self.photodiode.read_data()
        self.data_display.append(str(data))
        self.photodiode.stop_measurement()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
