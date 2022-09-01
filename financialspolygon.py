from polygon import RESTClient

def obtener_datos(ticker, fecha_inicio, fecha_fin):
    client = RESTClient('fhj7pibsaRPl8kwrMeSjPtL_VDCpi1TX')

    print('******AGGS**********')
    aggs = client.get_aggs(ticker, 1, "day", fecha_inicio, fecha_fin)

    return aggs
    