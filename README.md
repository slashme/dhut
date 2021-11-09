## Humidity and temperature measurement

Measuring humidity and temperature with a Raspberry Pi and logging the data on Heroku.

If you find this code or these instructions useful, let me know which parts need to be improved!

## Hardware setup

I did this project with two Raspberry Pi single-board computers, each connected to two DHT22 humidity and temperature detectors. I've also tried out DHT11 sensors, which also worked, but are less precise.

Each DHT22 has its positive terminal connected to a 5V+ pin on the Pi, and its negative to a GND pin. The signal pin was then connected to one of the GPIO pins, in my case, either GPIO 4 or GPIO 18.

## Software setup

The code to get the Raspberry Pi to read data from the sensors is in the directory raspberryscripts. This requires the Pi to have an active internet connection, and of course only works if you have a website set up to receive the data. 

Currently I have the target site hardcoded, but it would be easy to move this to a config file.

You also need to set up the development environment, and install two Python modules, namely pytz (time zone management) and Adafruit-DHT (the package that reads data from the sensors)

```
sudo apt install python3-dev python3-pip
sudo pip3 install pytz
sudo pip3 install Adafruit_DHT
```

You tell the script how many DHT22s or DHT11s you have, which pins they read their data from, and how frequently to read them, by editing the file sensorlist.json .

You can run the script directly on your raspberry pi, but it's more robust to run it as a service that will start when the pi starts, and which you can turn on and off as you need.

First, decide where you want to keep the script that reads the sensors, and edit the line starting with ExecStart in the file dhttest.service accordingly, and then /lib/systemd/system/ on the raspberry pi. I've also hardcoded the location of the config file (sensorlist.json) in dhttest.py - change the line that starts with "with open" to point at the right place. In the unlikely event that anyone ever uses this code and these instructions, please do send me a pull request where you fix this ugliness.

Once you've moved the script into the right place and created the service file, you have to make it active:

```
sudo chmod 644 /lib/systemd/system/dhttest.service
sudo systemctl daemon-reload
sudo systemctl enable dhttest.service
sudo systemctl start dhttest.service
```

Then you will be able to start stop and restart the script by doing:

```
sudo service dhttest start
sudo service dhttest stop
sudo service dhttest restart
```
