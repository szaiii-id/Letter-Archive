# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Instansi.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_pageInstansi(object):
    def setupUi(self, pageInstansi):
        if not pageInstansi.objectName():
            pageInstansi.setObjectName(u"pageInstansi")
        pageInstansi.resize(772, 408)
        self.label = QLabel(pageInstansi)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 231, 31))
        self.formLayoutWidget = QWidget(pageInstansi)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 60, 311, 311))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLabel = QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName(u"iDLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaInstansiLabel = QLabel(self.formLayoutWidget)
        self.namaInstansiLabel.setObjectName(u"namaInstansiLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaInstansiLabel)

        self.editNamaInstansi = QLineEdit(self.formLayoutWidget)
        self.editNamaInstansi.setObjectName(u"editNamaInstansi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNamaInstansi)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.editEmail = QLineEdit(self.formLayoutWidget)
        self.editEmail.setObjectName(u"editEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editEmail)

        self.teleponLabel = QLabel(self.formLayoutWidget)
        self.teleponLabel.setObjectName(u"teleponLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.teleponLabel)

        self.editTelp = QLineEdit(self.formLayoutWidget)
        self.editTelp.setObjectName(u"editTelp")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTelp)

        self.websiteLabel = QLabel(self.formLayoutWidget)
        self.websiteLabel.setObjectName(u"websiteLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.websiteLabel)

        self.editWebsite = QLineEdit(self.formLayoutWidget)
        self.editWebsite.setObjectName(u"editWebsite")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editWebsite)

        self.logoLabel = QLabel(self.formLayoutWidget)
        self.logoLabel.setObjectName(u"logoLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.logoLabel)

        self.editLogo = QLineEdit(self.formLayoutWidget)
        self.editLogo.setObjectName(u"editLogo")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editLogo)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.txtAlamat = QTextEdit(self.formLayoutWidget)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.tblInstansi = QTableWidget(pageInstansi)
        self.tblInstansi.setObjectName(u"tblInstansi")
        self.tblInstansi.setGeometry(QRect(350, 60, 391, 251))
        self.btnCreate = QPushButton(pageInstansi)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setGeometry(QRect(350, 350, 82, 24))
        self.btnUpdate = QPushButton(pageInstansi)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(450, 350, 82, 24))
        self.btnDelete = QPushButton(pageInstansi)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(560, 350, 82, 24))
        self.btnClear = QPushButton(pageInstansi)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(660, 350, 82, 24))

        self.retranslateUi(pageInstansi)

        QMetaObject.connectSlotsByName(pageInstansi)
    # setupUi

    def retranslateUi(self, pageInstansi):
        pageInstansi.setWindowTitle(QCoreApplication.translate("pageInstansi", u"Form", None))
        self.label.setText(QCoreApplication.translate("pageInstansi", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">PENGATURAN INSTANSI</span></p></body></html>", None))
        self.iDLabel.setText(QCoreApplication.translate("pageInstansi", u"ID", None))
        self.namaInstansiLabel.setText(QCoreApplication.translate("pageInstansi", u"Nama Instansi", None))
        self.emailLabel.setText(QCoreApplication.translate("pageInstansi", u"Email", None))
        self.teleponLabel.setText(QCoreApplication.translate("pageInstansi", u"Telepon", None))
        self.websiteLabel.setText(QCoreApplication.translate("pageInstansi", u"Website", None))
        self.logoLabel.setText(QCoreApplication.translate("pageInstansi", u"Logo", None))
        self.label_2.setText(QCoreApplication.translate("pageInstansi", u"Alamat", None))
        self.btnCreate.setText(QCoreApplication.translate("pageInstansi", u"Create", None))
        self.btnUpdate.setText(QCoreApplication.translate("pageInstansi", u"Update", None))
        self.btnDelete.setText(QCoreApplication.translate("pageInstansi", u"Delete", None))
        self.btnClear.setText(QCoreApplication.translate("pageInstansi", u"Clear", None))
    # retranslateUi

