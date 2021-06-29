'''
File : measureDistance.py
Author : Mochamad Teguh Subarkah

Description :
measureDistance.py is calculating distance between 2 point of latitude and longitude. Point 1 is located in 
Moscow Ring Road, with specified point is
- latitude : 55.766557
- longitude : 37.623429

The function measureDistance(lat,lon) receive lat and lon from another function, which is getCoordinate()

'''

#Import math library, for calculation purpose
from math import sin, cos, sqrt, atan2, radians

#define Moscow Ring Road Latitude and Longitude
MOSCOW_RING_ROAD_Latitude = 55.766557
MOSCOW_RING_ROAD_Longitude = 37.623429

def measureDistance(lat,lon):

	if type(lat) not in [int,float] and type(lon) not in [int,float] :
		raise TypeError("The latitude and longitude must be in float or int number")
	
	R = 6373.0

	#Turn position lat and lon into radians
	lat1 = radians(lat)
	lon1 = radians(lon)
	lat2 = radians(MOSCOW_RING_ROAD_Latitude)
	lon2 = radians(MOSCOW_RING_ROAD_Longitude)

	dlon = (lon2 - lon1)
	dlat = (lat2 - lat1)
	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
	
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	return  round(R * c, 2)

