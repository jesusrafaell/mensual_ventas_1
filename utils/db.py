from variables import *
import pyodbc

class Database:
    
    def __init__(self):
        self.codigoError = ""
        self.descripcionError = ""	
        self.conn = None                
        self.entrada = None

    def conectar():
        try:		
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos", e)
            return None

    def getCuentaBanco(cnxn):
        SPsql = "EXEC GetCuentaBanco"
        result = cnxn.cursor().execute(SPsql)
        row = result.fetchone()
        # print (row[0])
        return row[0]


