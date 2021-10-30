import Adafruit_DHT
import time
import datetime
import urllib.request
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        a=datetime.datetime.now()
        blah=urllib.request.urlopen('https://dhut.herokuapp.com/add?when={}-{}-{}%20{}%3a{}%3a{}.{}&temp={}&rh={}'.format(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond, temperature, humidity))
        print(temperature,humidity)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(60)
