import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class DarkModeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.proxy_process = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dark Mode Proxy")
        
        layout = QVBoxLayout()

        self.status_label = QLabel("Status: OFF")
        layout.addWidget(self.status_label)

        self.start_btn = QPushButton("Start Dark Mode")
        self.start_btn.clicked.connect(self.start_proxy)
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop Dark Mode")
        self.stop_btn.clicked.connect(self.stop_proxy)
        layout.addWidget(self.stop_btn)

        self.setLayout(layout)

    def start_proxy(self):
        if not self.proxy_process:
            self.proxy_process = subprocess.Popen(
                ["mitmdump", "-s", "injector.py"]
            )
            self.status_label.setText("Status: ON")

    def stop_proxy(self):
        if self.proxy_process:
            self.proxy_process.terminate()
            self.proxy_process = None
            self.status_label.setText("Status: OFF")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DarkModeApp()
    window.show()
    sys.exit(app.exec_())