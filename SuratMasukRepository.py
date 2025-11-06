# This Python file uses the following encoding: utf-8
from Connection import getConnection
from mysql.connector import Error


class SuratMasukRepository:

    def readSuratMasuk(self):
        connect = getConnection()
        result = None
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = """SELECT id_surat, no_agenda, asal_surat, no_surat, isi,
                                    kode, indeks, tgl_surat, tgl_diterima, file_path,
                                    keterangan, id_user
                             FROM surat_masuk"""
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print("Read Surat Masuk Success")
            except Error as er:
                print(f"Read Surat Masuk Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()
        return result

    def createSuratMasuk(self, id_surat, no_agenda, asal_surat, no_surat, isi, kode, indeks, tgl_surat, tgl_diterima, file_path, keterangan, id_user):
        """Membuat surat masuk baru. Perhatian: id_surat HARUS diisi manual."""
        connect = getConnection()
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = """INSERT INTO surat_masuk (id_surat, no_agenda, asal_surat, no_surat, isi,
                                      kode, indeks, tgl_surat, tgl_diterima, file_path,
                                      keterangan, id_user)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    values = (id_surat, no_agenda, asal_surat, no_surat, isi, kode, indeks, tgl_surat, tgl_diterima, file_path, keterangan, id_user)
                    cursor.execute(sql, values)
                    connect.commit()
                    print("Create Surat Masuk Success")
            except Error as er:
                print(f"Create Surat Masuk Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()

    def updateSuratMasuk(self, no_agenda, asal_surat, no_surat, isi, kode, indeks, tgl_surat, tgl_diterima, file_path, keterangan, id_user, id_surat):
        """Update surat masuk berdasarkan id_surat."""
        connect = getConnection()
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = """UPDATE surat_masuk SET
                                no_agenda = %s, asal_surat = %s, no_surat = %s, isi = %s,
                                kode = %s, indeks = %s, tgl_surat = %s, tgl_diterima = %s,
                                file_path = %s, keterangan = %s, id_user = %s
                             WHERE id_surat = %s"""
                    values = (no_agenda, asal_surat, no_surat, isi, kode, indeks, tgl_surat, tgl_diterima, file_path, keterangan, id_user, id_surat)
                    cursor.execute(sql, values)
                    connect.commit()
                    print("Update Surat Masuk Success")
            except Error as er:
                print(f"Update Surat Masuk Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()

    def deleteSuratMasuk(self, id_surat):
        """Hapus surat masuk berdasarkan id_surat."""
        connect = getConnection()
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = "DELETE FROM surat_masuk WHERE id_surat = %s"
                    values = (id_surat,)
                    cursor.execute(sql, values)
                    connect.commit()
                    print("Delete Surat Masuk Success")
            except Error as er:
                print(f"Delete Surat Masuk Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()
