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
    """Opciones del Menú Principal"""
    
    print("*******MENÚ PRINCIPAL****************")
    print("(1) Actualización de Datos")
    print("(2) Visualización de Datos")
    print("(0) Salir")

    opcion = input("Ingrese una opción: ")

    return opcion

def visualizador_de_datos():
    """Opciones para Visualizador Datos"""

    print("***********Visualizador de Datos***********")
    print()
    print("(1) Resumen")
    print("(2) Gráfico de ticker")
    print("(0) Volver")

    opcion = input("Ingrese una opción: ")

    return opcion