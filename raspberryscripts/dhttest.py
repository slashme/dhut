#!/usr/bin/python3
import Adafruit_DHT
import time
import datetime
import pytz
import json
import urllib.request
 
with open('/home/david/sensorlist.json', 'r') as f:
    sensorlist = json.load(f)

while True:
    for sensor in sensorlist:
        humidity, temperature = Adafruit_DHT.read_retry(eval(sensor['model']), sensor['pin'])
        if humidity is not None and temperature is not None:
            a=datetime.datetime.now().astimezone(pytz.utc)
            try:
                blah=urllib.request.urlopen('https://dhut.herokuapp.com/add?when={}-{}-{}%20{}%3a{}%3a{}.{}%2B00:00&temp={}&rh={}&sensor={}'.format(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond, temperature, humidity, sensor['sensor_id']))
            except urllib.error.URLError as error:
                print("Error in connection: ", error)
    time.sleep(60)
