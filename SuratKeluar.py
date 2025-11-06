import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader

from SuratKeluarRepository import SuratKeluarRepository

class SuratKeluarPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Page Surat Keluar")
        UiFile = QFile("SuratKeluar.ui")
        UiFile.open(QFile.ReadOnly)

        UiLoader = QUiLoader()
        self.UiMenu = UiLoader.load(UiFile, self)

        self.resize(self.UiMenu.size())

        self.repo = SuratKeluarRepository()

        self.UiMenu.btnCreate.clicked.connect(self.btnCreateSuratKeluar)
        self.UiMenu.btnUpdate.clicked.connect(self.btnUpdateSuratKeluar)
        self.UiMenu.btnDelete.clicked.connect(self.btnDeleteSuratKeluar)
        self.UiMenu.btnClear.clicked.connect(self.btnClearSuratKeluar)

        self.UiMenu.tblSuratKeluar.cellClicked.connect(self.tableCellClick)

        self.tableView()
        self.readDataSuratKeluar()

    def tableView(self):
        headers = ["ID", "No Agenda", "Tujuan", "No Surat", "Isi",
                   "Kode", "Tgl Surat", "File", "Keterangan", "ID User"]
        table = self.UiMenu.tblSuratKeluar
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def tableCellClick(self, row, column):

        dataIdSurat = self.UiMenu.tblSuratKeluar.item(row, 0).text()
        dataNoAgenda = self.UiMenu.tblSuratKeluar.item(row, 1).text()
        dataTujuan = self.UiMenu.tblSuratKeluar.item(row, 2).text()
        dataNoSurat = self.UiMenu.tblSuratKeluar.item(row, 3).text()
        dataIsi = self.UiMenu.tblSuratKeluar.item(row, 4).text()
        dataKode = self.UiMenu.tblSuratKeluar.item(row, 5).text().strip()
        dataTglSurat = self.UiMenu.tblSuratKeluar.item(row, 6).text()
        dataFile = self.UiMenu.tblSuratKeluar.item(row, 7).text()
        dataKeterangan = self.UiMenu.tblSuratKeluar.item(row, 8).text()
        dataIdUser = self.UiMenu.tblSuratKeluar.item(row, 9).text().strip()

        self.UiMenu.editID.setText(dataIdSurat)
        self.UiMenu.editNoAgenda.setText(dataNoAgenda)
        self.UiMenu.editTujuan.setText(dataTujuan)
        self.UiMenu.editNoSurat.setText(dataNoSurat)
        self.UiMenu.txtIsi.setText(dataIsi)
        self.UiMenu.editFile.setText(dataFile)
        self.UiMenu.txtKeterangan.setText(dataKeterangan)

        indexKode = self.UiMenu.cmbKode.findText(dataKode)
        if indexKode >= 0:
            self.UiMenu.cmbKode.setCurrentIndex(indexKode)

        indexIdUser = self.UiMenu.cmbIdUser.findText(dataIdUser)
        if indexIdUser >= 0:
            self.UiMenu.cmbIdUser.setCurrentIndex(indexIdUser)

        self.UiMenu.dateTanggalSurat.setDate(QDate.fromString(dataTglSurat, "yyyy-MM-dd"))


    def readDataSuratKeluar(self):
        results = self.repo.readSuratKeluar()

        table = self.UiMenu.tblSuratKeluar
        table.setRowCount(0)

        if results:
            for row_number, row_data in enumerate(results):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def btnCreateSuratKeluar(self):
        tempIdSurat = self.UiMenu.editID.text()
        tempNoAgenda = self.UiMenu.editNoAgenda.text()
        tempTujuan = self.UiMenu.editTujuan.text()
        tempNoSurat = self.UiMenu.editNoSurat.text()
        tempIsi = self.UiMenu.txtIsi.toPlainText()

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Surat ID cannot be empty.")
            self.UiMenu.editID.setFocus()
            return

        if not tempNoAgenda:
            QMessageBox.warning(self, "Warning", "Agenda Number cannot be empty.")
            self.UiMenu.editNoAgenda.setFocus()
            return

        if not tempTujuan:
            QMessageBox.warning(self, "Warning", "Destination cannot be empty.")
            self.UiMenu.editTujuan.setFocus()
            return

        if not tempNoSurat:
            QMessageBox.warning(self, "Warning", "Surat Number cannot be empty.")
            self.UiMenu.editNoSurat.setFocus()
            return

        if not tempIsi:
            QMessageBox.warning(self, "Warning", "Surat Content cannot be empty.")
            self.UiMenu.txtIsi.setFocus()
            return

        tempFile = self.UiMenu.editFile.text()
        tempKeterangan = self.UiMenu.txtKeterangan.toPlainText()
        tempKode = self.UiMenu.cmbKode.currentText()
        tempIdUser = self.UiMenu.cmbIdUser.currentText()
        tempTglSurat = self.UiMenu.dateTanggalSurat.date().toString("yyyy-MM-dd")

        self.repo.createSuratKeluar(
            tempIdSurat, tempNoAgenda, tempTujuan, tempNoSurat, tempIsi,
            tempKode, tempTglSurat, tempFile,
            tempKeterangan, tempIdUser
        )

        QMessageBox.information(self, "Create Outgoing Mail","Outgoing Mail Data Created Successfully")

        self.readDataSuratKeluar()
        self.btnClearSuratKeluar()

    def btnUpdateSuratKeluar(self):
        tempIdSurat = self.UiMenu.editID.text()
        tempNoAgenda = self.UiMenu.editNoAgenda.text()
        tempTujuan = self.UiMenu.editTujuan.text()
        tempNoSurat = self.UiMenu.editNoSurat.text()
        tempIsi = self.UiMenu.txtIsi.toPlainText()

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Please select data from the table first.")
            return

        if not tempNoAgenda:
            QMessageBox.warning(self, "Warning", "Agenda Number cannot be empty.")
            self.UiMenu.editNoAgenda.setFocus()
            return

        if not tempTujuan:
            QMessageBox.warning(self, "Warning", "Destination cannot be empty.")
            self.UiMenu.editTujuan.setFocus()
            return

        if not tempNoSurat:
            QMessageBox.warning(self, "Warning", "Surat Number cannot be empty.")
            self.UiMenu.editNoSurat.setFocus()
            return

        if not tempIsi:
            QMessageBox.warning(self, "Warning", "Surat Content cannot be empty.")
            self.UiMenu.txtIsi.setFocus()
            return

        tempFile = self.UiMenu.editFile.text()
        tempKeterangan = self.UiMenu.txtKeterangan.toPlainText()
        tempKode = self.UiMenu.cmbKode.currentText()
        tempIdUser = self.UiMenu.cmbIdUser.currentText()
        tempTglSurat = self.UiMenu.dateTanggalSurat.date().toString("yyyy-MM-dd")

        btnConfirm = QMessageBox.question(self, "Confirm Update", "Do you want to update this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.updateSuratKeluar(
                tempNoAgenda, tempTujuan, tempNoSurat, tempIsi,
                tempKode, tempTglSurat, tempFile,
                tempKeterangan, tempIdUser,
                tempIdSurat
            )
            QMessageBox.information(self, "Update Outgoing Mail","Outgoing Mail Data Updated Successfully")
            self.readDataSuratKeluar()
            self.btnClearSuratKeluar()
        else :
            QMessageBox.information(self, "Update Outgoing Mail","Failed to Update Outgoing Mail Data")

    def btnDeleteSuratKeluar(self):
        tempIdSurat = self.UiMenu.editID.text()

        if not tempIdSurat:
            QMessageBox.warning(self, "Warning", "Please select data from the table to delete.")
            return

        btnConfirm = QMessageBox.question(self, "Confirm Delete", "Do you want to delete this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.deleteSuratKeluar(tempIdSurat)
            QMessageBox.information(self, "Delete Outgoing Mail","Outgoing Mail Data Deleted Successfully")
            self.readDataSuratKeluar()
            self.btnClearSuratKeluar()
        else :
            QMessageBox.information(self, "Delete Outgoing Mail","Failed to Delete Outgoing Mail Data")

    def btnClearSuratKeluar(self):
        self.UiMenu.editID.clear()
        self.UiMenu.editNoAgenda.clear()
        self.UiMenu.editTujuan.clear()
        self.UiMenu.editNoSurat.clear()
        self.UiMenu.editFile.clear()
        self.UiMenu.txtIsi.clear()
        self.UiMenu.txtKeterangan.clear()
        self.UiMenu.cmbKode.setCurrentIndex(0)
        self.UiMenu.cmbIdUser.setCurrentIndex(0)
        self.UiMenu.dateTanggalSurat.setDate(QDate.currentDate())
