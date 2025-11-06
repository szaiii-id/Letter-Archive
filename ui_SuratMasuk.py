# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SuratMasuk.ui'
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

class Ui_pageSuratMasuk(object):
    def setupUi(self, pageSuratMasuk):
        if not pageSuratMasuk.objectName():
            pageSuratMasuk.setObjectName(u"pageSuratMasuk")
        pageSuratMasuk.resize(829, 528)
        self.label = QLabel(pageSuratMasuk)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 10, 151, 21))
        self.formLayoutWidget = QWidget(pageSuratMasuk)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 60, 311, 450))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLabel = QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName(u"iDLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLabel)

        self.editId = QLineEdit(self.formLayoutWidget)
        self.editId.setObjectName(u"editId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editId)

        self.noAgendaLabel = QLabel(self.formLayoutWidget)
        self.noAgendaLabel.setObjectName(u"noAgendaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.noAgendaLabel)

        self.editNoAgenda = QLineEdit(self.formLayoutWidget)
        self.editNoAgenda.setObjectName(u"editNoAgenda")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNoAgenda)

        self.asalSuratLabel = QLabel(self.formLayoutWidget)
        self.asalSuratLabel.setObjectName(u"asalSuratLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.asalSuratLabel)

        self.editAsalSurat = QLineEdit(self.formLayoutWidget)
        self.editAsalSurat.setObjectName(u"editAsalSurat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editAsalSurat)

        self.noSuratLabel = QLabel(self.formLayoutWidget)
        self.noSuratLabel.setObjectName(u"noSuratLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.noSuratLabel)

        self.editNoSurat = QLineEdit(self.formLayoutWidget)
        self.editNoSurat.setObjectName(u"editNoSurat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editNoSurat)

        self.kodeLabel = QLabel(self.formLayoutWidget)
        self.kodeLabel.setObjectName(u"kodeLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.kodeLabel)

        self.cmbKode = QComboBox(self.formLayoutWidget)
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.addItem("")
        self.cmbKode.setObjectName(u"cmbKode")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbKode)

        self.indexLabel = QLabel(self.formLayoutWidget)
        self.indexLabel.setObjectName(u"indexLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.indexLabel)

        self.cmbIndex = QComboBox(self.formLayoutWidget)
        self.cmbIndex.addItem("")
        self.cmbIndex.addItem("")
        self.cmbIndex.addItem("")
        self.cmbIndex.addItem("")
        self.cmbIndex.addItem("")
        self.cmbIndex.addItem("")
        self.cmbIndex.setObjectName(u"cmbIndex")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbIndex)

        self.tanggalSuratLabel = QLabel(self.formLayoutWidget)
        self.tanggalSuratLabel.setObjectName(u"tanggalSuratLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.tanggalSuratLabel)

        self.dateTanggalSurat = QDateEdit(self.formLayoutWidget)
        self.dateTanggalSurat.setObjectName(u"dateTanggalSurat")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.dateTanggalSurat)

        self.tanggalDiterimaLabel = QLabel(self.formLayoutWidget)
        self.tanggalDiterimaLabel.setObjectName(u"tanggalDiterimaLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.tanggalDiterimaLabel)

        self.dateTanggalDiterima = QDateEdit(self.formLayoutWidget)
        self.dateTanggalDiterima.setObjectName(u"dateTanggalDiterima")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.dateTanggalDiterima)

        self.fileLabel = QLabel(self.formLayoutWidget)
        self.fileLabel.setObjectName(u"fileLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.fileLabel)

        self.editFile = QLineEdit(self.formLayoutWidget)
        self.editFile.setObjectName(u"editFile")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.editFile)

        self.iDUserLabel = QLabel(self.formLayoutWidget)
        self.iDUserLabel.setObjectName(u"iDUserLabel")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.iDUserLabel)

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

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.cmbIdUser)

        self.txtIsi = QTextEdit(self.formLayoutWidget)
        self.txtIsi.setObjectName(u"txtIsi")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.txtIsi)

        self.txtKeterangan = QTextEdit(self.formLayoutWidget)
        self.txtKeterangan.setObjectName(u"txtKeterangan")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.txtKeterangan)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.tblSuratMasuk = QTableWidget(pageSuratMasuk)
        self.tblSuratMasuk.setObjectName(u"tblSuratMasuk")
        self.tblSuratMasuk.setGeometry(QRect(370, 60, 431, 381))
        self.btnCreate = QPushButton(pageSuratMasuk)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setGeometry(QRect(371, 490, 81, 24))
        self.btnUpdate = QPushButton(pageSuratMasuk)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(480, 490, 81, 24))
        self.btnDelete = QPushButton(pageSuratMasuk)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(600, 490, 81, 24))
        self.btnClear = QPushButton(pageSuratMasuk)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(720, 490, 81, 24))

        self.retranslateUi(pageSuratMasuk)

        QMetaObject.connectSlotsByName(pageSuratMasuk)
    # setupUi

    def retranslateUi(self, pageSuratMasuk):
        pageSuratMasuk.setWindowTitle(QCoreApplication.translate("pageSuratMasuk", u"Form", None))
        self.label.setText(QCoreApplication.translate("pageSuratMasuk", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">SURAT MASUK</span></p></body></html>", None))
        self.iDLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"ID", None))
        self.noAgendaLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"No Agenda", None))
        self.asalSuratLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"Asal Surat", None))
        self.noSuratLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"No Surat", None))
        self.kodeLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"Kode", None))
        self.cmbKode.setItemText(0, QCoreApplication.translate("pageSuratMasuk", u"K-01 - Keuangan", None))
        self.cmbKode.setItemText(1, QCoreApplication.translate("pageSuratMasuk", u"P-02 - Personalia", None))
        self.cmbKode.setItemText(2, QCoreApplication.translate("pageSuratMasuk", u"M-03 - Marketing", None))
        self.cmbKode.setItemText(3, QCoreApplication.translate("pageSuratMasuk", u"U-04 - Umum", None))
        self.cmbKode.setItemText(4, QCoreApplication.translate("pageSuratMasuk", u"L-05 - Lain-lain", None))

        self.indexLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"Index", None))
        self.cmbIndex.setItemText(0, QCoreApplication.translate("pageSuratMasuk", u"Keuangan", None))
        self.cmbIndex.setItemText(1, QCoreApplication.translate("pageSuratMasuk", u"Kepegawaian", None))
        self.cmbIndex.setItemText(2, QCoreApplication.translate("pageSuratMasuk", u"Pemasaran", None))
        self.cmbIndex.setItemText(3, QCoreApplication.translate("pageSuratMasuk", u"Umum", None))
        self.cmbIndex.setItemText(4, QCoreApplication.translate("pageSuratMasuk", u"Penting", None))
        self.cmbIndex.setItemText(5, QCoreApplication.translate("pageSuratMasuk", u"Rahasia", None))

        self.tanggalSuratLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"Tanggal Surat", None))
        self.tanggalDiterimaLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"Tanggal Diterima", None))
        self.fileLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"File", None))
        self.iDUserLabel.setText(QCoreApplication.translate("pageSuratMasuk", u"ID User", None))
        self.cmbIdUser.setItemText(0, QCoreApplication.translate("pageSuratMasuk", u"1", None))
        self.cmbIdUser.setItemText(1, QCoreApplication.translate("pageSuratMasuk", u"2", None))
        self.cmbIdUser.setItemText(2, QCoreApplication.translate("pageSuratMasuk", u"3", None))
        self.cmbIdUser.setItemText(3, QCoreApplication.translate("pageSuratMasuk", u"4", None))
        self.cmbIdUser.setItemText(4, QCoreApplication.translate("pageSuratMasuk", u"5", None))
        self.cmbIdUser.setItemText(5, QCoreApplication.translate("pageSuratMasuk", u"6", None))
        self.cmbIdUser.setItemText(6, QCoreApplication.translate("pageSuratMasuk", u"7", None))
        self.cmbIdUser.setItemText(7, QCoreApplication.translate("pageSuratMasuk", u"8", None))

        self.label_2.setText(QCoreApplication.translate("pageSuratMasuk", u"Isi", None))
        self.label_3.setText(QCoreApplication.translate("pageSuratMasuk", u"Keterangan", None))
        self.btnCreate.setText(QCoreApplication.translate("pageSuratMasuk", u"Create", None))
        self.btnUpdate.setText(QCoreApplication.translate("pageSuratMasuk", u"Update", None))
        self.btnDelete.setText(QCoreApplication.translate("pageSuratMasuk", u"Delete", None))
        self.btnClear.setText(QCoreApplication.translate("pageSuratMasuk", u"Clear", None))
    # retranslateUi

