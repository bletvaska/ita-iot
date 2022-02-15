import json
from datetime import datetime
from time import sleep

import paho.mqtt.client as mqtt

def on_message_received(client, xxx, message):
    try:
        # decode data from message
        data = json.loads(message.payload.decode())

        # extract data
        name = data['name']
        temp = float(data['temperature'])
        hum = float(data['humidity'])
        press = float(data['pressure'])

        # prepare log message
        now = datetime.now()
        log = f'{now.strftime("%d.%m.%Y %H:%M:%S")};{name};{temp:.2f};{hum:.2f};{press:.0f}'
        print(log)

        # write data to log file
        with open('data.csv', 'a') as file:
            print(log, file=file)

    except Exception as ex:
        print(f'Error: chybny vstup: {ex}')
        print(message.payload)


# connect to mqtt broker
client = mqtt.Client()
client.connect('broker.hivemq.com', port=1883)
client.on_message = on_message_received
client.subscribe('ita/meteoservis/#')

# infinite loop
client.loop_forever()