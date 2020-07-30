# Yet another boot.py for Micropython
#
# the external file "wifi.json" should state the ssid and password.
# Sample "wifi.json": {"ssid":"someSSID","password":"somePASSWORD"}  
#
# Missing wifi.json => no wifi connection
#
import gc
import time
import json
import network
import esp
from machine import Pin

esp.osdebug(None) # for esp8266 retro compat
gc.enable()

LEDPIN = 2 # Adjust to your board
WIFI_CONFIGFILE = "wifi.json"
led = Pin(LEDPIN, Pin.OUT)

def successBlink():
    for i in range(0, 6):
        led.value(i % 2 == 0)
        time.sleep_ms(60)

def connectToWifi():

    print("Connecting to wifi...")

    try:
        with open(WIFI_CONFIGFILE) as f:
            data = json.load(f)

        ssid = data.get("ssid")
        password = data.get("password")

        wifiClient = network.WLAN(network.STA_IF)
        wifiClient.active(True)
        wifiClient.connect(ssid, password)

        while not wifiClient.isconnected():
            pass

        ipaddress = wifiClient.ifconfig()[0]
        netmask = wifiClient.ifconfig()[1]
        gateway = wifiClient.ifconfig()[2]
        dns = wifiClient.ifconfig()[3]

        print('Connection to WiFi successful:\n\taddress: {}\n\tnetmask: {}\n\tgateway: {}\n\tdns: {}\n'.format(ipaddress, netmask, gateway, dns))
        successBlink()

    except Exception as ex:
        print(3 * "Error connecting to Wifi: {}\n".format(str(ex)))

connectToWifi()


