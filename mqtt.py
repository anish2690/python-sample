import paho.mqtt.client as paho
import time


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


client = paho.Client()
client.on_publish = on_publish
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883)
client.subscribe('encyclopedia/#', qos=1)
client.loop_start()

while True:
    temperature = 1
    (rc, mid) = client.publish('encyclopedia/temperature', str(temperature), qos=1)
    time.sleep(.5)
