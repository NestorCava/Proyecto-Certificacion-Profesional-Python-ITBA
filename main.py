import vista
"""
Analisis de Finanzas

Esta implementación permite leer datos de una API de finanzas, guardarlos en una base de datos y graficarlos
"""
while True:
    vista.presentacion()
    opcion = vista.menu_principal()

    if opcion == "1": #Actualización de Datos
        print("Actualización de Datos")
        print()
        
    elif opcion == "2": #Visualizador de Datos
        print("Visualizador de Datos")
        print()

    elif opcion == "0": #Salida
        break

    else: #Mensaje de Error
        print("Opción elegida incorrecta")
        print()