from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QLabel,
    QLineEdit,
    QApplication
)
from PySide6.QtCore import Qt
import sys

from core.regions import REGIONES
from core.bot_worker import BotWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inazuma AFK Bot")

        # ===== Ajustar a 3/4 de pantalla =====
        screen = QApplication.primaryScreen().availableGeometry()
        self.resize(
            int(screen.width() * 0.75),
            int(screen.height() * 0.75)
        )

        self.bot = None

        # ===== Widget central =====
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # =========================
        # CONFIG EQUIPO RIVAL
        # =========================
        rival_layout = QHBoxLayout()

        self.rival_label = QLabel("Equipo rival (separado por comas):")
        self.rival_input = QLineEdit()
        self.rival_input.setPlaceholderText("LUZ, ETE, SOMBRA")

        rival_layout.addWidget(self.rival_label)
        rival_layout.addWidget(self.rival_input)

        main_layout.addLayout(rival_layout)

        # =========================
        # BOTONES
        # =========================
        btn_layout = QHBoxLayout()

        self.start_btn = QPushButton("Iniciar bot")
        self.stop_btn = QPushButton("Detener bot")

        self.stop_btn.setEnabled(False)

        self.start_btn.clicked.connect(self.start_bot)
        self.stop_btn.clicked.connect(self.stop_bot)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        main_layout.addLayout(btn_layout)

        # =========================
        # LOG
        # =========================
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)

        main_layout.addWidget(self.log_box)

    # =========================
    # ACTUALIZAR REGIONES
    # =========================
    def actualizar_equipo_rival(self):
        texto = self.rival_input.text().upper().strip()
        if not texto:
            return

        palabras = [p.strip() for p in texto.split(",") if p.strip()]

        for r in REGIONES:
            if r["nombre"] == "Equipo rival":
                r["palabras"] = palabras
                break

        self.add_log(f"Equipo rival actualizado: {palabras}")

    # =========================
    # CONTROL BOT
    # =========================
    def start_bot(self):
        self.actualizar_equipo_rival()

        if self.bot is None or not self.bot.isRunning():
            self.bot = BotWorker()
            self.bot.log.connect(self.add_log)
            self.bot.start()

            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)

    def stop_bot(self):
        if self.bot:
            self.bot.stop()
            self.bot.wait()

            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)

    # =========================
    # LOG
    # =========================
    def add_log(self, text):
        self.log_box.append(text)


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
