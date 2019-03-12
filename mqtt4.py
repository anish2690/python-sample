# working copy

import paho.mqtt.client as mqtt  # import the client
import time
import sys
keep_alive = 60


class Client:
    def on_disconnect(self, client, userdata, flags, rc=0):
        m = "DisConnected flags"+"result code "+str(rc)+"client_id  "
        print(m)
        client.connected_flag = False

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("connected OK Returned code=", rc)
            client.connected_flag = True  # Flag to indicate success
        else:
            print("Bad connection Returned code=", rc)
            client.bad_connection_flag = True

    def on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def on_message(self, client, userdata, message):
        print("message received  ", str(message.payload.decode("utf-8")))

    def publish_call_back(self):
        print('test acces')
        rc = self.client.publish('testing', 0)
        return rc

    def __init__(self):
        self.client = mqtt.Client("P!")

    def run(self):
        QOS1 = 1
        QOS2 = 0
        CLEAN_SESSION = False
        port = 1883
        broker = "13.127.168.220"  # cloud broker
        # broker="iot.eclipse.org" #use cloud broker

        # client = mqtt.Client("P!")  # create new instance
        # self.client.on_log = self.on_log  # client logging
        mqtt.Client.connected_flag = False  # create flags
        mqtt.Client.bad_connection_flag = False
        mqtt.Client.retry_count = 0
        self.client.on_connect = self.on_connect  # attach function to callback
        self.client.on_disconnect = self.on_disconnect

        run_main = False
        run_flag = True
        while run_flag:
            while not self.client.connected_flag and self.client.retry_count < 3:
                count = 0
                run_main = False
                try:
                    print("connecting ", broker)
                    self.client.username_pw_set('test', 'test')
                    # connect to broker
                    self.client.connect(broker, port, keep_alive)
                    # self.client.subscribe('onlineusers')
                    break  # break from while loop
                except:
                    print("connection attempt failed will retry")
                    self.client.retry_count += 1
                    if self.client.retry_count > 3:
                        run_flag = False
            if not run_main:
                self.client.loop_start()
                while True:
                    if self.client.connected_flag:  # wait for connack
                        self.client.retry_count = 0  # reset counter
                        run_main = True
                        break
                    if count > 6 or self.client.bad_connection_flag:  # don't wait forever
                        self.client.loop_stop()  # stop loop
                        self.client.retry_count += 1
                        if self.client.retry_count > 3:
                            run_flag = False
                        break  # break from while loop

                    time.sleep(1)
                    count += 1
            if run_main:
                try:
                    # Do main loop
                    print("in main loop")  # publish and subscribe here
                    time.sleep(3)
                    # Added try block to catch keyborad interrupt  to break loop so we
                    # don't leave loop thread running.

                except(KeyboardInterrupt):
                    print("keyboard Interrupt so ending")
                    run_flag = False

        print("quitting")
        self.client.disconnect()
        self.client.loop_stop()
        sys.exit()
