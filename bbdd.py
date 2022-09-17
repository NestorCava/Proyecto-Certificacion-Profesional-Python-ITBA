import sqlite3
import pandas as pd

class GestorBD(object):
    instance = None

    def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self):
        self.con =sqlite3.connect('datafinancial.db')
        self.cursor = self.con.cursor()
        self.crear_tabla()
    
    def __del__(self):
        #Cierre de conexion
        self.con.close()
    
    def execute(self,sql):

        try:
            self.cursor.execute(sql)
        except sqlite3.OperationalError:
            print("Error al ejecutar sentencia")

    def executemany(self,sql,datos):

        try:
            self.cursor.executemany(sql,datos)
        except sqlite3.OperationalError:
            print("Error al ejecutar sentencia")
    
    def commit(self):

        try:
            self.con.commit()
        except sqlite3.OperationalError:
            print("Error al ejecutar sentencia")

    def crear_tabla(self):
        '''Crea la Tabla'''

        sql = ('''CREATE TABLE financial(
                                        ticker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ticker_name TEXT NOT NULL, 
                                        date INTEGER NOT NULL, 
                                        open REAL NOT NULL,
                                        high REAL NOT NULL,
                                        low REAL NOT NULL,
                                        close REAL NOT NULL,
                                        volume REAL NOT NULL,
                                        vwap REAL NOT NULL,
                                        transactions REAL NOT NULL);''')
        self.execute(sql)

    def guardar_datos(self,datos):
        '''Guarda la lista de datos'''
    
        sql = ('''INSERT INTO financial(            
                                        ticker_name, 
                                        date, 
                                        open,
                                        high,
                                        low,
                                        close,
                                        volume,
                                        vwap,
                                        transactions) 
                VALUES(?,?,?,?,?,?,?,?,?);''')
        self.executemany(sql,datos)
        self.commit()
    
    def leer_pandas(self,sql):
        
        resultado = []
        try:
            resultado = pd.read_sql(con=self.con, sql= sql)

        except sqlite3.OperationalError:
            print("Error al leer datos")
        finally:
            return resultado

    def ticker_cargados(self):

        sql = '''SELECT ticker_name,COUNT(ticker_name),MAX(date),MIN(date) FROM(financial) GROUP BY ticker_name;'''
        return self.leer_pandas(sql)
        

    def registros_cargados(self, ticker=""):

        if ticker=="":
            sql = "SELECT * FROM financial;"
            print(sql)
        else:
            sql = (f"SELECT * FROM financial WHERE ticker_name='{ticker}';")
            print(sql)

        return self.leer_pandas(sql)
    
    

