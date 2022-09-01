"""
Modulo para manejar los menu
"""

def presentacion():
    """Mensaje de Bienvenida"""

    print("**************************************")
    print("Bienvenido al Visualizador de Finanzas")
    print("**************************************")
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

def vista_actualizar_datos():
    '''Solicita datos para la petición de aggs'''

    ticker=input('Ingrese "ticker": ')
    fecha_inicio=input("Fecha de Inicio (AAAA-MM-DD): ")
    fecha_fin=input("Fecha de Inicio (AAAA-MM-DD): ")

    return (ticker,fecha_inicio,fecha_fin)