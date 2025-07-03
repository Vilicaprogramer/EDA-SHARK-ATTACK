import pandas as pd
import numpy as np
import requests
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from datetime import datetime, timedelta
from meteostat import Point, Daily


def geo_point(row, area, pais):
    area = row[area]
    pais = row[pais]
    geolocator = Nominatim(user_agent="geoapi")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geocode(area + ',' + pais)
    if location == None:
        return location
    else:
        lat = location.latitude
        lon = location.longitude

    return lat, lon
