import json

from sense_emu import SenseHat
import paho.mqtt.client as mqtt

# create sensehat object
sense = SenseHat()

# get data from sense hat
temp = sense.get_temperature()
hum = sense.get_humidity()
press = sense.get_pressure()

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
    "temperature": f"{temp}°C",
    "humidity": f"{hum}%",
    "pressure": f"{press}hPa"
}

client.publish('ita/meteoservis/mirek', json.dumps(data, ensure_ascii=False))