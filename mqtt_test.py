
# class Mqqt:
#     def __init__(self, client, host, port, timeout, user, passwd):
#         self._client_id = client
#         self._host = host
#         self._port = port
#         self._timeout = timeout
#         self._user = user
#         self._passwd = passwd


#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import sys
import time


class MyMQTTClass(mqtt.Client):
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))
        if rc == 0:
            self.connected_flag = True
            print("Connected Ok")
        else:
            print('Bad Connection')
            self.loop_stop()

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def publish_message(self, topic, payload):
        # print('publish a new message')
        rc = self.publish(topic, payload)
        print('publish a new message', str(rc))

    def run(self):
        self.connected_flag = False
        self.username_pw_set('test', 'test')
        try:
            self.connect("13.127.168.220", 1883, 60)
        except:
            print(" cant't connect")
            sys.exit(1)
        # self.connect("localhost", 1883, 60)
        # self.connect("broker.hivemq.com", 1883, 60)
        # self.subscribe("$SYS/#", 0)
        # self.subscribe("onlineusers", 0)
        # rc = 0
        # while rc == 0:
        #     print('rc status ', rc)
        #     rc = self.loop()
        # return rc
        self.loop_start()
        while not self.connected_flag:
            print(' in waiting loop')
            time.sleep(1)


# If you want to use a specific client id, use
# mqttc = MyMQTTClass("23213123123")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = MyMQTTClass()
mqttc.run()
