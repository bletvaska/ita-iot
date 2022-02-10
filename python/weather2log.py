import json
from datetime import datetime
from time import sleep

from sense_emu import SenseHat
import paho.mqtt.client as mqtt

# create sensehat object
sense = SenseHat()

while True:
    # get data from sense hat
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    press = sense.get_pressure()

    # log
    now = datetime.now()
    print(f'{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}:{now.second};{temp:.2f};{hum:.2f};{press:.0f}')

    sleep(1)

client = mqtt.Client()
client.connect('broker.hivemq.com', port=1883)

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