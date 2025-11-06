# This Python file uses the following encoding: utf-8

import mysql.connector as myConnection
from mysql.connector import Error

def getConnection():

    connection = None
    try:
        connection = myConnection.connect(
            host = "localhost",
            user = "root",
            password = "Lostvyne04!",
            database = "pbo2_2310010358"
        )

        if connection.is_connected():
            print("Connection Success")
            return connection
    except Error as er:
        print(f"Connection Failed : {er}")
        return None

