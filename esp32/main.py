from time import sleep
from machine import Pin
from dht import DHT22

def do_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def toggle(led):
  led.value(not led.value())

do_connect('Wokwi-GUEST', '')

led = Pin(18, Pin.OUT)
sensor = DHT22(Pin(14))

# while True:
#   led.on()
#   sensor.measure()
#   temp = sensor.temperature()
#   hum = sensor.humidity()
#   print(f'{temp:.2}C {hum:.2}%')
#   led.off()
#   sleep(10)

