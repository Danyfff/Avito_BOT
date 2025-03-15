import os, time, sys, json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PyQt6.QtCore import QObject, pyqtSignal
from ..logger import logger


# Для запуска с файла .exe
if getattr(sys, 'frozen', False):
    ROOT_PATH = sys._MEIPASS
else:
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

cookies_path = os.path.join(ROOT_PATH, 'app', 'cookies', 'cookies.txt')
chromedriver_path = os.path.join(ROOT_PATH, 'app', 'chromedriver-win64', 'chromedriver.exe')

# Для запуска с консоли
# cookies_path = 'app\\cookies\\cookies.txt'
# chromedriver_path = 'chromedriver-win64\\chromedriver.exe'

class LoginWorker(QObject):
    action_changed = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.login_action = 'login'
        self.driver = None

    def run(self):
        logger.info('Войдите в аккаунт и собирите Cookies')
        self.login_action = 'login'
        self.login()

    def update_action(self, action):
        self.login_action = action
        if action == 'save':
            logger.info(f"Собираем Cookies...")
        else: logger.info(f"Закрываем браузер...")


    # Инициализация драйвера
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-javascript")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--log-level=3')
        service = Service(chromedriver_path, log_path=os.devnull)
        return webdriver.Chrome(service=service, options=options)

    # Функция для сохранения cookies
    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(cookies_path, 'w') as file:
            json.dump(cookies, file, indent=4)

    # Функция ожидания входа в аккаунт
    def login(self):
        self.driver = self.setup_driver()
        try:
            while self.login_action == 'login':
                self.driver.get('https://www.avito.ru/#login')
                time.sleep(0.5)

            if self.login_action == 'save':
                self.save_cookies()
                logger.info(f'Cookies собраны')

        except Exception as ex:
                logger.error(f'{ex}')
        
        finally:
            try:
                self.finished.emit()
                self.driver.quit()
            except Exception as ex:
                logger.error(f'{ex}')


