# This Python file uses the following encoding: utf-8
from Connection import getConnection
from mysql.connector import Error

class DisposisiRepository:

    def readDisposisi(self):
        connect = getConnection()
        result = None
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = """SELECT id_disposisi, id_surat, tujuan, isi_disposisi,
                                    sifat, batas_waktu, catatan, id_user
                             FROM disposisi"""
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print("Read Disposisi Success")
            except Error as er:
                print(f"Read Disposisi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()
        return result

    def createDisposisi(self, id_surat, tujuan, isi_disposisi, sifat, batas_waktu, catatan, id_user):
        """Membuat disposisi baru (id_disposisi auto-increment)."""
        connect = getConnection()
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = """INSERT INTO disposisi (id_surat, tujuan, isi_disposisi,
                                     sifat, batas_waktu, catatan, id_user)
                             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    values = (id_surat, tujuan, isi_disposisi, sifat, batas_waktu, catatan, id_user)
                    cursor.execute(sql, values)
                    connect.commit()
                    print("Create Disposisi Success")
            except Error as er:
                print(f"Create Disposisi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()

    def updateDisposisi(self, id_surat, tujuan, isi_disposisi, sifat, batas_waktu, catatan, id_user, id_disposisi):
        """Update disposisi berdasarkan id_disposisi."""
        connect = getConnection()
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = """UPDATE disposisi SET
                                id_surat = %s, tujuan = %s, isi_disposisi = %s,
                                sifat = %s, batas_waktu = %s, catatan = %s, id_user = %s
                             WHERE id_disposisi = %s"""
                    values = (id_surat, tujuan, isi_disposisi, sifat, batas_waktu, catatan, id_user, id_disposisi)
                    cursor.execute(sql, values)
                    connect.commit()
                    print("Update Disposisi Success")
            except Error as er:
                print(f"Update Disposisi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()

    def deleteDisposisi(self, id_disposisi):
        """Hapus disposisi berdasarkan id_disposisi."""
        connect = getConnection()
        if connect:
            try:
                with connect.cursor() as cursor:
                    sql = "DELETE FROM disposisi WHERE id_disposisi = %s"
                    values = (id_disposisi,)
                    cursor.execute(sql, values)
                    connect.commit()
                    print("Delete Disposisi Success")
            except Error as er:
                print(f"Delete Disposisi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if connect and connect.is_connected():
                    connect.close()
