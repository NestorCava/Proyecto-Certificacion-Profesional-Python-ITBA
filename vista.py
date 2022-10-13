from os import system
import pandas as pd
import matplotlib.pyplot as plt
"""
Modulo para manejar los menu
"""
ancho_pantalla = 120

def presentacion():
    """Mensaje de Bienvenida
    """
    
    system("cls")
    print("*"*ancho_pantalla)
    mensaje = "Bienvenido al Visualizador de Finanzas"
    print("*"*(int((ancho_pantalla-len(mensaje))/2)) +
          mensaje+"*"*(int((ancho_pantalla-len(mensaje))/2)))
    print("*"*ancho_pantalla)
    print()

def menu_principal():
    """Opciones del Menú Principal
    
        Returns:
            opcion (str): String con la opción elegida
    """
    mensaje = "MENÚ PRINCIPAL"
    
    print("*"*(int((ancho_pantalla-len(mensaje))/2)) +
          mensaje+"*"*(int((ancho_pantalla-len(mensaje))/2)))
    print()
    print("(1) Actualización de Datos")
    print("(2) Visualización de Datos")
    print("(0) Salir")

    opcion = input("Ingrese una opción: ")
    print()

    return opcion

def vista_actualizar_datos():
    """Solicita datos para la petición de aggs

    Returns:
        _type_: _description_
    """
    
    mensaje = "Actualización de Datos"
    
    print("*"*(int((ancho_pantalla-len(mensaje))/2)) +
          mensaje+"*"*(int((ancho_pantalla-len(mensaje))/2)))
    print()

    ticker=(input('Ingrese "ticker": ')).upper()
    fecha_inicio=input("Fecha de Inicio (AAAA-MM-DD): ")
    fecha_fin=input("Fecha de Fin (AAAA-MM-DD): ")

    return (ticker,fecha_inicio,fecha_fin)

def visualizador_de_datos():
    """
    Opciones para Visualizador Datos

        Returns:
            opcion (str): String con la opción elegida
    """
    mensaje = "Visualizador de Datos"
    
    print("*"*(int((ancho_pantalla-len(mensaje))/2)) +
          mensaje+"*"*(int((ancho_pantalla-len(mensaje))/2)))
    print()

    print("(1) Ticker Cargados")
    print("(2) Registros Cargados")
    print("(3) Gráfico de Ticker")
    print("(0) Volver")

    opcion = input("Ingrese una opción: ")

    return opcion

def graficar(resultados, ticker):
    """Visualización de los datos en forma gráfica

    Args:
        resultados (list): lista con los datos en forma de DataFrame
        ticker (str): Nombre del ticker que se quiere graficar
    """

    
    plt.plot((resultados.loc[:,"date"]),(resultados.loc[:,["open"]]))
    plt.title(f"Evolución {ticker}")
    plt.xticks(rotation=90)
    plt.show()  


