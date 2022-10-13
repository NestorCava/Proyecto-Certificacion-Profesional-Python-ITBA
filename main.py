import vista
import financialspolygon
import bbdd
from datetime import datetime
from os import system
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

    if opcion_principal == "1": 
        """
        Menú para la Actualización de Datos
        """

        print("Actualización de Datos")
        print()
        ticker, fecha_inicio, fecha_fin = vista.vista_actualizar_datos()
        aggs = financialspolygon.obtener_datos(ticker, fecha_inicio, fecha_fin)
        
        if not len(aggs)==0:
            datos = pd.DataFrame(aggs, columns=[
                "ticker_name", "date", "open", "high", "low", "close", "volume", "vwap", "transactions"])
    
            datos['date'] = [datetime.fromtimestamp(d/1000) for d in datos['date']]    
              
            print(datos)
            guardar = input("¿Desea Guardar los Datos? S/N: ")
            if guardar.upper() == "S":
                gestor_BD.guardar_datos(aggs)
                print("Datos Guardados")
            else:
                print("Datos NO Guardados")
        else:
            print("Verifique los datos ingresados")
        
        system("pause")
        
    
    elif opcion_principal == "2": 
        """
        Menú para la Visualización de los Datos
        """

        while True:
            opcion_vista = vista.visualizador_de_datos()

            if opcion_vista == "1": 
                """
                Submenú de Visualización para ver los ticker cargados
                """
                        
                resultados = gestor_BD.ticker_cargados()
                
                if not resultados.empty:
                    resultados.rename(columns={"COUNT(ticker_name)":"Count",
                                               "MAX(open)":"Open Max",
                                               "MIN(open)":"Open Min",
                                               "MAX(date)":"Date Final",
                                               "MIN(date)":"Date Init"},
                                      inplace=True)
                    resultados["Date Final"] = [datetime.fromtimestamp(d/1000) for d in resultados["Date Final"]] 
                    resultados['Date Init'] = [datetime.fromtimestamp(d/1000) for d in resultados['Date Init']] 
                    print(resultados)
                else:
                    print("No hay datos para mostrar")
                system("pause")
                    
            elif opcion_vista == "2": #Registros Cargados
                """
                Submenú de Visualización para ver los registros cargados de un ticker
                """

                ticker = ""
                ticker = (input("Ingrese un Ticker o presione Enter para contiuar: ")).upper()
                
                resultados = gestor_BD.registros_cargados(ticker)
                
                if not resultados.empty:
                    resultados['date'] = [datetime.fromtimestamp(d/1000) for d in resultados['date']]  
                    print(resultados)
                else:
                    print("No hay datos para mostrar")

                system("pause")
                        
            elif opcion_vista == "3": #Gráfico de ticker
                """
                Submenú de Visualización para graficar los registros cargados de un ticker
                """

                print("Gráfico de ticker")
                print()
                ticker = ""
                ticker = (input("Ingrese un Ticker: ")).upper()
                if ticker=="":
                    print("NO ingresó Ticker")
                    system("pause")
                else:
                    resultados = gestor_BD.registros_cargados(ticker)
                    resultados['date'] = [datetime.fromtimestamp(d/1000) for d in resultados['date']]   

                    if not resultados.empty:
                        # plt.plot((resultados.loc[:,"date"]),(resultados.loc[:,["open","high","low","close"]]))
                        # plt.show()     
                        vista.graficar(resultados, ticker.upper())
                    else:
                        print("No hay resultados para mostrar")
                        system("pause")       

            elif opcion_vista == "0":
                """
                Opción para volver
                """
                print("Volver")
                print()
                break

            else: 
                """
                Mensaje de error cuando la opción elegida en el submenu de visualización es incorrecta
                """
                print("Opción Incorrecta")
                print()

    elif opcion_principal == "0": 
        """
        Opción para Salir
        """
        break

    else: 
        """
        Mensaje de Error cuando la opción elegida en el menú principal es incorrecta
        """
        print("Opción elegida incorrecta")
        print()