from .ui_form.cookies_ui import Ui_CookiesWindow 
from PyQt6.QtWidgets import QMainWindow
import json
import os


class CookiesWindow(QMainWindow, Ui_CookiesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Cookise')
        
        self.closeButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.save_cookies)
        self.cookies_path = os.path.join(os.getcwd(), 'app', 'cookies', 'cookies1.txt')
        
    def save_cookies(self):
        cookies = self.textEdit.toPlainText()
        print(cookies)
        with open(self.cookies_path, 'w', encoding='utf-8') as file:
            file.write(cookies)
        
        self.close()