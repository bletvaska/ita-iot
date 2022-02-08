import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('broker.hivemq.com', port=1883)

data = {
    "name": "mirek",
    "lat": 48.730892,
    "lon": 21.245767,
    "iconColor": "#0000ff",
    "icon": "home",
    "ttl": 30,
    "photoUrl": "https://bletvaska.github.io/images/mirek.na.hackathone.jpg",
    "weblink": {
        "name": "homepage",
        "url": "https://bletvaska.github.io/",
        "target": "_new"
    },
    "label": "mirek from Mu",
    "temp": "3.8°C",
    "hum": "56%"
}

client.publish('ita/meteoservis/mirek', json.dumps(data, ensure_ascii=False))