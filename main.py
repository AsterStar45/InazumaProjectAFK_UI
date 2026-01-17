import sys
import os

if sys.platform == "win32":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "InazumaAFK.App.Bot.42"
    )

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from ui.main_window import MainWindow

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main():
    app = QApplication(sys.argv)

    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.ico")
    app.setWindowIcon(QIcon(resource_path("assets/icon.ico")))

    window = MainWindow()


    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()