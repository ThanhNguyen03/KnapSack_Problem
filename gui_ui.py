# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grBtable = QGroupBox(self.centralwidget)
        self.grBtable.setObjectName(u"grBtable")
        self.grBtable.setGeometry(QRect(310, 20, 281, 411))
        self.tableView = QTableView(self.grBtable)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(30, 20, 221, 311))
        self.grBmaxwei_2 = QGroupBox(self.grBtable)
        self.grBmaxwei_2.setObjectName(u"grBmaxwei_2")
        self.grBmaxwei_2.setGeometry(QRect(0, 340, 211, 61))
        self.viewMaxWeight = QLineEdit(self.grBmaxwei_2)
        self.viewMaxWeight.setObjectName(u"viewMaxWeight")
        self.viewMaxWeight.setGeometry(QRect(30, 20, 171, 31))
        self.viewMaxWeight.setMouseTracking(False)
        self.viewMaxWeight.setReadOnly(True)
        self.grBbag = QGroupBox(self.centralwidget)
        self.grBbag.setObjectName(u"grBbag")
        self.grBbag.setGeometry(QRect(30, 20, 261, 381))
        self.grBvalue = QGroupBox(self.grBbag)
        self.grBvalue.setObjectName(u"grBvalue")
        self.grBvalue.setGeometry(QRect(30, 20, 181, 61))
        self.value = QLineEdit(self.grBvalue)
        self.value.setObjectName(u"value")
        self.value.setGeometry(QRect(30, 20, 121, 31))
        self.value.setInputMethodHints(Qt.ImhPreferNumbers)
        self.grBweight = QGroupBox(self.grBbag)
        self.grBweight.setObjectName(u"grBweight")
        self.grBweight.setGeometry(QRect(30, 90, 181, 61))
        self.weight = QLineEdit(self.grBweight)
        self.weight.setObjectName(u"weight")
        self.weight.setGeometry(QRect(30, 20, 121, 31))
        self.grBmaxwei = QGroupBox(self.grBbag)
        self.grBmaxwei.setObjectName(u"grBmaxwei")
        self.grBmaxwei.setGeometry(QRect(30, 170, 211, 61))
        self.maxWeight = QLineEdit(self.grBmaxwei)
        self.maxWeight.setObjectName(u"maxWeight")
        self.maxWeight.setGeometry(QRect(30, 20, 171, 31))
        self.btnSubmit = QPushButton(self.grBbag)
        self.btnSubmit.setObjectName(u"btnSubmit")
        self.btnSubmit.setGeometry(QRect(70, 240, 111, 31))
        self.btnReset = QPushButton(self.grBbag)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(70, 280, 111, 31))
        self.btnCalc = QPushButton(self.grBbag)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(70, 320, 111, 31))
        self.grBresult = QGroupBox(self.centralwidget)
        self.grBresult.setObjectName(u"grBresult")
        self.grBresult.setGeometry(QRect(30, 430, 561, 131))
        self.result = QLineEdit(self.grBresult)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(130, 30, 121, 31))
        self.result.setMouseTracking(False)
        self.result.setReadOnly(True)
        self.label = QLabel(self.grBresult)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 121, 31))
        self.label_2 = QLabel(self.grBresult)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 251, 31))
        self.valueresult = QLineEdit(self.grBresult)
        self.valueresult.setObjectName(u"valueresult")
        self.valueresult.setGeometry(QRect(270, 80, 121, 31))
        self.valueresult.setMouseTracking(False)
        self.valueresult.setReadOnly(True)
        self.weightresult = QLineEdit(self.grBresult)
        self.weightresult.setObjectName(u"weightresult")
        self.weightresult.setGeometry(QRect(410, 80, 121, 31))
        self.weightresult.setMouseTracking(False)
        self.weightresult.setReadOnly(True)
        self.label_3 = QLabel(self.grBresult)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 90, 16, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 619, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hill Climbing For Knapsack", None))
        self.grBtable.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng gi\u00e1 tr\u1ecb v\u00e0 kh\u1ed1i l\u01b0\u1ee3ng t\u01b0\u01a1ng \u1ee9ng c\u1ee7a t\u00fai:", None))
        self.grBmaxwei_2.setTitle(QCoreApplication.translate("MainWindow", u"Kh\u1ed1i l\u01b0\u1ee3ng l\u1edbn nh\u1ea5t t\u00fai c\u00f3 th\u1ec3 mang:", None))
        self.grBbag.setTitle(QCoreApplication.translate("MainWindow", u"V\u1eadt ph\u1ea9m", None))
        self.grBvalue.setTitle(QCoreApplication.translate("MainWindow", u"Gi\u00e1 tr\u1ecb v\u1eadt ph\u1ea9m:", None))
        self.grBweight.setTitle(QCoreApplication.translate("MainWindow", u"Kh\u1ed1i l\u01b0\u1ee3ng c\u1ee7a v\u1eadt ph\u1ea9m:", None))
        self.grBmaxwei.setTitle(QCoreApplication.translate("MainWindow", u"Kh\u1ed1i l\u01b0\u1ee3ng l\u1edbn nh\u1ea5t t\u00fai c\u00f3 th\u1ec3 mang:", None))
        self.btnSubmit.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnCalc.setText(QCoreApplication.translate("MainWindow", u"T\u00ednh to\u00e1n", None))
        self.grBresult.setTitle(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn v\u1eadt ph\u1ea9m th\u1ee9:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"V\u1edbi t\u1ed5ng gi\u00e1 tr\u1ecb v\u00e0 t\u1ed5ng kh\u1ed1i l\u01b0\u1ee3ng l\u1ea7n l\u01b0\u1ee3t l\u00e0:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u",", None))
    # retranslateUi

