import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader

from SuratMasukRepository import SuratMasukRepository

class SuratMasukPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Page Surat Masuk")
        UiFile = QFile("SuratMasuk.ui")
        UiFile.open(QFile.ReadOnly)

        UiLoader = QUiLoader()
        self.UiMenu = UiLoader.load(UiFile, self)

        self.resize(self.UiMenu.size())

        self.repo = SuratMasukRepository()

        self.UiMenu.btnCreate.clicked.connect(self.btnCreateSuratMasuk)
        self.UiMenu.btnUpdate.clicked.connect(self.btnUpdateSuratMasuk)
        self.UiMenu.btnDelete.clicked.connect(self.btnDeleteSuratMasuk)
        self.UiMenu.btnClear.clicked.connect(self.btnClearSuratMasuk)

        self.UiMenu.tblSuratMasuk.cellClicked.connect(self.tableCellClick)

        self.tableView()
        self.readDataSuratMasuk()

    def tableView(self):
        headers = ["ID", "No Agenda", "Asal Surat", "No Surat", "Isi",
                   "Kode", "Indeks", "Tgl Surat", "Tgl Diterima", "File",
                   "Keterangan", "ID User"]
        table = self.UiMenu.tblSuratMasuk
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def tableCellClick(self, row, column):

        dataIdSurat = self.UiMenu.tblSuratMasuk.item(row, 0).text()
        dataNoAgenda = self.UiMenu.tblSuratMasuk.item(row, 1).text()
        dataAsalSurat = self.UiMenu.tblSuratMasuk.item(row, 2).text()
        dataNoSurat = self.UiMenu.tblSuratMasuk.item(row, 3).text()
        dataIsi = self.UiMenu.tblSuratMasuk.item(row, 4).text()
        dataKode = self.UiMenu.tblSuratMasuk.item(row, 5).text().strip()
        dataIndeks = self.UiMenu.tblSuratMasuk.item(row, 6).text().strip()
        dataTglSurat = self.UiMenu.tblSuratMasuk.item(row, 7).text()
        dataTglDiterima = self.UiMenu.tblSuratMasuk.item(row, 8).text()
        dataFile = self.UiMenu.tblSuratMasuk.item(row, 9).text()
        dataKeterangan = self.UiMenu.tblSuratMasuk.item(row, 10).text()
        dataIdUser = self.UiMenu.tblSuratMasuk.item(row, 11).text().strip()

        self.UiMenu.editId.setText(dataIdSurat)
        self.UiMenu.editNoAgenda.setText(dataNoAgenda)
        self.UiMenu.editAsalSurat.setText(dataAsalSurat)
        self.UiMenu.editNoSurat.setText(dataNoSurat)
        self.UiMenu.editFile.setText(dataFile)

        self.UiMenu.txtIsi.setText(dataIsi)
        self.UiMenu.txtKeterangan.setText(dataKeterangan)

        indexKode = self.UiMenu.cmbKode.findText(dataKode)
        if indexKode >= 0:
            self.UiMenu.cmbKode.setCurrentIndex(indexKode)

        indexIndeks = self.UiMenu.cmbIndex.findText(dataIndeks)
        if indexIndeks >= 0:
            self.UiMenu.cmbIndex.setCurrentIndex(indexIndeks)

        indexIdUser = self.UiMenu.cmbIdUser.findText(dataIdUser)
        if indexIdUser >= 0:
            self.UiMenu.cmbIdUser.setCurrentIndex(indexIdUser)

        self.UiMenu.dateTanggalSurat.setDate(QDate.fromString(dataTglSurat, "yyyy-MM-dd"))
        self.UiMenu.dateTanggalDiterima.setDate(QDate.fromString(dataTglDiterima, "yyyy-MM-dd"))


    def readDataSuratMasuk(self):
        results = self.repo.readSuratMasuk()

        table = self.UiMenu.tblSuratMasuk
        table.setRowCount(0)

        if results:
            for row_number, row_data in enumerate(results):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def btnCreateSuratMasuk(self):
        tempIdSurat = self.UiMenu.editId.text()
        tempNoAgenda = self.UiMenu.editNoAgenda.text()
        tempAsalSurat = self.UiMenu.editAsalSurat.text()
        tempNoSurat = self.UiMenu.editNoSurat.text()
        tempIsi = self.UiMenu.txtIsi.toPlainText()

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Surat ID cannot be empty.")
            self.UiMenu.editId.setFocus()
            return

        if not tempNoAgenda:
            QMessageBox.warning(self, "Warning", "No Agenda cannot be empty.")
            self.UiMenu.editNoAgenda.setFocus()
            return

        if not tempAsalSurat:
            QMessageBox.warning(self, "Warning", "Asal Surat cannot be empty.")
            self.UiMenu.editAsalSurat.setFocus()
            return

        if not tempNoSurat:
            QMessageBox.warning(self, "Warning", "No Surat cannot be empty.")
            self.UiMenu.editNoSurat.setFocus()
            return

        if not tempIsi:
            QMessageBox.warning(self, "Warning", "Isi cannot be empty.")
            self.UiMenu.txtIsi.setFocus()
            return

        tempFile = self.UiMenu.editFile.text()
        tempKeterangan = self.UiMenu.txtKeterangan.toPlainText()
        tempKode = self.UiMenu.cmbKode.currentText()
        tempIndeks = self.UiMenu.cmbIndex.currentText()
        tempIdUser = self.UiMenu.cmbIdUser.currentText()
        tempTglSurat = self.UiMenu.dateTanggalSurat.date().toString("yyyy-MM-dd")
        tempTglDiterima = self.UiMenu.dateTanggalDiterima.date().toString("yyyy-MM-dd")

        self.repo.createSuratMasuk(
            tempIdSurat, tempNoAgenda, tempAsalSurat, tempNoSurat, tempIsi,
            tempKode, tempIndeks, tempTglSurat, tempTglDiterima, tempFile,
            tempKeterangan, tempIdUser
        )

        QMessageBox.information(self, "Create Data","Data Created Successfully")

        self.readDataSuratMasuk()
        self.btnClearField()

    def btnUpdateSuratMasuk(self):
        tempIdSurat = self.UiMenu.editId.text()
        tempNoAgenda = self.UiMenu.editNoAgenda.text()
        tempAsalSurat = self.UiMenu.editAsalSurat.text()
        tempNoSurat = self.UiMenu.editNoSurat.text()
        tempIsi = self.UiMenu.txtIsi.toPlainText()

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Surat ID cannot be empty.")
            self.UiMenu.editId.setFocus()
            return

        if not tempNoAgenda:
            QMessageBox.warning(self, "Warning", "No Agenda cannot be empty.")
            self.UiMenu.editNoAgenda.setFocus()
            return

        if not tempAsalSurat:
            QMessageBox.warning(self, "Warning", "Asal Surat cannot be empty.")
            self.UiMenu.editAsalSurat.setFocus()
            return

        if not tempNoSurat:
            QMessageBox.warning(self, "Warning", "No Surat cannot be empty.")
            self.UiMenu.editNoSurat.setFocus()
            return

        if not tempIsi:
            QMessageBox.warning(self, "Warning", "Isi cannot be empty.")
            self.UiMenu.txtIsi.setFocus()
            return

        tempFile = self.UiMenu.editFile.text()
        tempKeterangan = self.UiMenu.txtKeterangan.toPlainText()
        tempKode = self.UiMenu.cmbKode.currentText()
        tempIndeks = self.UiMenu.cmbIndex.currentText()
        tempIdUser = self.UiMenu.cmbIdUser.currentText()
        tempTglSurat = self.UiMenu.dateTanggalSurat.date().toString("yyyy-MM-dd")
        tempTglDiterima = self.UiMenu.dateTanggalDiterima.date().toString("yyyy-MM-dd")

        btnConfirm = QMessageBox.question(self, "Confirm Update", "Do you want to update this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.updateSuratMasuk(
                tempNoAgenda, tempAsalSurat, tempNoSurat, tempIsi,
                tempKode, tempIndeks, tempTglSurat, tempTglDiterima, tempFile,
                tempKeterangan, tempIdUser,
                tempIdSurat
            )
            QMessageBox.information(self, "Update Data","Data Updated Successfully")
            self.readDataSuratMasuk()
            self.btnClearField()
        else :
            QMessageBox.information(self, "Update Data","Failed to Update Data")

    def btnDeleteSuratMasuk(self):
        tempIdSurat = self.UiMenu.editId.text()

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Please select data from the table to delete.")
            return

        btnConfirm = QMessageBox.question(self, "Confirm Delete", "Do you want to delete this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.deleteSuratMasuk(tempIdSurat)
            QMessageBox.information(self, "Delete Data","Data Deleted Successfully")
            self.readDataSuratMasuk()
            self.btnClearField()
        else :
            QMessageBox.information(self, "Delete Data","Failed to Delete Data")

    def btnClearSuratMasuk(self):
        self.UiMenu.editId.clear()
        self.UiMenu.editNoAgenda.clear()
        self.UiMenu.editAsalSurat.clear()
        self.UiMenu.editNoSurat.clear()
        self.UiMenu.editFile.clear()

        self.UiMenu.txtIsi.clear()
        self.UiMenu.txtKeterangan.clear()

        self.UiMenu.cmbKode.setCurrentIndex(0)
        self.UiMenu.cmbIndex.setCurrentIndex(0)
        self.UiMenu.cmbIdUser.setCurrentIndex(0)

        self.UiMenu.dateTanggalSurat.setDate(QDate.currentDate())
        self.UiMenu.dateTanggalDiterima.setDate(QDate.currentDate())
