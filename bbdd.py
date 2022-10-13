import sqlite3
import pandas as pd

class GestorBD(object):
    """Singleton para el manejo de la base de datos
    """
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

        datos_depurado = []
        
        for d in datos:
            if len(self.cursor.execute("select count(*) from financial").fetchall()) == 0:
                datos_depurado.append(d)
                # print("Bandera 1")
            elif len(self.registros_cargados_por_fecha(d[0],d[1]))==0:
                datos_depurado.append(d)
                # print("Bandera 2")
        
        if not len(datos_depurado)==0:
            sql = ('''INSERT INTO financial(            
                                            ticker_name, 
                                            date, 
                                            open,
                                            high,
                                            low,
                                            close,
                                            volume,
                                            vwap,
                                            transactions
                                            ) 
                     VALUES(?,?,?,?,?,?,?,?,?);''')
            self.executemany(sql,datos_depurado)
            self.commit()
    
    def leer_pandas(self,sql):
        """Lee datos de la base de datos según la sentencia sql pasada

        Args:
            sql (str): sentencia sql

        Returns:
            list: lista con los valores de la base de datos
        """
        resultado = []
        try:
            resultado = pd.read_sql(con=self.con, sql= sql)
            #print("Error al leer datos")
        finally:
            return resultado

    def ticker_cargados(self):
        """Función para obtener una lista de los ticker cargados y un resumen de datos asociados

        Returns:
            list: lista de ticker con un resumen de datos asociados a los mismos. Lista de DataFrame
        """

        sql = '''SELECT ticker_name,COUNT(ticker_name),MAX(open),MIN(open),MAX(date),MIN(date) FROM(financial) GROUP BY ticker_name;'''
        return self.leer_pandas(sql)
        

    def registros_cargados(self, ticker=""):
        """Obtiene registros según el ticker pasado.

        Si no se pasa ningun valor de ticker, la función devuelve toda la base de datos

        Args:
            ticker (str, optional): ticker del que se requiere información. Defaults to "".

        Returns:
            list: lista de DataFrame con los valores
        """
        if ticker=="":
            sql = "SELECT * FROM financial ORDER BY  ticker_name, date;"
        else:
            sql = (f"SELECT * FROM financial WHERE ticker_name='{ticker}' ORDER BY  date;")

        return self.leer_pandas(sql)
    
    def registros_cargados_por_periodo(self, ticker, fecha_inicio, fecha_fin):
        """Devuelve los valores de un período determinado de un ticker determinado

        Args:
            ticker (str): ticker del que se quiere obtener información
            fecha_inicio (timestamp): fecha inicial del periodo
            fecha_fin (timestamp): fecha final del periodo

        Returns:
            list: lista de DataFrame con los valores
        """

        if ticker=="":
            sql = (f'''SELECT * FROM financial 
                     WHERE date BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
                     ORDER BY  ticker_name, date;''')
        else:
            sql = (f'''SELECT * FROM financial 
                     WHERE ticker_name='{ticker}' AND date BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
                     ORDER BY  date;''')

        return self.leer_pandas(sql)

    def registros_cargados_por_fecha(self, ticker, fecha):
        """Devuelve los valores de una fecha determinada de un ticker determinado

        Args:
            ticker (str): ticker del que se quiere obtener información
            fecha (timestamp): fecha de la que se quiere obtener información

        Returns:
            list: lista de DataFrame con los valores
        """

        if ticker=="":
            sql = (f'''SELECT * FROM financial 
                        WHERE date='{fecha}'
                        ORDER BY  ticker_name, date;''')
        else:
            sql = (f'''SELECT * FROM financial 
                       WHERE ticker_name='{ticker}' AND date='{fecha}'
                       ORDER BY  date;''')

        return self.leer_pandas(sql)
    

