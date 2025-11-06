from Connection import getConnection
from mysql.connector import Error

class InstansiRepository:

    def readInstansi(self):
        connect = getConnection()
        result = None
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = """SELECT id_instansi, nama_instansi, alamat,
                                telpon, website, email, logo_path
                         FROM pengaturan_instansi"""
                cursor.execute(sql)
                result = cursor.fetchall()
                print("Read Instansi Success")
            except Error as er:
                print(f"Read Instansi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()
        return result

    def createInstansi(self, id_instansi, nama_instansi, alamat, telpon, website, email, logo_path):
        connect = getConnection()
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = """INSERT INTO pengaturan_instansi (id_instansi, nama_instansi, alamat,
                                          telpon, website, email, logo_path)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                values = (id_instansi, nama_instansi, alamat, telpon, website, email, logo_path)
                cursor.execute(sql, values)
                connect.commit()
                print("Create Instansi Success")
            except Error as er:
                print(f"Create Instansi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()

    def updateInstansi(self, nama_instansi, alamat, telpon, website, email, logo_path, id_instansi):
        connect = getConnection()
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = """UPDATE pengaturan_instansi SET
                            nama_instansi = %s, alamat = %s, telpon = %s,
                            website = %s, email = %s, logo_path = %s
                         WHERE id_instansi = %s"""
                values = (nama_instansi, alamat, telpon, website, email, logo_path, id_instansi)
                cursor.execute(sql, values)
                connect.commit()
                print("Update Instansi Success")
            except Error as er:
                print(f"Update Instansi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()

    def deleteInstansi(self, id_instansi):
        connect = getConnection()
        cursor = None
        if connect:
            try:
                cursor = connect.cursor()
                sql = "DELETE FROM pengaturan_instansi WHERE id_instansi = %s"
                values = (id_instansi,)
                cursor.execute(sql, values)
                connect.commit()
                print("Delete Instansi Success")
            except Error as er:
                print(f"Delete Instansi Failed : {er}")
                if connect:
                    connect.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connect and connect.is_connected():
                    connect.close()
