# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_gui_main(object):
    def setupUi(self, gui_main):
        if not gui_main.objectName():
            gui_main.setObjectName(u"gui_main")
        gui_main.resize(1200, 800)
        font = QFont()
        font.setPointSize(30)
        font.setBold(False)
        gui_main.setFont(font)
        self.actionDokumentation = QAction(gui_main)
        self.actionDokumentation.setObjectName(u"actionDokumentation")
        self.actionHilfe = QAction(gui_main)
        self.actionHilfe.setObjectName(u"actionHilfe")
        self.action = QAction(gui_main)
        self.action.setObjectName(u"action")
        self.actionEinstellungen = QAction(gui_main)
        self.actionEinstellungen.setObjectName(u"actionEinstellungen")
        self.action_ffnen = QAction(gui_main)
        self.action_ffnen.setObjectName(u"action_ffnen")
        self.actionSpeichern = QAction(gui_main)
        self.actionSpeichern.setObjectName(u"actionSpeichern")
        self.actionSpeichern_unter = QAction(gui_main)
        self.actionSpeichern_unter.setObjectName(u"actionSpeichern_unter")
        self.actionL_schen = QAction(gui_main)
        self.actionL_schen.setObjectName(u"actionL_schen")
        self.centralwidget = QWidget(gui_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_temp = QLabel(self.centralwidget)
        self.lb_temp.setObjectName(u"lb_temp")
        self.lb_temp.setGeometry(QRect(0, 20, 281, 81))
        font1 = QFont()
        font1.setFamilies([u"Cantarell"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.lb_temp.setFont(font1)
        self.lb_temp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_humidity = QLabel(self.centralwidget)
        self.lb_humidity.setObjectName(u"lb_humidity")
        self.lb_humidity.setGeometry(QRect(0, 130, 321, 121))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        self.lb_humidity.setFont(font2)
        self.lb_level = QLabel(self.centralwidget)
        self.lb_level.setObjectName(u"lb_level")
        self.lb_level.setGeometry(QRect(0, 290, 291, 71))
        self.lb_level.setFont(font2)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 410, 361, 101))
        self.label.setFont(font2)
        self.bt_refresh = QPushButton(self.centralwidget)
        self.bt_refresh.setObjectName(u"bt_refresh")
        self.bt_refresh.setGeometry(QRect(200, 590, 171, 61))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(False)
        self.bt_refresh.setFont(font3)
        self.bt_seed = QPushButton(self.centralwidget)
        self.bt_seed.setObjectName(u"bt_seed")
        self.bt_seed.setGeometry(QRect(480, 590, 211, 61))
        self.bt_seed.setFont(font3)
        self.bt_harvest = QPushButton(self.centralwidget)
        self.bt_harvest.setObjectName(u"bt_harvest")
        self.bt_harvest.setGeometry(QRect(800, 590, 181, 61))
        self.bt_harvest.setFont(font3)
        gui_main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(gui_main)
        self.statusbar.setObjectName(u"statusbar")
        gui_main.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(gui_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 29))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(False)
        self.menubar.setFont(font4)
        self.menuSkyfarms_Informationsinterface = QMenu(self.menubar)
        self.menuSkyfarms_Informationsinterface.setObjectName(u"menuSkyfarms_Informationsinterface")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        gui_main.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuSkyfarms_Informationsinterface.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSkyfarms_Informationsinterface.addAction(self.actionEinstellungen)
        self.menuHelp.addAction(self.actionDokumentation)
        self.menuHelp.addAction(self.actionHilfe)
        self.menuHelp.addAction(self.action)
        self.menuDatei.addAction(self.action_ffnen)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDatei.addAction(self.actionSpeichern_unter)
        self.menuDatei.addAction(self.actionL_schen)

        self.retranslateUi(gui_main)

        QMetaObject.connectSlotsByName(gui_main)
    # setupUi

    def retranslateUi(self, gui_main):
        gui_main.setWindowTitle(QCoreApplication.translate("gui_main", u"MainWindow", None))
        self.actionDokumentation.setText(QCoreApplication.translate("gui_main", u"Dokumentation", None))
        self.actionHilfe.setText(QCoreApplication.translate("gui_main", u"Hilfe", None))
        self.action.setText(QCoreApplication.translate("gui_main", u"?", None))
        self.actionEinstellungen.setText(QCoreApplication.translate("gui_main", u"Einstellungen", None))
        self.action_ffnen.setText(QCoreApplication.translate("gui_main", u"\u00d6ffnen", None))
        self.actionSpeichern.setText(QCoreApplication.translate("gui_main", u"Speichern", None))
        self.actionSpeichern_unter.setText(QCoreApplication.translate("gui_main", u"Speichern unter", None))
        self.actionL_schen.setText(QCoreApplication.translate("gui_main", u"L\u00f6schen", None))
        self.lb_temp.setText(QCoreApplication.translate("gui_main", u"Temperatur:", None))
        self.lb_humidity.setText(QCoreApplication.translate("gui_main", u"Luftfeuchtigkeit:", None))
        self.lb_level.setText(QCoreApplication.translate("gui_main", u"Wasserstand:", None))
        self.label.setText(QCoreApplication.translate("gui_main", u"Verstrichene Zeit:", None))
        self.bt_refresh.setText(QCoreApplication.translate("gui_main", u"Aktualisieren", None))
        self.bt_seed.setText(QCoreApplication.translate("gui_main", u"Neue Aussaat", None))
        self.bt_harvest.setText(QCoreApplication.translate("gui_main", u"Geerntet", None))
        self.menuSkyfarms_Informationsinterface.setTitle(QCoreApplication.translate("gui_main", u"Optionen", None))
        self.menuHelp.setTitle(QCoreApplication.translate("gui_main", u"Extras", None))
        self.menuDatei.setTitle(QCoreApplication.translate("gui_main", u"Datei", None))
    # retranslateUi

