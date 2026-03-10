import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QFrame)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    """Jendela utama aplikasi."""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        """Inisialisasi komponen UI"""
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(400, 500)
        self.setMinimumSize(350, 450)
        
        self.center_on_screen()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(20, 20, 20, 20)

        self.lbl_nama = QLabel("Nama Lengkap:")
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan Nama Lengkap")
 
        self.lbl_nim = QLabel("NIM:")
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
    
        self.lbl_kelas = QLabel("Kelas:")
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A")
        
        self.lbl_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["-- Pilih Jenis Kelamin --", "Laki-laki", "Perempuan"])
   
        btn_layout = QHBoxLayout()
        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")
        self.btn_tampilkan.setObjectName("btn_tampilkan")
        self.btn_reset.setObjectName("btn_reset")
        
        btn_layout.addWidget(self.btn_tampilkan)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch()

        self.result_frame = QFrame()
        self.result_frame.setObjectName("result_frame")
        self.result_layout = QVBoxLayout(self.result_frame)
        
        self.lbl_hasil = QLabel("")
        self.lbl_hasil.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.result_layout.addWidget(self.lbl_hasil)
        self.result_frame.setVisible(False)

        main_layout.addWidget(self.lbl_nama)
        main_layout.addWidget(self.input_nama)
        main_layout.addWidget(self.lbl_nim)
        main_layout.addWidget(self.input_nim)
        main_layout.addWidget(self.lbl_kelas)
        main_layout.addWidget(self.input_kelas)
        main_layout.addWidget(self.lbl_jk)
        main_layout.addWidget(self.combo_jk)
        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.result_frame)
        main_layout.addStretch()

        self.setLayout(main_layout)
        
        self.setStyleSheet("""
            QWidget {
                font-family: Arial, sans-serif;
                font-size: 13px;
            }
            QLineEdit, QComboBox {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #28a745;
            }
            QPushButton#btn_tampilkan {
                background-color: #3498db;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                border: none;
            }
            QPushButton#btn_tampilkan:hover {
                background-color: #2980b9;
            }
            QPushButton#btn_reset {
                background-color: #95a5a6;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                border: none;
            }
            QPushButton#btn_reset:hover {
                background-color: #7f8c8d;
            }
            QFrame#result_frame {
                background-color: #d4edda;
                border-left: 4px solid #28a745;
                border-radius: 2px;
                padding: 5px;
            }
            QLabel {
                color: #333;
            }
        """)

    def setup_connections(self):
        """Setup signal-slot connections."""
        self.btn_tampilkan.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_data)

    def tampilkan_data(self):
        """Mengambil data dari input, validasi, dan menampilkan hasilnya."""
        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        kelas = self.input_kelas.text().strip()
        jk = self.combo_jk.currentText()
        jk_index = self.combo_jk.currentIndex()

        if not nama or not nim or not kelas or jk_index == 0:
            QMessageBox.warning(self, "Validasi Error", "Semua field harus diisi dan dipilih dengan benar!")
            return

        teks_hasil = (
            f"<b>DATA BIODATA</b><br><br>"
            f"Nama: {nama}<br>"
            f"NIM: {nim}<br>"
            f"Kelas: {kelas}<br>"
            f"Jenis Kelamin: {jk}"
        )
        
        self.lbl_hasil.setText(teks_hasil)
        self.result_frame.setVisible(True)

    def reset_data(self):
        """Mengosongkan semua input dan menyembunyikan hasil."""
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        
        self.lbl_hasil.clear()
        self.result_frame.setVisible(False)

    def center_on_screen(self):
        """Posisikan jendela di tengah layar"""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

def main():
    """Entry point aplikasi."""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()