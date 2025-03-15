import sqlite3
import sys
import os

# Для запуска с файла .exe
if getattr(sys, 'frozen', False):
    ROOT_PATH = sys._MEIPASS
else:
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(ROOT_PATH, 'app', 'database', 'table.sql')
DB_PATH = os.path.join(ROOT_PATH, 'app', 'database', 'base.sqlite')

# Для запуска с консоли
# DATA_PATH = 'app\\database\\table.sql'
# DB_PATH = 'app\\database\\base.sqlite'


class DBManager:
    def __init__(self):
        if not self.__check_base():
            self.__create_base()

    def __check_base(self) -> bool:
        '''Проверка есть ли БД'''
        return os.path.exists(DB_PATH)

    def __connect_to_base(self):
        '''Подключение к БД'''
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        return conn, cur

    def __create_base(self):
        '''Создание БД'''
        conn, cur = self.__connect_to_base()
        try:
            cur.executescript(open(DATA_PATH, encoding="utf-8").read())
            conn.commit()
            print('Tables are created')
        except sqlite3.Error as ex:
            print(ex)
        finally:
            conn.close()

    def execute(self, query: str, args=(), many: bool = True):
        '''Выполнение SQL скрипта'''
        conn, cur = self.__connect_to_base()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            if result == None or result == []:
                return {"code": 201, "data": None}
            else:
                return {"code": 200, "data": result}
        except sqlite3.Error as er:
            eror = {"code": 400, "data": {'eror': str(er)}}
            print(eror)
            return eror
        finally:
            conn.close()