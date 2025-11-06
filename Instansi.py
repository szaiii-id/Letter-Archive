import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from InstansiRepository import InstansiRepository

class InstansiPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Page Pengaturan Instansi")
        UiFile = QFile("Instansi.ui")
        UiFile.open(QFile.ReadOnly)

        UiLoader = QUiLoader()
        self.UiMenu = UiLoader.load(UiFile, self)

        self.resize(self.UiMenu.size())

        self.repo = InstansiRepository()

        self.UiMenu.btnCreate.clicked.connect(self.btnCreateInstansi)
        self.UiMenu.btnUpdate.clicked.connect(self.btnUpdateInstansi)
        self.UiMenu.btnDelete.clicked.connect(self.btnDeleteInstansi)
        self.UiMenu.btnClear.clicked.connect(self.btnClearInstansi)

        self.UiMenu.tblInstansi.cellClicked.connect(self.tableCellClick)

        self.tableView()
        self.readDataInstansi()

    def tableView(self):
        headers = ["ID", "Nama Instansi", "Alamat", "Telpon", "Website", "Email", "Logo Path"]
        table = self.UiMenu.tblInstansi
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def tableCellClick(self, row, column):

        dataIdInstansi = self.UiMenu.tblInstansi.item(row, 0).text()
        dataNamaInstansi = self.UiMenu.tblInstansi.item(row, 1).text()
        dataAlamat = self.UiMenu.tblInstansi.item(row, 2).text()
        dataTelpon = self.UiMenu.tblInstansi.item(row, 3).text()
        dataWebsite = self.UiMenu.tblInstansi.item(row, 4).text()
        dataEmail = self.UiMenu.tblInstansi.item(row, 5).text()
        dataLogoPath = self.UiMenu.tblInstansi.item(row, 6).text()

        self.UiMenu.editID.setText(dataIdInstansi)
        self.UiMenu.editNamaInstansi.setText(dataNamaInstansi)
        self.UiMenu.txtAlamat.setText(dataAlamat)
        self.UiMenu.editTelp.setText(dataTelpon)
        self.UiMenu.editWebsite.setText(dataWebsite)
        self.UiMenu.editEmail.setText(dataEmail)
        self.UiMenu.editLogo.setText(dataLogoPath)


    def readDataInstansi(self):
        results = self.repo.readInstansi()

        table = self.UiMenu.tblInstansi
        table.setRowCount(0)

        if results:
            for row_number, row_data in enumerate(results):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def btnCreateInstansi(self):
        tempIdInstansi = self.UiMenu.editID.text()
        tempNamaInstansi = self.UiMenu.editNamaInstansi.text()
        tempAlamat = self.UiMenu.txtAlamat.toPlainText()
        tempTelpon = self.UiMenu.editTelp.text()
        tempWebsite = self.UiMenu.editWebsite.text()
        tempEmail = self.UiMenu.editEmail.text()
        tempLogoPath = self.UiMenu.editLogo.text()

        if not tempIdInstansi:
            QMessageBox.warning(self, "Warning", "Instansi ID cannot be empty.")
            self.UiMenu.editID.setFocus()
            return

        if not tempNamaInstansi:
            QMessageBox.warning(self, "Warning", "Nama Instansi cannot be empty.")
            self.UiMenu.editNamaInstansi.setFocus()
            return

        if not tempAlamat:
            QMessageBox.warning(self, "Warning", "Alamat cannot be empty.")
            self.UiMenu.txtAlamat.setFocus()
            return

        if not tempTelpon:
            QMessageBox.warning(self, "Warning", "Telepon cannot be empty.")
            self.UiMenu.editTelp.setFocus()
            return

        self.repo.createInstansi(
            tempIdInstansi, tempNamaInstansi, tempAlamat, tempTelpon,
            tempWebsite, tempEmail, tempLogoPath
        )

        QMessageBox.information(self, "Create Instansi","Instansi Data Created Successfully")

        self.readDataInstansi()
        self.btnClearInstansi()

    def btnUpdateInstansi(self):
        tempIdInstansi = self.UiMenu.editID.text()
        tempNamaInstansi = self.UiMenu.editNamaInstansi.text()
        tempAlamat = self.UiMenu.txtAlamat.toPlainText()
        tempTelpon = self.UiMenu.editTelp.text()
        tempWebsite = self.UiMenu.editWebsite.text()
        tempEmail = self.UiMenu.editEmail.text()
        tempLogoPath = self.UiMenu.editLogo.text()

        if not tempIdInstansi:
            QMessageBox.warning(self, "Warning", "Please select data from the table first.")
            return

        if not tempNamaInstansi:
            QMessageBox.warning(self, "Warning", "Nama Instansi cannot be empty.")
            self.UiMenu.editNamaInstansi.setFocus()
            return

        if not tempAlamat:
            QMessageBox.warning(self, "Warning", "Alamat cannot be empty.")
            self.UiMenu.txtAlamat.setFocus()
            return

        if not tempTelpon:
            QMessageBox.warning(self, "Warning", "Telepon cannot be empty.")
            self.UiMenu.editTelp.setFocus()
            return

        btnConfirm = QMessageBox.question(self, "Confirm Update", "Do you want to update this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.updateInstansi(
                tempNamaInstansi, tempAlamat, tempTelpon,
                tempWebsite, tempEmail, tempLogoPath,
                tempIdInstansi
            )
            QMessageBox.information(self, "Update Instansi","Instansi Data Updated Successfully")
            self.readDataInstansi()
            self.btnClearInstansi()
        else :
            QMessageBox.information(self, "Update Instansi","Failed to Update Instansi Data")

    def btnDeleteInstansi(self):
        tempIdInstansi = self.UiMenu.editID.text()

        if not tempIdInstansi:
            QMessageBox.warning(self, "Warning", "Please select data from the table to delete.")
            return

        btnConfirm = QMessageBox.question(self, "Confirm Delete", "Do you want to delete this data?")

        if btnConfirm == QMessageBox.Yes :
            self.repo.deleteInstansi(tempIdInstansi)
            QMessageBox.information(self, "Delete Instansi","Instansi Data Deleted Successfully")
            self.readDataInstansi()
            self.btnClearInstansi()
        else :
            QMessageBox.information(self, "Delete Instansi","Failed to Delete Instansi Data")

    def btnClearInstansi(self):
        self.UiMenu.editID.clear()
        self.UiMenu.editNamaInstansi.clear()
        self.UiMenu.txtAlamat.clear()
        self.UiMenu.editTelp.clear()
        self.UiMenu.editWebsite.clear()
        self.UiMenu.editEmail.clear()
        self.UiMenu.editLogo.clear()
