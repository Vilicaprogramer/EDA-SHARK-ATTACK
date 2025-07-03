import pandas as pd
import numpy as np
import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
from meteostat import Point, Daily


def gnerar_meteostat(area, country, date):
    try:
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.geocode(area + ',' + country)
        if location == None:
            return None, None, None, None
        else:
            lat = location.latitude
            lon = location.longitude

            # Set time period
            start = date - timedelta(weeks=1)
            end =  date + timedelta(weeks=1)
            return lat, lon, start, end
    except:
        return None, None, None, None


def buscar_datos_meteo_cercanos(lat, lon, start, end, pasos=10, offset=0.05):
    """
    Busca datos meteorológicos moviendo ligeramente las coordenadas hasta encontrar datos válidos.
    
    :param lat: Latitud inicial
    :param lon: Longitud inicial
    :param start: Fecha de inicio (datetime)
    :param end: Fecha de fin (datetime)
    :param pasos: Número de pasos en cada dirección
    :param offset: Tamaño de cada desplazamiento (en grados)
    :return: (dataframe de meteostat, coordenadas usadas) o (None, None) si falla
    """
    if (lat == None) & (lon == None) & (start == None) & (end == None):
        return None, None
    else:
        for i in range(-pasos, pasos + 1):
            for j in range(-pasos, pasos + 1):
                lat_nueva = lat + i * offset
                lon_nueva = lon + j * offset
                punto = Point(lat_nueva, lon_nueva)

                try:
                    data = Daily(punto, start, end).fetch()
                    if not data.empty:
                        print(f"Datos encontrados en ({lat_nueva:.4f}, {lon_nueva:.4f})")
                        return data, (lat_nueva, lon_nueva)
                except Exception as e:
                    continue  # Ignorar errores silenciosamente

        print("No se encontraron datos meteorológicos cercanos.")
    return None, None, None, None