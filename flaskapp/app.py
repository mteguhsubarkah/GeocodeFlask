'''
File : app.py
Author : Mochamad Teguh Subarkah
Description :
app.py is the main program of this Geocode app. Its receive input from user, which is a location,
then app.py will pass the location in HTTP requests to get the xml file. And last, calculate the distance between Moscow Ring Road 
and specified location

Position point is extracted by getCoordinate.py, so the file is imported here and
Distance is calculated by measureDistance.py, which also imported here

This program is loged into 'geocodeflask.log'
'''

#import Library
from flask import Flask, url_for, render_template, request, redirect, jsonify  
import logging
import requests
import xml.etree.ElementTree as ET
import measureDistance as mD
import getCoordinate as getCoor


app = Flask(__name__)

#Define logger
logging.basicConfig(filename='geocodeFlask.log',
level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#API key for http requests, got from yandex API
API_KEY = '8bfc2849-a789-4584-bd57-04f0e286fe5e'

@app.route('/', methods=["POST", "GET"])
def index():
    #Pass Location in HTTP Requests
    if request.method == "POST":
        location = request.form["location"]
        ploads = {
        'apikey' :API_KEY,
        'geocode':location
        }
        response = requests.get('https://geocode-maps.yandex.ru/1.x/?', ploads)
        with open('data.xml', 'wb') as f:
            f.write(response.content)
    else: 
        location=""

    
     #Get position point of the input location
    position = getCoor.getCoordinate("data.xml")

 
    #If the specified location is "MKAD", the system will not calculating
    if (location == "MKAD"):
        distance = 0
    else:
        distance = mD.measureDistance((position[1]),(position[0]))
    

    app.logger.info('Info level log')

    #Return the value of specified location and distance into front-end level, in indec.html
    return render_template("index.html", inputLocation = location, measuredDistance = distance)

if __name__ == "__main__":
    app.run(debug=True)
