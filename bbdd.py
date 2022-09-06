import sqlite3

def crear_tabla():
    #Conexión con la base de datos
    con = sqlite3.connect('datafinancial.db')

    #Creación del cursor
    cursor = con.cursor()
    
    try:
        #Creación de Tablas
        cursor.execute('''CREATE TABLE financial(
                        ticker_id INTEGER PRIMARY KEY,
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