# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SuratKeluar.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_pageSuratKeluar(object):
    def setupUi(self, pageSuratKeluar):
        if not pageSuratKeluar.objectName():
            pageSuratKeluar.setObjectName(u"pageSuratKeluar")
        pageSuratKeluar.resize(779, 490)
        self.label = QLabel(pageSuratKeluar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 10, 191, 31))
        self.formLayoutWidget = QWidget(pageSuratKeluar)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 50, 321, 411))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLabel = QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName(u"iDLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.noAgendaLabel = QLabel(self.formLayoutWidget)
        self.noAgendaLabel.setObjectName(u"noAgendaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.noAgendaLabel)

        self.editNoAgenda = QLineEdit(self.formLayoutWidget)
        self.editNoAgenda.setObjectName(u"editNoAgenda")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNoAgenda)

        self.tujuanLabel = QLabel(self.formLayoutWidget)
        self.tujuanLabel.setObjectName(u"tujuanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tujuanLabel)

        self.editTujuan = QLineEdit(self.formLayoutWidget)
        self.editTujuan.setObjectName(u"editTujuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editTujuan)

        self.noSuratLabel = QLabel(self.formLayoutWidget)
        self.noSuratLabel.setObjectName(u"noSuratLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.noSuratLabel)

        self.editNoSurat = QLineEdit(self.formLayoutWidget)
        self.editNoSurat.setObjectName(u"editNoSurat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editNoSurat)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.cmbKode = QComboBox(self.formLayoutWidget)
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.setObjectName(u"cmbKode")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbKode)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.dateTanggalSurat = QDateEdit(self.formLayoutWidget)
        self.dateTanggalSurat.setObjectName(u"dateTanggalSurat")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.dateTanggalSurat)

        self.fileLabel = QLabel(self.formLayoutWidget)
        self.fileLabel.setObjectName(u"fileLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.fileLabel)

        self.editFile = QLineEdit(self.formLayoutWidget)
        self.editFile.setObjectName(u"editFile")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editFile)

        self.cmbIdUser = QComboBox(self.formLayoutWidget)
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.addItem("")
        self.cmbIdUser.setObjectName(u"cmbIdUser")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cmbIdUser)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.txtIsi = QTextEdit(self.formLayoutWidget)
        self.txtIsi.setObjectName(u"txtIsi")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.txtIsi)

        self.txtKeterangan = QTextEdit(self.formLayoutWidget)
        self.txtKeterangan.setObjectName(u"txtKeterangan")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.txtKeterangan)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.tblSuratKeluar = QTableWidget(pageSuratKeluar)
        self.tblSuratKeluar.setObjectName(u"tblSuratKeluar")
        self.tblSuratKeluar.setGeometry(QRect(360, 50, 391, 331))
        self.btnCreate = QPushButton(pageSuratKeluar)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setGeometry(QRect(360, 430, 82, 31))
        self.btnUpdate = QPushButton(pageSuratKeluar)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(460, 430, 82, 31))
        self.btnDelete = QPushButton(pageSuratKeluar)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(570, 430, 82, 31))
        self.btnClear = QPushButton(pageSuratKeluar)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(670, 430, 82, 31))

        self.retranslateUi(pageSuratKeluar)

        QMetaObject.connectSlotsByName(pageSuratKeluar)
    # setupUi

    def retranslateUi(self, pageSuratKeluar):
        pageSuratKeluar.setWindowTitle(QCoreApplication.translate("pageSuratKeluar", u"Form", None))
        self.label.setText(QCoreApplication.translate("pageSuratKeluar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">SURAT KELUAR</span></p></body></html>", None))
        self.iDLabel.setText(QCoreApplication.translate("pageSuratKeluar", u"ID", None))
        self.noAgendaLabel.setText(QCoreApplication.translate("pageSuratKeluar", u"No Agenda", None))
        self.tujuanLabel.setText(QCoreApplication.translate("pageSuratKeluar", u"Tujuan", None))
        self.noSuratLabel.setText(QCoreApplication.translate("pageSuratKeluar", u"No Surat", None))
        self.label_2.setText(QCoreApplication.translate("pageSuratKeluar", u"Kode", None))
        self.cmbKode.setItemText(0, QCoreApplication.translate("pageSuratKeluar", u"K-01 - Keuangan", None))
        self.cmbKode.setItemText(1, QCoreApplication.translate("pageSuratKeluar", u"P-02 - Personalia", None))
        self.cmbKode.setItemText(2, QCoreApplication.translate("pageSuratKeluar", u"M-03 - Marketing", None))
        self.cmbKode.setItemText(3, QCoreApplication.translate("pageSuratKeluar", u"U-04 - Umum", None))
        self.cmbKode.setItemText(4, QCoreApplication.translate("pageSuratKeluar", u"L-05 - Lain-lain", None))

        self.label_3.setText(QCoreApplication.translate("pageSuratKeluar", u"Tanggal Surat", None))
        self.fileLabel.setText(QCoreApplication.translate("pageSuratKeluar", u"File", None))
        self.cmbIdUser.setItemText(0, QCoreApplication.translate("pageSuratKeluar", u"1", None))
        self.cmbIdUser.setItemText(1, QCoreApplication.translate("pageSuratKeluar", u"2", None))
        self.cmbIdUser.setItemText(2, QCoreApplication.translate("pageSuratKeluar", u"3", None))
        self.cmbIdUser.setItemText(3, QCoreApplication.translate("pageSuratKeluar", u"4", None))
        self.cmbIdUser.setItemText(4, QCoreApplication.translate("pageSuratKeluar", u"5", None))
        self.cmbIdUser.setItemText(5, QCoreApplication.translate("pageSuratKeluar", u"6", None))
        self.cmbIdUser.setItemText(6, QCoreApplication.translate("pageSuratKeluar", u"7", None))
        self.cmbIdUser.setItemText(7, QCoreApplication.translate("pageSuratKeluar", u"8", None))

        self.label_4.setText(QCoreApplication.translate("pageSuratKeluar", u"ID User", None))
        self.label_5.setText(QCoreApplication.translate("pageSuratKeluar", u"Isi", None))
        self.label_6.setText(QCoreApplication.translate("pageSuratKeluar", u"Keterangan", None))
        self.btnCreate.setText(QCoreApplication.translate("pageSuratKeluar", u"Create", None))
        self.btnUpdate.setText(QCoreApplication.translate("pageSuratKeluar", u"Update", None))
        self.btnDelete.setText(QCoreApplication.translate("pageSuratKeluar", u"Delete", None))
        self.btnClear.setText(QCoreApplication.translate("pageSuratKeluar", u"Clear", None))
    # retranslateUi

