from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QHeaderView
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer
from .ui_form.window_ui import Ui_MainWindow
from ..database.db_scripts import serv
from ..automation.login_automatize import LoginWorker
from ..automation.automatize import ScriptWorker
from ..utilities import utilite, stylie
from ..logger import logger


# Главное окно приложения
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('AvitoAPP')

        self.stopButton.hide()
        self.cookieButtonSave.hide()
        self.cancelButton.hide()

        # Конекты события действия при нажатии на кнопку
        self.startButton.clicked.connect(lambda: self.script_manager('start'))
        self.stopButton.clicked.connect(lambda: self.script_manager('stop'))
        self.loginButton.clicked.connect(lambda: self.login_manager('start'))
        self.cookieButtonSave.clicked.connect(lambda: self.login_manager('save'))
        self.cancelButton.clicked.connect(lambda: self.login_manager('exit'))
        self.updateButton.clicked.connect(lambda: self.update_table())  
        self.createButton.clicked.connect(lambda: self._add_line(func='new')) 

        logger.log_signal.connect(self.append_log)

        self.update_table()

        self.thred = None
        self.script_worker = None
        self.login_worker = None

    def append_log(self, message):
        self.log_edit.append(message)

    def script_manager(self, func):
        if func == 'start':
            if self.thred is None or not self.thred.isRunning():
                self.stopButton.show()
                self.startButton.hide()
                self.startButton.setEnabled(False)
                self.loginButton.setEnabled(False)
                
                
                self.thred = QThread()
                self.script_worker = ScriptWorker()

                self.script_worker.moveToThread(self.thred)

                self.thred.started.connect(self.script_worker.run)
                self.script_worker.finished.connect(self.thred.quit)
                self.script_worker.finished.connect(self.script_worker.deleteLater)
                self.thred.finished.connect(self.on_script_finished)

                self.thred.start()
            else:
                logger.info("Скрипт уже запущен")

        elif func == 'stop':
            self.stopButton.hide()
            self.startButton.show()
            if self.thred and self.thred.isRunning():
                self.script_worker.update_action('stop')
            else:
                logger.info("Скрипт уже запущен")

    def on_script_finished(self):
            logger.info("Скрипт завершён!!!")
            self.startButton.setEnabled(True)
            self.loginButton.setEnabled(True)
            self.stopButton.hide()
            self.startButton.show()
            self.thred = None
            self.script_worker = None
        

    def login_manager(self, func):
        if func == 'start':
            if self.thred is None or not self.thred.isRunning():
                self.loginButton.hide()
                self.startButton.setEnabled(False)
                self.loginButton.setEnabled(False)
                self.cookieButtonSave.show()
                self.cancelButton.show()

                self.thred = None
                self.script_worker = None
                self.thred = QThread()
                self.login_worker = LoginWorker()

                self.login_worker.moveToThread(self.thred)

                self.thred.started.connect(self.login_worker.run)
                self.login_worker.finished.connect(self.thred.quit)
                self.login_worker.finished.connect(self.login_worker.deleteLater)
                self.thred.finished.connect(self.on_login_script_finished)

                self.thred.start()
            else:
                logger.info("Скрипт уже запущен")

        elif func == 'save':
            if self.thred and self.thred.isRunning():
                self.login_worker.update_action('save')
                self.loginButton.show()
                self.cookieButtonSave.hide()
                self.cancelButton.hide()

            else:
                logger.info("Скрипт не запущен")

        elif func == 'exit':
            if self.thred and self.thred.isRunning():
                self.login_worker.update_action('exit')
                self.loginButton.show()
                self.cookieButtonSave.hide()
                self.cancelButton.hide()

            else:
                logger.info("Скрипт не запущен")

    def on_login_script_finished(self):
        logger.info("Скрипт завершён!!!")
        self.loginButton.show()
        self.startButton.setEnabled(True)
        self.loginButton.setEnabled(True)
        self.cookieButtonSave.hide()
        self.cancelButton.hide()

    #Работа с таблицей
    def __button(self, text, style, func):
        btn = QPushButton(text)
        btn.setStyleSheet(style)
        btn.clicked.connect(func)
        btn.setFixedSize(100, 50)
        return btn
    
    def __set_table_item(self, row, col, text):
        item = QTableWidgetItem(str(text))
        self.tableWidget.setItem(row, col, item)
        return item

    def update_table(self):
        data = serv.get_services()
        rows = len(data['data']) if data['code'] == 200 else 0
        
        self.tableWidget.clear()
        self.tableWidget.setRowCount(rows) 
        self.tableWidget.setColumnCount(6)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalHeaderLabels(["id", "Ссылка", "Название", "Обновлено", '', ''])
          
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        
        row = 0
        if data['data']:
            for item in data['data']:
                self.tableWidget.setRowHeight(row, 50)
                self._add_line(row, item)
                row += 1

            self.tableWidget.setColumnWidth(0, 5)
            self.tableWidget.setColumnWidth(1, 230)
            self.tableWidget.setColumnWidth(2, 80)
            self.tableWidget.setColumnWidth(3, 70)
            self.tableWidget.setColumnWidth(4, 100)
            self.tableWidget.setColumnWidth(5, 100)

    def _add_line(self, row=0, data=None, func='views'):
        if func == 'views':
            item = self.__set_table_item(row, 0, data[0])
            stylie.applying_styles_item(item)
            item = self.__set_table_item(row, 1, data[1])
            stylie.applying_styles_item(item)
            item = self.__set_table_item(row, 2, data[2])
            stylie.applying_styles_item(item)
            item = self.__set_table_item(row, 3, utilite.replace_third_dash_with_newline(data[3] if data[3] else '-'))
            stylie.applying_styles_item(item)
            btn = self.__button('Удалить', stylie.delete_btn, lambda: self._delete_item(data[0]))
            self.tableWidget.setCellWidget(row, 4, btn)
            btn = self.__button('Изменить', stylie.change_btn, lambda: self._add_line(item.row(), func='change'))
            self.tableWidget.setCellWidget(row, 5, btn)

        elif func == 'new':
            self.tableWidget.insertRow(0)
            self.tableWidget.setRowHeight(0, 50)
            id = self.__set_table_item(0, 0, '-')
            stylie.applying_styles_item(id)
            href = self.__set_table_item(0, 1, '')
            stylie.applying_styles_item(href, change=True)
            name = self.__set_table_item(0, 2, '')
            stylie.applying_styles_item(name, change=True)
            item = self.__set_table_item(0, 3, '-')
            stylie.applying_styles_item(item)
            btn = self.__button('Отмена', stylie.delete_btn, lambda: self._cancel_item(item.row()))
            self.tableWidget.setCellWidget(0, 4, btn)
            btn = self.__button('Сохранить', stylie.change_btn, lambda: self._create_item(href.text(), name.text()))
            self.tableWidget.setCellWidget(0, 5, btn)

        elif func == 'change':
            id = self.tableWidget.item(row, 0)
            href = self.tableWidget.item(row, 1)
            stylie.applying_styles_item(href, change=True)
            name = self.tableWidget.item(row, 2)
            stylie.applying_styles_item(name, change=True)
            btn = self.__button('Отмена', stylie.delete_btn, lambda: self._cancel_item(id.row(), id.text()))
            self.tableWidget.setCellWidget(row, 4, btn)
            btn = self.__button('Сохранить', stylie.change_btn, lambda: self._save_change_item(id.row(), id.text(), href.text(), name.text()))
            self.tableWidget.setCellWidget(row, 5, btn)

    def _delete_item(self, id):
        serv.delete_service(id)
        logger.info(f'Удаление объявления с id:{id}')
        self.update_table()

    def _cancel_item(self, row, id=None):
        if not id:
            self.tableWidget.removeRow(row)
        else:
            data = serv.get_service(id)
            self._add_line(row, data['data'])


    def _create_item(self, href, name):
        serv.create_service(href, name)
        logger.info(f'Запись добавленна в базу')
        self.update_table()

    def _save_change_item(self, row, id, href, name):
        serv.update_service(id, href, name)
        logger.info(f'Успешное изменение объявления id={id}')
        data = serv.get_service(id)
        self._add_line(row, data['data'])