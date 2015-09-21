#Calculo de distancia entre dos puntos de coordenadas.
#Utiliza latitud y longitud, devolviendo la distancia en metros.
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	r = 6371 # radio tierra en kilometros
	return c * r * 1000
