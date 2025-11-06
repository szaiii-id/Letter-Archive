# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Disposisi.ui'
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

class Ui_pageDisposisi(object):
    def setupUi(self, pageDisposisi):
        if not pageDisposisi.objectName():
            pageDisposisi.setObjectName(u"pageDisposisi")
        pageDisposisi.resize(768, 413)
        self.label = QLabel(pageDisposisi)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 10, 141, 31))
        self.formLayoutWidget = QWidget(pageDisposisi)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 60, 311, 321))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLabel = QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName(u"iDLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.tujuanLabel = QLabel(self.formLayoutWidget)
        self.tujuanLabel.setObjectName(u"tujuanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tujuanLabel)

        self.editTujuan = QLineEdit(self.formLayoutWidget)
        self.editTujuan.setObjectName(u"editTujuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editTujuan)

        self.iDSuratLabel = QLabel(self.formLayoutWidget)
        self.iDSuratLabel.setObjectName(u"iDSuratLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.iDSuratLabel)

        self.cmbIdSurat = QComboBox(self.formLayoutWidget)
        self.cmbIdSurat.addItem("")
        self.cmbIdSurat.addItem("")
        self.cmbIdSurat.addItem("")
        self.cmbIdSurat.addItem("")
        self.cmbIdSurat.addItem("")
        self.cmbIdSurat.addItem("")
        self.cmbIdSurat.setObjectName(u"cmbIdSurat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbIdSurat)

        self.batasWaktuLabel = QLabel(self.formLayoutWidget)
        self.batasWaktuLabel.setObjectName(u"batasWaktuLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.batasWaktuLabel)

        self.dateBatasWaktu = QDateEdit(self.formLayoutWidget)
        self.dateBatasWaktu.setObjectName(u"dateBatasWaktu")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateBatasWaktu)

        self.iDUserLabel = QLabel(self.formLayoutWidget)
        self.iDUserLabel.setObjectName(u"iDUserLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDUserLabel)

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

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbIdUser)

        self.txtIsi = QTextEdit(self.formLayoutWidget)
        self.txtIsi.setObjectName(u"txtIsi")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtIsi)

        self.txtCatatan = QTextEdit(self.formLayoutWidget)
        self.txtCatatan.setObjectName(u"txtCatatan")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txtCatatan)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.tblDisposisi = QTableWidget(pageDisposisi)
        self.tblDisposisi.setObjectName(u"tblDisposisi")
        self.tblDisposisi.setGeometry(QRect(360, 60, 391, 261))
        self.btnCreate = QPushButton(pageDisposisi)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setGeometry(QRect(360, 360, 82, 24))
        self.btnUpdate = QPushButton(pageDisposisi)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(460, 360, 82, 24))
        self.btnDelete = QPushButton(pageDisposisi)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(570, 360, 82, 24))
        self.btnClear = QPushButton(pageDisposisi)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(670, 360, 82, 24))

        self.retranslateUi(pageDisposisi)

        QMetaObject.connectSlotsByName(pageDisposisi)
    # setupUi

    def retranslateUi(self, pageDisposisi):
        pageDisposisi.setWindowTitle(QCoreApplication.translate("pageDisposisi", u"Form", None))
        self.label.setText(QCoreApplication.translate("pageDisposisi", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">DISPOSISI</span></p></body></html>", None))
        self.iDLabel.setText(QCoreApplication.translate("pageDisposisi", u"ID", None))
        self.tujuanLabel.setText(QCoreApplication.translate("pageDisposisi", u"Tujuan", None))
        self.iDSuratLabel.setText(QCoreApplication.translate("pageDisposisi", u"ID Surat", None))
        self.cmbIdSurat.setItemText(0, QCoreApplication.translate("pageDisposisi", u"1", None))
        self.cmbIdSurat.setItemText(1, QCoreApplication.translate("pageDisposisi", u"2", None))
        self.cmbIdSurat.setItemText(2, QCoreApplication.translate("pageDisposisi", u"3", None))
        self.cmbIdSurat.setItemText(3, QCoreApplication.translate("pageDisposisi", u"4", None))
        self.cmbIdSurat.setItemText(4, QCoreApplication.translate("pageDisposisi", u"5", None))
        self.cmbIdSurat.setItemText(5, QCoreApplication.translate("pageDisposisi", u"6", None))

        self.batasWaktuLabel.setText(QCoreApplication.translate("pageDisposisi", u"Batas Waktu", None))
        self.iDUserLabel.setText(QCoreApplication.translate("pageDisposisi", u"ID User", None))
        self.cmbIdUser.setItemText(0, QCoreApplication.translate("pageDisposisi", u"1", None))
        self.cmbIdUser.setItemText(1, QCoreApplication.translate("pageDisposisi", u"2", None))
        self.cmbIdUser.setItemText(2, QCoreApplication.translate("pageDisposisi", u"3", None))
        self.cmbIdUser.setItemText(3, QCoreApplication.translate("pageDisposisi", u"4", None))
        self.cmbIdUser.setItemText(4, QCoreApplication.translate("pageDisposisi", u"5", None))
        self.cmbIdUser.setItemText(5, QCoreApplication.translate("pageDisposisi", u"6", None))
        self.cmbIdUser.setItemText(6, QCoreApplication.translate("pageDisposisi", u"7", None))
        self.cmbIdUser.setItemText(7, QCoreApplication.translate("pageDisposisi", u"8", None))

        self.label_2.setText(QCoreApplication.translate("pageDisposisi", u"Isi", None))
        self.label_3.setText(QCoreApplication.translate("pageDisposisi", u"Catatan", None))
        self.btnCreate.setText(QCoreApplication.translate("pageDisposisi", u"Create", None))
        self.btnUpdate.setText(QCoreApplication.translate("pageDisposisi", u"Update", None))
        self.btnDelete.setText(QCoreApplication.translate("pageDisposisi", u"Delete", None))
        self.btnClear.setText(QCoreApplication.translate("pageDisposisi", u"Clear", None))
    # retranslateUi

