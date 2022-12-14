from time import time
from polygon import RESTClient
from datetime import datetime, timedelta
import requests
import json

from polygon.exceptions import BadResponse, NoResultsError

def obtener_datos(ticker, fecha_inicio, fecha_fin):
    '''
    Obtiene los datos de la API Polygon
    
        Param:
            ticker(str): Valor del ticker que deseamos
            fecha_inicio(str): Fecha de inicio de los datos (YYYY-MM-DD)
            fecha_fin(str): Fecha de fin de los datos (YYYY-MM-DD)
        
        Return:
            aggs_lista(lista): lista de tuplas con los datos obtenidos
    '''
    fecha_inicio_date = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin_date = datetime.strptime(fecha_fin, '%Y-%m-%d')

    # client = RESTClient('fhj7pibsaRPl8kwrMeSjPtL_VDCpi1TX')

    #print('******AGGS**********')
    aggs_lista = []
    fecha = fecha_inicio_date

    while (fecha <= fecha_fin_date):

        fecha_fin_2 = fecha_fin_date
        if ((fecha-fecha_fin_date).days>50): fecha_fin_2 += timedelta(50)
        
        try:
            client = RESTClient('fhj7pibsaRPl8kwrMeSjPtL_VDCpi1TX')
            aggs = client.get_aggs(ticker, 1, "minute", 
                                   fecha.strftime('%Y-%m-%d'), 
                                   fecha_fin_2.strftime('%Y-%m-%d'),
                                   limit=50000)
    
            for agg in aggs:
                aggs_lista.append((ticker,
                                agg.timestamp,
                                agg.open,
                                agg.high,
                                agg.low,
                                agg.close,
                                agg.volume,
                                agg.vwap,
                                agg.transactions))

            
        except NoResultsError:
            print("Error al Leer Valores desde el servidor 1")
        except BadResponse:
            print("Error al Leer Valores desde el servidor 2")
        finally:
            fecha += timedelta(51)
    
    return aggs_lista
    