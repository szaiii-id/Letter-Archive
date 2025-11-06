# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


from SuratMasuk import SuratMasukPage
from SuratKeluar import SuratKeluarPage
from Disposisi import DisposisiPage
from Instansi import InstansiPage

class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        UiFile = QFile("main.ui")
        UiFile.open(QFile.ReadOnly)

        UiLoader = QUiLoader()
        self.UiMenu = UiLoader.load(UiFile, self)

        self.setMenuBar(self.UiMenu.menuBar())
        self.resize(self.UiMenu.size())

        action_surat_masuk = self.UiMenu.actionSuratMasuk
        action_surat_masuk.triggered.connect(self.suratMasukOnClick)

        action_surat_keluar = self.UiMenu.actionSuratKeluar
        action_surat_keluar.triggered.connect(self.suratKeluarOnClick)

        action_disposisi = self.UiMenu.actionDisposisi
        action_disposisi.triggered.connect(self.disposisiOnClick)

        action_instansi = self.UiMenu.actionInstansi
        action_instansi.triggered.connect(self.instansiOnClick)


    def suratMasukOnClick(self):
        self.suratMasukApp = SuratMasukPage(self)
        self.suratMasukApp.show()

    def suratKeluarOnClick(self):
        self.suratKeluarApp = SuratKeluarPage(self)
        self.suratKeluarApp.show()

    def disposisiOnClick(self):
        self.disposisiApp = DisposisiPage(self)
        self.disposisiApp.show()

    def instansiOnClick(self):
        self.instansiApp = InstansiPage(self)
        self.instansiApp.show()
    # -----------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appInstace = main()
    appInstace.show()
    sys.exit(app.exec())
