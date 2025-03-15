from PyQt6.QtWidgets import QApplication
import sys
from app.window_forms.window import MainWindow


def window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    window()
    