import json

import requests
import paho.mqtt.client as mqtt

appid = '08f5d8fd385c443eeff6608c643e0bc5'
city = 'Košice,sk'
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={appid}'

# download data
response = requests.get(url.format(appid=appid, city=city))

# extract data
data = response.json()
temp = data['main']['temp']
hum = data['main']['humidity']
press = data['main']['pressure']

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
    "temperature": f"{temp}°C",
    "humidity": f"{hum}%",
    "pressure": f"{press}hPa"
}

client.publish('ita/meteoservis/mirek', json.dumps(data, ensure_ascii=False))