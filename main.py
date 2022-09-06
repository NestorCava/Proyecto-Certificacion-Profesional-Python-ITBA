import vista
import financialspolygon
from datetime import datetime
from polygon import RESTClient
"""
Analisis de Finanzas

Esta implementación permite leer datos de una API de finanzas, guardarlos en una base de datos y graficarlos
"""
while True:
    vista.presentacion()
    opcion_principal = vista.menu_principal()

    if opcion_principal == "1": #Actualización de Datos
        print("Actualización de Datos")
        print()
        ticker, fecha_inicio, fecha_fin = vista.vista_actualizar_datos()
        aggs = financialspolygon.obtener_datos(ticker, fecha_inicio, fecha_fin)
        
        for agg in aggs:
            print(agg)

    elif opcion_principal == "2": #Visualizador de Datos

        while True:
            opcion_vista = vista.visualizador_de_datos()

            if opcion_vista == "1": #Visualizar Resumen
                print("Visualizar Resumen")
                print()
        
            elif opcion_vista == "2": #Gráfico de ticker
                print("Gráfico de ticker")
                print()

            elif opcion_vista == "0": #Volver
                print("Volver")
                print()
                break
        
            else:
                print("Opción Incorrecta")
                print()

    elif opcion_principal == "0": #Salida
        break

    else: #Mensaje de Error
        print("Opción elegida incorrecta")
        print()