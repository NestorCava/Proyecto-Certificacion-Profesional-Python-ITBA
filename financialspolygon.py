from time import time
from polygon import RESTClient
from datetime import datetime, timedelta
import requests
import json

def obtener_datos(ticker, fecha_inicio, fecha_fin):
    
    client = RESTClient('fhj7pibsaRPl8kwrMeSjPtL_VDCpi1TX')

    print('******AGGS**********')
    aggs = client.get_aggs(ticker, 1, "day", fecha_inicio, fecha_fin)
    aggs_lista = []
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
    return aggs_lista
    