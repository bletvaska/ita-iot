from time import sleep
from machine import Pin, unique_id
from dht import DHT22
from umqtt.robust import MQTTClient

import config


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

# connect to wifi
do_connect(config.ESSID, config.PASSWORD)

# connect to MQTT
mqtt = MQTTClient(unique_id(), config.MQTT_BROKER)
mqtt.connect()

# sensors/actuators initialization
led = Pin(18, Pin.OUT)
sensor = DHT22(Pin(14))

# main loop
while True:
  led.on()
  sensor.measure()
  temp = sensor.temperature()
  hum = sensor.humidity()
  message = f'{temp:.2}C {hum:.2}%'
  print(message)
  mqtt.publish(MQTT_TOPIC, message)
  led.off()
  sleep(10)
  break
