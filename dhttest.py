import Adafruit_DHT
import time
import datetime
import urllib.request
import glob
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperature = read_temp()
    if humidity is not None and temperature is not None:
        a=datetime.datetime.now()
        blah=urllib.request.urlopen('https://dhut.herokuapp.com/add?when={}-{}-{}%20{}%3a{}%3a{}.{}&temp={}&rh={}'.format(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond, temperature, humidity))
        #print('http://localhost:5000/add?when={}-{}-{}%20{}%3a{}%3a{}.{}&temp={}&rh={}'.format(a.year, a.month, a.day, a.hour, a.minute, a.second, a.microsecond, temperature, humidity))
        print(temperature,humidity)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(60)
