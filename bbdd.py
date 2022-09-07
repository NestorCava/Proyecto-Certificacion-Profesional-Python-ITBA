import sqlite3

def crear_tabla():
    '''Crea la Tabla'''

    #Conexión con la base de datos
    con = sqlite3.connect('datafinancial.db')

    #Creación del cursor
    cursor = con.cursor()
    
    try:
        #Creación de Tablas 
        cursor.execute('''CREATE TABLE financial(
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
    except sqlite3.OperationalError:
        pass
    finally:
        #Cierre de conexion
        con.close()

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
 