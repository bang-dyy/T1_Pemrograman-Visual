import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QMessageBox, QFrame)
from PySide6.QtCore import Qt

class KonversiSuhu(QWidget):
    """Jendela utama aplikasi Konversi Suhu."""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        """Inisialisasi komponen UI"""
        self.setWindowTitle("Konversi Suhu")
        self.resize(400, 450)
        self.center_on_screen()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(25, 25, 25, 25)

        self.lbl_header = QLabel("KONVERSI SUHU")
        self.lbl_header.setObjectName("header")
        self.lbl_header.setAlignment(Qt.AlignCenter)

        self.lbl_input = QLabel("Masukkan Suhu (Celsius):")
        self.input_celsius = QLineEdit()
        btn_layout = QHBoxLayout()
        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin = QPushButton("Kelvin")
        self.btn_reamur = QPushButton("Reamur")
        
        btn_layout.addWidget(self.btn_fahrenheit)
        btn_layout.addWidget(self.btn_kelvin)
        btn_layout.addWidget(self.btn_reamur)

        self.result_frame = QFrame()
        self.result_frame.setObjectName("result_frame")
        self.result_layout = QVBoxLayout(self.result_frame)
        
        self.lbl_title_hasil = QLabel("Hasil Konversi:")
        self.lbl_title_hasil.setStyleSheet("font-weight: bold; color: #003366;")
        
        self.lbl_hasil = QLabel("-")
        self.lbl_hasil.setObjectName("lbl_hasil")
        
        self.result_layout.addWidget(self.lbl_title_hasil)
        self.result_layout.addWidget(self.lbl_hasil)

        main_layout.addWidget(self.lbl_header)
        main_layout.addWidget(self.lbl_input)
        main_layout.addWidget(self.input_celsius)
        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.result_frame)
        main_layout.addStretch()

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget { background-color: #f8f9fa; font-family: Segoe UI, sans-serif; }
            QLabel#header {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                font-size: 18px;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #a8e6cf;
                border-radius: 6px;
                font-size: 16px;
                background-color: #f0fff4;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover { background-color: #2980b9; }
            QFrame#result_frame {
                background-color: #d1e9ff;
                border-left: 5px solid #004085;
                border-radius: 4px;
                padding: 15px;
            }
            QLabel#lbl_hasil { font-size: 15px; color: #004085; }
        """)

    def setup_connections(self):
        """Menghubungkan tombol ke fungsi konversi."""
        self.btn_fahrenheit.clicked.connect(lambda: self.hitung_konversi("Fahrenheit"))
        self.btn_kelvin.clicked.connect(lambda: self.hitung_konversi("Kelvin"))
        self.btn_reamur.clicked.connect(lambda: self.hitung_konversi("Reamur"))

    def hitung_konversi(self, tipe):
        """Fungsi logika konversi dan validasi."""
        try:
            celsius = float(self.input_celsius.text())
            if tipe == "Fahrenheit":
                hasil = (celsius * 9/5) + 32
                unit = "Fahrenheit"
            elif tipe == "Kelvin":
                hasil = celsius + 273.15
                unit = "Kelvin"
            elif tipe == "Reamur":
                hasil = celsius * 4/5
                unit = "Reamur"

            self.lbl_hasil.setText(f"{celsius} Celsius = {hasil:.2f} {unit}")

        except ValueError:
            QMessageBox.critical(self, "Error Input", "Masukkan angka yang valid untuk suhu Celsius!")
            self.input_celsius.clear()

    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

def main():
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()