from PyQt6.QtCore import pyqtSignal, QObject

class Logger(QObject):
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.log_level = "INFO"

    def __log(self, message, level="INFO"):
        """Метод для отправки сообщения в лог"""
        formatted_message = f"[{level}] {message}"
        self.log_signal.emit(formatted_message)

    def info(self, message):
        """Логирование уровня INFO"""
        self.__log(message, "INFO")

    def warning(self, message):
        """Логирование уровня WARNING"""
        self.__log(message, "WARNING")

    def error(self, message):
        """Логирование уровня ERROR"""
        self.__log(message, "ERROR")

logger = Logger()