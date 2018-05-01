# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelpWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpWin(object):
    def setupUi(self, HelpWin):
        HelpWin.setObjectName("HelpWin")
        HelpWin.resize(278, 377)
        self.centralwidget = QtWidgets.QWidget(HelpWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 251, 421))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        HelpWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HelpWin)
        self.statusbar.setObjectName("statusbar")
        HelpWin.setStatusBar(self.statusbar)

        self.retranslateUi(HelpWin)
        QtCore.QMetaObject.connectSlotsByName(HelpWin)

    def retranslateUi(self, HelpWin):
        _translate = QtCore.QCoreApplication.translate
        HelpWin.setWindowTitle(_translate("HelpWin", "Помощь"))
        self.label.setText(_translate("HelpWin", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; font-weight:600; color:#000000;\">Задача:</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\"> зачеркнуть крестиком все </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">цветные фигуры на поле поочереди</span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">одну за одной. Черный крест - </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">ваша текущая позиция;</span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; font-weight:600; color:#000000;\">Как играть в Цепная реакция:</span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">Можно ходить по горизонтали или </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">вертикили на любое расстояние, </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">соблюдая условие - либо цвет, </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">либа форма следующей фигуры</span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">должна совпадать с исходной; </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">Управление: кликаете мышкой </span></p><p align=\"justify\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:15px; color:#000000;\">по цветным фигурам. </span></p></body></html>"))

