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
            pass

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

def guardar_datos(datos):
    '''Guarda la lista de datos'''
    
    #Conexión con la base de datos
    con = sqlite3.connect('datafinancial.db')

    #Creación del cursor
    cursor = con.cursor()
    
    try:
        #Creación de Tablas
        cursor.executemany('''INSERT INTO financial(            
                                                    ticker_name, 
                                                    date, 
                                                    open,
                                                    high,
                                                    low,
                                                    close,
                                                    volume,
                                                    vwap,
                                                    transactions) 
                                VALUES(?,?,?,?,?,?,?,?,?);''',
                                datos)
        con.commit()
    except sqlite3.OperationalError:
        print("Datos no agregados")
    finally:
        #Cierre de conexion
        con.close()

def ticker_cargados():

    #Conexión con la base de datos
    con = sqlite3.connect('datafinancial.db')

    #Creación del cursor
    cursor = con.cursor()
    resultado = []
    try:
        sql = '''SELECT ticker_name,COUNT(ticker_name),MAX(date),MIN(date) FROM(financial) GROUP BY ticker_name;'''
        resultado = pd.read_sql(con=con, sql= sql)

    except sqlite3.OperationalError:
        print("Error al leer datos")
    finally:
        #Cierre de conexion
        con.close() 
        return resultado

def registros_cargados():

    #Conexión con la base de datos
    con = sqlite3.connect('datafinancial.db')

    #Creación del cursor
    cursor = con.cursor()
    resultado = []
    try:
        sql = "SELECT * FROM financial;"
        resultado = pd.read_sql(con=con, sql= sql)

    except sqlite3.OperationalError:
        print("Error al leer datos")
    finally:
        #Cierre de conexion
        con.close() 
        return resultado
