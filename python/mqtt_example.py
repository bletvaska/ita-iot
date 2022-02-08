import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('broker.hivemq.com', port=1883)

client.publish('ita/messages', 'hello world (mirek)')