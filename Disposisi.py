import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader

from DisposisiRepository import DisposisiRepository

class DisposisiPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Page Disposisi")
        UiFile = QFile("Disposisi.ui")
        UiFile.open(QFile.ReadOnly)

        UiLoader = QUiLoader()
        self.UiMenu = UiLoader.load(UiFile, self)

        self.resize(self.UiMenu.size())

        self.repo = DisposisiRepository()

        self.UiMenu.editID.setReadOnly(True)

        self.UiMenu.btnCreate.clicked.connect(self.btnCreateDisposisi)
        self.UiMenu.btnUpdate.clicked.connect(self.btnUpdateDisposisi)
        self.UiMenu.btnDelete.clicked.connect(self.btnDeleteDisposisi)
        self.UiMenu.btnClear.clicked.connect(self.btnClearDisposisi)

        self.UiMenu.tblDisposisi.cellClicked.connect(self.tableCellClick)

        self.tableView()
        self.readDataDisposisi()

    def tableView(self):
        headers = ["ID", "ID Surat", "Tujuan", "Isi Disposisi", "Sifat", "Batas Waktu", "Catatan", "ID User"]
        table = self.UiMenu.tblDisposisi
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def tableCellClick(self, row, column):

        dataIdDisposisi = self.UiMenu.tblDisposisi.item(row, 0).text()
        dataIdSurat = self.UiMenu.tblDisposisi.item(row, 1).text().strip()
        dataTujuan = self.UiMenu.tblDisposisi.item(row, 2).text()
        dataIsiDisposisi = self.UiMenu.tblDisposisi.item(row, 3).text()
        dataSifat = self.UiMenu.tblDisposisi.item(row, 4).text().strip()
        dataBatasWaktu = self.UiMenu.tblDisposisi.item(row, 5).text()
        dataCatatan = self.UiMenu.tblDisposisi.item(row, 6).text()
        dataIdUser = self.UiMenu.tblDisposisi.item(row, 7).text().strip()

        self.UiMenu.editID.setText(dataIdDisposisi)
        self.UiMenu.editTujuan.setText(dataTujuan)
        self.UiMenu.txtIsi.setText(dataIsiDisposisi)
        self.UiMenu.txtCatatan.setText(dataCatatan)

        indexIdSurat = self.UiMenu.cmbIdSurat.findText(dataIdSurat)
        if indexIdSurat >= 0:
            self.UiMenu.cmbIdSurat.setCurrentIndex(indexIdSurat)

        indexIdUser = self.UiMenu.cmbIdUser.findText(dataIdUser)
        if indexIdUser >= 0:
            self.UiMenu.cmbIdUser.setCurrentIndex(indexIdUser)

        self.UiMenu.dateBatasWaktu.setDate(QDate.fromString(dataBatasWaktu, "yyyy-MM-dd"))


    def readDataDisposisi(self):
        results = self.repo.readDisposisi()

        table = self.UiMenu.tblDisposisi
        table.setRowCount(0)

        if results:
            for row_number, row_data in enumerate(results):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def btnCreateDisposisi(self):
        tempIdSurat = self.UiMenu.cmbIdSurat.currentText()
        tempTujuan = self.UiMenu.editTujuan.text()
        tempIsiDisposisi = self.UiMenu.txtIsi.toPlainText()
        tempCatatan = self.UiMenu.txtCatatan.toPlainText()
        tempIdUser = self.UiMenu.cmbIdUser.currentText()
        tempBatasWaktu = self.UiMenu.dateBatasWaktu.date().toString("yyyy-MM-dd")

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Surat ID cannot be empty.")
            self.UiMenu.cmbIdSurat.setFocus()
            return

        if not tempTujuan:
            QMessageBox.warning(self, "Warning", "Destination cannot be empty.")
            self.UiMenu.editTujuan.setFocus()
            return

        if not tempIsiDisposisi:
            QMessageBox.warning(self, "Warning", "Isi Disposisi cannot be empty.")
            self.UiMenu.txtIsi.setFocus()
            return

        self.repo.createDisposisi(
            tempIdSurat, tempTujuan, tempIsiDisposisi,
            None, tempBatasWaktu, tempCatatan, tempIdUser
        )

        QMessageBox.information(self, "Create Disposition","Disposition Data Created Successfully")

        self.readDataDisposisi()
        self.btnClearDisposisi()

    def btnUpdateDisposisi(self):
        tempIdDisposisi = self.UiMenu.editID.text()
        tempIdSurat = self.UiMenu.cmbIdSurat.currentText()
        tempTujuan = self.UiMenu.editTujuan.text()
        tempIsiDisposisi = self.UiMenu.txtIsi.toPlainText()
        tempCatatan = self.UiMenu.txtCatatan.toPlainText()
        tempIdUser = self.UiMenu.cmbIdUser.currentText()
        tempBatasWaktu = self.UiMenu.dateBatasWaktu.date().toString("yyyy-MM-dd")

        if not tempIdDisposisi:
            QMessageBox.warning(self, "Warning", "Please select data from the table first.")
            return

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Surat ID cannot be empty.")
            self.UiMenu.cmbIdSurat.setFocus()
            return

        if not tempTujuan:
            QMessageBox.warning(self, "Warning", "Destination cannot be empty.")
            self.UiMenu.editTujuan.setFocus()
            return

        if not tempIsiDisposisi:
            QMessageBox.warning(self, "Warning", "Isi Disposisi cannot be empty.")
            self.UiMenu.txtIsi.setFocus()
            return

        btnConfirm = QMessageBox.question(self, "Confirm Update", "Do you want to update this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.updateDisposisi(
                tempIdSurat, tempTujuan, tempIsiDisposisi,
                None, tempBatasWaktu, tempCatatan, tempIdUser,
                tempIdDisposisi
            )
            QMessageBox.information(self, "Update Disposition","Disposition Data Updated Successfully")
            self.readDataDisposisi()
            self.btnClearDisposisi()
        else :
            QMessageBox.information(self, "Update Disposition","Failed to Update Disposition Data")

    def btnDeleteDisposisi(self):
        tempIdDisposisi = self.UiMenu.editID.text()

        if not tempIdDisposisi:
            QMessageBox.warning(self, "Warning", "Please select data from the table to delete.")
            return

        btnConfirm = QMessageBox.question(self, "Confirm Delete", "Do you want to delete this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.deleteDisposisi(tempIdDisposisi)
            QMessageBox.information(self, "Delete Disposition","Disposition Data Deleted Successfully")
            self.readDataDisposisi()
            self.btnClearDisposisi()
        else :
            QMessageBox.information(self, "Delete Disposition","Failed to Delete Disposition Data")

    def btnClearDisposisi(self):
        self.UiMenu.editID.clear()
        self.UiMenu.cmbIdSurat.setCurrentIndex(0)
        self.UiMenu.editTujuan.clear()
        self.UiMenu.txtIsi.clear()
        self.UiMenu.txtCatatan.clear()
        self.UiMenu.cmbIdUser.setCurrentIndex(0)
        self.UiMenu.dateBatasWaktu.setDate(QDate.currentDate())
