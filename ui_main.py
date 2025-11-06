# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionSuratMasuk = QAction(Main)
        self.actionSuratMasuk.setObjectName(u"actionSuratMasuk")
        self.actionSuratKeluar = QAction(Main)
        self.actionSuratKeluar.setObjectName(u"actionSuratKeluar")
        self.actionDisposisi = QAction(Main)
        self.actionDisposisi.setObjectName(u"actionDisposisi")
        self.actionInstansi = QAction(Main)
        self.actionInstansi.setObjectName(u"actionInstansi")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionSuratMasuk)
        self.menuMenu.addAction(self.actionSuratKeluar)
        self.menuMenu.addAction(self.actionDisposisi)
        self.menuMenu.addAction(self.actionInstansi)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionSuratMasuk.setText(QCoreApplication.translate("Main", u"Surat Masuk", None))
        self.actionSuratKeluar.setText(QCoreApplication.translate("Main", u"Surat Keluar", None))
        self.actionDisposisi.setText(QCoreApplication.translate("Main", u"Disposisi", None))
        self.actionInstansi.setText(QCoreApplication.translate("Main", u"Pengaturan Instansi", None))
        self.menuMenu.setTitle(QCoreApplication.translate("Main", u"Menu", None))
    # retranslateUi

