'''
File : getCoordinate.py
Author : Mochamad Teguh Subarkah

Description :
getCoordinate.py is extracting latitude and longitude value from xml file
The function getCoordinate(xml_file) receive xml_file name 

'''

#Import Library
import xml.etree.ElementTree as ET
foundStatus = 0
def getCoordinate(xml_file):
	checkFileType = '.xml'

	
	if type(xml_file) not in [str]:
		raise TypeError("The file must be in string")
		if checkFileType not in xml_file:
			raise TypeError("The file must be in xml")

	
	tree = ET.parse(xml_file)
	root = tree.getroot()

	foundStatus = (tree.find('.//{http://maps.yandex.ru/geocoder/1.x}found').text)
	
	if foundStatus != 0:
		lon = (tree.find('.//{http://www.opengis.net/gml}pos').text).split(' ')[0] #get longitude position
		lat = (tree.find('.//{http://www.opengis.net/gml}pos').text).split(' ')[1] #get latitude position
		return [float(lon),float(lat)]
	else:
		return 0