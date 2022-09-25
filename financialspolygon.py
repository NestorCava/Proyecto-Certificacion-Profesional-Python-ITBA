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
    
    client = RESTClient('fhj7pibsaRPl8kwrMeSjPtL_VDCpi1TX')

    print('******AGGS**********')
    aggs_lista = []
    try:
        aggs = client.get_aggs(ticker, 1, "day", fecha_inicio, fecha_fin)
    
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
        print("Error al Leer Valores desde el servidor")
    except BadResponse:
        print("Error al Leer Valores desde el servidor")
    return aggs_lista
    