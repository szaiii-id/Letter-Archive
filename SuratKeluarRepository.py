from Connection import getConnection
from mysql.connector import Error

class SuratKeluarRepository:

    def readSuratKeluar(self):
        connect = getConnection()
        result = None
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = """SELECT id_surat, no_agenda, tujuan, no_surat, isi,
                                kode, tgl_surat, file_path, keterangan, id_user
                         FROM surat_keluar"""
                cursor.execute(sql)
                result = cursor.fetchall()
                print("Read Surat Keluar Success")
            except Error as er:
                print(f"Read Surat Keluar Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()
        return result

    def createSuratKeluar(self, id_surat, no_agenda, tujuan, no_surat, isi, kode, tgl_surat, file_path, keterangan, id_user):
        connect = getConnection()
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = """INSERT INTO surat_keluar (id_surat, no_agenda, tujuan, no_surat, isi,
                                    kode, tgl_surat, file_path, keterangan, id_user)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (id_surat, no_agenda, tujuan, no_surat, isi, kode, tgl_surat, file_path, keterangan, id_user)
                cursor.execute(sql, values)
                connect.commit()
                print("Create Surat Keluar Success")
            except Error as er:
                print(f"Create Surat Keluar Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()

    def updateSuratKeluar(self, no_agenda, tujuan, no_surat, isi, kode, tgl_surat, file_path, keterangan, id_user, id_surat):
        connect = getConnection()
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = """UPDATE surat_keluar SET
                            no_agenda = %s, tujuan = %s, no_surat = %s, isi = %s,
                            kode = %s, tgl_surat = %s, file_path = %s,
                            keterangan = %s, id_user = %s
                         WHERE id_surat = %s"""
                values = (no_agenda, tujuan, no_surat, isi, kode, tgl_surat, file_path, keterangan, id_user, id_surat)
                cursor.execute(sql, values)
                connect.commit()
                print("Update Surat Keluar Success")
            except Error as er:
                print(f"Update Surat Keluar Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()

    def deleteSuratKeluar(self, id_surat):
        connect = getConnection()
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = "DELETE FROM surat_keluar WHERE id_surat = %s"
                values = (id_surat,)
                cursor.execute(sql, values)
                connect.commit()
                print("Delete Surat Keluar Success")
            except Error as er:
                print(f"Delete Surat Keluar Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()
