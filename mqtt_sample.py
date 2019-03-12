# import paho.mqtt.client as paho
import time
# import paho.mqtt.client as mqtt


# class Mqtt(mqtt.Client):
#     def __init__(self):
#         # self.client = paho.Client()
#         self.on_publish = self.on_publish
#         self.on_message = self.on_message
#         self.connect('broker.mqttdashboard.com', 1883)
#         self.subscribe('encyclopedia/#', qos=1)
#         self.loop_start()

#         while True:
#             temperature = 1
#             (rc, mid) = self.publish(
#                 'encyclopedia/temperature', str(temperature), qos=1)
#             time.sleep(1)

#     def on_publish(self, client, userdata, mid):
#         print("mid: "+str(mid))

#     def on_message(self, client, userdata, msg):
#         print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


# Mqtt()

import paho.mqtt.client as mqtt


class MyMQTTClass(mqtt.Client):
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    # def on_log(self, mqttc, obj, level, string):
    #     print(string)

    def publish_message(self, topic, payload):
        # print('publish a new message')
        rc = self.publish(topic, payload)
        print('publish a new message', str(rc))

    def run(self):
        self.username_pw_set('test', 'test')
        self.connect("13.127.168.220", 1883, 60)
        self.subscribe("onlineusers", 0)
        # self.loop_start()
        # while True:
        #     temperature = 1
        #     (rc, mid) = self.publish(
        #         'encyclopedia/temperature', str(temperature), qos=1)
        #     time.sleep(1)
        rc = 0
        while rc == 0:
            rc = self.loop()
        print('TEST')
        return rc


mqttc = MyMQTTClass()
rc = mqttc.run()
