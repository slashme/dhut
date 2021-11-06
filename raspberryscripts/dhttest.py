#!/usr/bin/python3
import Adafruit_DHT
import time
import datetime
import pytz
import urllib.request
 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
DHT_sensor = 1

DHT_SENSOR2 = Adafruit_DHT.DHT11
DHT_PIN2 = 18
DHT_sensor2 = 3

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        a=datetime.datetime.now().astimezone(pytz.utc)
        try:
            blah=urllib.request.urlopen('https://dhut.herokuapp.com/add?when={}-{}-{}%20{}%3a{}%3a{}.{}%2B00:00&temp={}&rh={}&sensor={}'.format(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond, temperature, humidity, DHT_sensor))
        except urllib.error.URLError as error:
            print("Error in connection: ", error)
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR2, DHT_PIN2)
    if humidity is not None and temperature is not None:
        a=datetime.datetime.now().astimezone(pytz.utc)
        try:
            blah=urllib.request.urlopen('https://dhut.herokuapp.com/add?when={}-{}-{}%20{}%3a{}%3a{}.{}%2B00:00&temp={}&rh={}&sensor={}'.format(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond, temperature, humidity, DHT_sensor2))
        except urllib.error.URLError as error:
            print("Error in connection: ", error)
    time.sleep(60)
