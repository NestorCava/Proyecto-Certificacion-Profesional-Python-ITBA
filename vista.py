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
    print("*"*(int((ancho_pantalla-len(mensaje))/2))+mensaje+"*"*(int((ancho_pantalla-len(mensaje))/2)))
    print("*"*ancho_pantalla)
    print()

def menu_principal():
    """
    Opciones del Menú Principal
    
        Returns:
            opcion (str): String con la opción elegida
    """
    
    print("*******MENÚ PRINCIPAL****************")
    print("(1) Actualización de Datos")
    print("(2) Visualización de Datos")
    print("(0) Salir")

    opcion = input("Ingrese una opción: ")

    return opcion

def vista_actualizar_datos():
    '''Solicita datos para la petición de aggs'''

    ticker=input('Ingrese "ticker": ')
    fecha_inicio=input("Fecha de Inicio (AAAA-MM-DD): ")
    fecha_fin=input("Fecha de Fin (AAAA-MM-DD): ")

    return (ticker,fecha_inicio,fecha_fin)

def visualizador_de_datos():
    """
    Opciones para Visualizador Datos

        Returns:
            opcion (str): String con la opción elegida
    """

    print("***********Visualizador de Datos***********")
    print()
    print("(1) Resumen")
    print("(2) Gráfico de ticker")
    print("(0) Volver")

    opcion = input("Ingrese una opción: ")

    return opcion

def visualizador_de_datos_resumen():
    '''Menu Resumen con vistas disponibles'''

    print("*********MENÚ RESUMEN************")
    print()
    print("(1) Ticker Cargados")
    print("(2) Registros Cargados")
    print("(0) Volver")

    opcion = input("Ingrese una opción: ")
    return opcion



