# Form implementation generated from reading ui file 'app\window_forms\ui_form\ui\window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 852)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(621, 600))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.createButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createButton.setStyleSheet("    QPushButton {\n"
"        background-color: #1976D2; /* Синий цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 5px 32px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 24px;\n"
"        margin: 4px 2px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #1565C0; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #0D47A1; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.createButton.setObjectName("createButton")
        self.verticalLayout_3.addWidget(self.createButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setMinimumSize(QtCore.QSize(150, 40))
        self.startButton.setStyleSheet("    QPushButton {\n"
"        background-color: #4CAF50; /* Зеленый цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 16px;\n"
"        padding: 5px 10px;\n"
"        margin: 4px 2px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #45a049; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #3e8e41; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setMinimumSize(QtCore.QSize(150, 40))
        self.stopButton.setStyleSheet("    QPushButton {\n"
"        background-color: #f44336; /* Красный цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 5px 10px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 16px;\n"
"        margin: 4px 2px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #d32f2f; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #b71c1c; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setMinimumSize(QtCore.QSize(150, 40))
        self.loginButton.setStyleSheet("    QPushButton {\n"
"        background-color: #1976D0; /* Синий цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 5px 10px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 16px;\n"
"        margin: 2px 1px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #1565C0; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #0D47A1; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.cookieButtonSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cookieButtonSave.setMinimumSize(QtCore.QSize(150, 40))
        self.cookieButtonSave.setStyleSheet("    QPushButton {\n"
"        background-color: #1976D0; /* Синий цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 5px 10px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 16px;\n"
"        margin: 2px 1px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #1565C0; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #0D47A1; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.cookieButtonSave.setObjectName("cookieButtonSave")
        self.verticalLayout.addWidget(self.cookieButtonSave)
        self.cancelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(150, 40))
        self.cancelButton.setStyleSheet("    QPushButton {\n"
"        background-color: #f44336; /* Красный цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 5px 10px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 16px;\n"
"        margin: 4px 2px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #d32f2f; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #b71c1c; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout.addWidget(self.cancelButton)
        self.updateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.updateButton.setMinimumSize(QtCore.QSize(150, 40))
        self.updateButton.setStyleSheet("    QPushButton {\n"
"        background-color: #1976D0; /* Синий цвет */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 5px 10px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        font-size: 16px;\n"
"        margin: 2px 1px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #1565C0; /* Цвет при наведении на кнопку */\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #0D47A1; /* Цвет при нажатии на кнопку */\n"
"    }")
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout.addWidget(self.updateButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label.setSizeIncrement(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.log_edit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.log_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.log_edit.setReadOnly(True)
        self.log_edit.setObjectName("log_edit")
        self.verticalLayout_2.addWidget(self.log_edit)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createButton.setText(_translate("MainWindow", "+"))
        self.startButton.setText(_translate("MainWindow", "Старт"))
        self.stopButton.setText(_translate("MainWindow", "Стоп"))
        self.loginButton.setText(_translate("MainWindow", "Войти в аккаунт"))
        self.cookieButtonSave.setText(_translate("MainWindow", "Собрать cookie"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.updateButton.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "Консоль логов"))
