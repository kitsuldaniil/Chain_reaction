# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(350, 350)
        MainWin.setMinimumSize(QtCore.QSize(350, 350))
        MainWin.setMaximumSize(QtCore.QSize(350, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("winicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 30, 280, 280))
        self.tableView.setMinimumSize(QtCore.QSize(280, 280))
        self.tableView.setMaximumSize(QtCore.QSize(280, 280))
        self.tableView.setShowGrid(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setHighlightSections(True)
        self.tableView.verticalHeader().setVisible(False)
        self.levelspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.levelspinBox.setGeometry(QtCore.QRect(300, 0, 42, 22))
        self.levelspinBox.setToolTipDuration(10)
        self.levelspinBox.setMinimum(1)
        self.levelspinBox.setMaximum(2)
        self.levelspinBox.setObjectName("levelspinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 71, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(7)
        self.label.setObjectName("label")
        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.test.setObjectName("test")
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setToolTipDuration(2)
        self.menuOptions.setStatusTip("")
        self.menuOptions.setToolTipsVisible(True)
        self.menuOptions.setObjectName("menuOptions")
        MainWin.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWin)
        self.action.setObjectName("action")
        self.action2 = QtWidgets.QAction(MainWin)
        self.action2.setObjectName("action2")
        self.new_game = QtWidgets.QAction(MainWin)
        self.new_game.setObjectName("new_game")
        self.settings = QtWidgets.QAction(MainWin)
        self.settings.setObjectName("settings")
        self.menuGame.addAction(self.new_game)
        self.menuGame.addAction(self.settings)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "Цепная реакция"))
        self.levelspinBox.setToolTip(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Уровень сложности</span></p></body></html>"))
        self.label.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Уровень</span></p></body></html>"))
        self.test.setText(_translate("MainWin", "PushButton"))
        self.menuGame.setTitle(_translate("MainWin", "Игра"))
        self.menuOptions.setToolTip(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:9pt;\">Правила Игры</span></p></body></html>"))
        self.menuOptions.setTitle(_translate("MainWin", "Помощь"))
        self.action.setText(_translate("MainWin", "1"))
        self.action2.setText(_translate("MainWin", "2"))
        self.new_game.setText(_translate("MainWin", "Новая"))
        self.settings.setText(_translate("MainWin", "Настройки"))

