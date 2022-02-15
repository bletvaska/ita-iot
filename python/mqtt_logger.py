import json
from datetime import datetime
from time import sleep

import paho.mqtt.client as mqtt

def on_message_received(client, xxx, message):
    data = message.payload.decode()
    print(message.topic, data)

# connect to mqtt broker
client = mqtt.Client()
client.connect('broker.hivemq.com', port=1883)
client.on_message = on_message_received
client.subscribe('ita/meteoservis/#')

# pocuvaj donekonecna (a este dalej)
client.loop_forever()
