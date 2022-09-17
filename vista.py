from os import system
"""
Modulo para manejar los menu
"""
ancho_pantalla = 120

def presentacion():
    """Mensaje de Bienvenida"""
    
    system("cls")
    print("*"*ancho_pantalla)
    mensaje = "Bienvenido al Visualizador de Finanzas"
    print("*"*(int((ancho_pantalla-len(mensaje))/2)) +
          mensaje+"*"*(int((ancho_pantalla-len(mensaje))/2)))
    print("*"*ancho_pantalla)
    print()

def menu_principal():
    """
    Opciones del Menú Principal
    
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
    '''Solicita datos para la petición de aggs'''
    
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

    print("(1) Resumen de Ticker Cargados")
    print("(2) Resumen de Registros Cargados")
    print("(3) Gráfico de Ticker")
    print("(0) Volver")

    opcion = input("Ingrese una opción: ")

    return opcion



