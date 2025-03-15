import os
import json
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..database.db_scripts import serv
from PyQt6.QtCore import QObject, pyqtSignal
from ..logger import logger
import datetime




timestamp = lambda: time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    
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

class ScriptWorker(QObject):
    action_changed = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.script_action = 'start'
        self.driver = None

    def run(self):
        logger.info('Начало работы скрипта...')
        self.script_action = 'start'
        self.automate()

    def update_action(self, action):
        self.script_action = action
        logger.info(f"Завершение работы скрипта...")
    
    # Инициализация драйвера
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--disable-javascript")
        options.add_argument('--headless')
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

    # Функция для вставки cookies
    def add_cookies(self):
        try:
            self.driver.delete_all_cookies()
            with open(cookies_path, 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            return True
        except:
            return False
             

    # Функция для скриншота для тестирования
    def take_screenshot(self):
    # Создаем папку, если она не существует
        screenshot_dir = os.path.join(os.getcwd(), 'app', 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Формируем имя файла
        screenshot_path = os.path.join(screenshot_dir, f'{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}_photo.png')
        self.driver.get_screenshot_as_file(screenshot_path)


    # Функция самой автоматизации
    def automate(self):
        try:
            try:
                self.driver = self.setup_driver()
                if self.script_action == 'stop':
                                return
                logger.info(f'ChromeDriver запустился')
            except Exception as ex: logger.info(f'ChromeDriver: {ex}')

            try:
                self.driver.get('https://www.avito.ru/')
                if self.script_action == 'stop':
                            return
                logger.info(f'Открыл сайт Авито')
            except Exception as ex: logger.info(f'Ошибка при загузке сайта: {ex}')

            if not self.add_cookies():
                 logger.error(f'Ошибка при вставке Cookies: Попробуйте пересохранить Cookies')
                 return
                 
            if self.script_action == 'stop':
                        return
            
            LABEL = (By.XPATH, '//div[@class="styles-block-wrapper-Ari_D"]')
            CHECKBOX_SERVICE = (By.XPATH, '//label[@role="switch"]')
            CHECKBOX_TIME_SERVICE = (By.XPATH, '//div[@class="styles-block-wrapper-Ari_D"]//div[@role="button"]')
            CHECKBOX_TIME_SERVICE = (By.XPATH, '//div[@class="styles-item-view-content-yk4jH"]//div[@role="button"]')
            ACCOUNT = (By.XPATH, '//a[@class="index-module-nav-link-YtJag index-module-login-K8jzD"]')
            TEXT_CHECKBOX_TIME_SERVICE = (By.CLASS_NAME, 'h6')

            try:
                 label = WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located(ACCOUNT))
                 if label:
                      logger.error(f'Ошибка профиля. Зайдите в аккаунт!')
                      return
            except: pass
                 
            data = serv.get_services()
                
            for url in data['data']:
                if self.script_action == 'stop':
                        return
                
                try:
                    self.driver.get(url[1])
                    label = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(LABEL))
                    time.sleep(2)

                    if self.script_action == 'stop':
                            return

                    try:
                        button_status = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located(CHECKBOX_SERVICE))

                        if self.script_action == 'stop':
                            return
                                
                        if button_status.get_attribute("aria-checked") == "false":
                            button_status.click()
                            logger.info(f'[id={url[0]}] Тумблер переключен')
                            time.sleep(0.5)

                            try:
                                buttons_time_status = WebDriverWait(self.driver, 10).until(
                                    EC.visibility_of_all_elements_located(CHECKBOX_TIME_SERVICE))

                                for btn in buttons_time_status:
                                    if 'Сегодня' in btn.text:
                                        btn.click()
                                        logger.info(f'[id={url[0]}] Галочка "Сегодня" включена')

                                # buttons_time_status[1].click()
                                # logger.info(f'[id={url[0]}] Галочка "Сегодня" включена')

                            except Exception as ex: logger.error(f'[id={url[0]}] Не найден Элемент "CHECKBOX_TIME_SERVICE"')
                            
                            serv.update_service_time(url[0], timestamp())
                            
                        else:
                            logger.info(f'[id={url[0]}] Все галочки уже стоят!!!')

                        self.save_cookies()

                    except Exception as e: logger.error(f'[id={url[0]}] Не найден Элемент "CHECKBOX_SERVICE"')

                except: logger.error(f'[id={url[0]}] Не найден элемент "LABEL"')

        finally:
            self.finished.emit()
            self.driver.quit()
            