from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

class Utilities:
    # Утилита для форматирования строки
    def replace_third_dash_with_newline(self, s: str) -> str:
        parts = s.split('-')
        if len(parts) < 4:
            return s 
        first_part = '-'.join(parts[:3])
        second_part = ':'.join(parts[3:])
        return f"{first_part}\n{second_part}"
  
utilite = Utilities()

class Stylies:
    # Стили кнопок
    change_btn = "QPushButton {background-color: #3F51B5; border: none; color: white; padding: 0px; font-size: 16px; margin: 2px 2px; border-radius: 6px;} QPushButton:hover {background-color: #5C6BC0;} QPushButton:pressed {background-color: #3949AB;}"
    delete_btn = "QPushButton {background-color: #E53935; border: none; color: white; padding: 0px; font-size: 14px; margin: 2px 2px; border-radius: 6px;} QPushButton:hover {background-color: #D32F2F;} QPushButton:pressed {background-color: #B71C1C;}"

    def applying_styles_item(self, item:QTableWidgetItem, change=False):
        if not change:
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
            # item.setFlags(Qt.ItemFlag.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)

stylie = Stylies()