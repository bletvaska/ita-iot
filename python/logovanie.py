import json
from datetime import datetime
from time import sleep

from sense_emu import SenseHat
import paho.mqtt.client as mqtt

# create sensehat object
sense = SenseHat()

client = mqtt.Client()
client.connect('broker.hivemq.com', port=1883)

while True:
    # get data from sense hat
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    press = sense.get_pressure()

    # log
    now = datetime.now()
    log = f'{now.strftime("%d.%m.%Y %H:%M:%S")};{temp:.2f};{hum:.2f};{press:.0f}'
    print(log)

    # mqtt message
    data = {
        "name": "mirek",
        "lat": 48.730892,
        "lon": 21.245767,
        "iconColor": "#0000ff",
        "icon": "home",
        "ttl": 3 * 60,
        "photoUrl": "https://bletvaska.github.io/images/mirek.na.hackathone.jpg",
        "weblink": {
            "name": "homepage",
            "url": "https://bletvaska.github.io/",
            "target": "_new"
        },
        "label": "mirek from Mu",
        "temperature": f"{temp:.2f}°C",
        "humidity": f"{hum:.2f}%",
        "pressure": f"{press:.0f}hPa"
    }
    client.publish('ita/meteoservis/mirek', json.dumps(data, ensure_ascii=False))

    # write log to file
    with open('data.csv', 'a') as file:
        # file.write(log)
        print(log, file=file)

    sleep(1 * 60)




