import vista
import financialspolygon
import bbdd
from datetime import datetime
from polygon import RESTClient
import pandas as pd
import matplotlib.pyplot as plt
"""
Analisis de Finanzas

Esta implementación permite leer datos de una API de finanzas, guardarlos en una base de datos y graficarlos
"""
gestor_BD = bbdd.GestorBD()

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
        
        gestor_BD.guardar_datos(aggs)
        

    elif opcion_principal == "2": #Visualizador de Datos

        while True:
            opcion_vista = vista.visualizador_de_datos()

            if opcion_vista == "1": #Visualizar Resumen
                print("Visualizar Resumen")
                print()

                while True:
                    opcion_resumen = vista.visualizador_de_datos_resumen()

                    if opcion_resumen == "1": #Ticker Cargados
                        
                        resultados = gestor_BD.ticker_cargados()
                        print(resultados)
                    
                    elif opcion_resumen == "2": #Registros Cargados
                        ticker = ""
                        ticker = input("Ingrese un Ticker o presione Enter para contiuar: ")
                        print(ticker)
                        resultados = gestor_BD.registros_cargados(ticker)
                        print(resultados)
                        plt.plot((resultados.loc[:,"date"]),(resultados.loc[:,["open","high","low","close"]]))
                        plt.show()
                        
                        

                    elif opcion_resumen == "0": #Volver
                        print("Volver")
                        print()
                        break

                    else: 
                        print("Opción Incorrecta")
                        print()
        
            elif opcion_vista == "2": #Gráfico de ticker
                print("Gráfico de ticker")
                print()
                ticker = ""
                ticker = input("Ingrese un Ticker o presione Enter para contiuar: ")
                print(ticker)
                resultados = gestor_BD.registros_cargados(ticker)
                plt.plot((resultados.loc[:,"date"]),(resultados.loc[:,["open","high","low","close"]]))
                plt.show()

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