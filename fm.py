from internet_connection import is_connected
import threading
import time

from mqtt4 import Client


class FM:
    def __init__(self):
        self._client = Client()
        self._first_com = False
        self.connection()
        while is_connected():
            self._first_com = True
            com_tread = threading.Thread(
                target=self._client.run(), name='mqtt_connect')
            com_tread.start()

    def connection(self):
        threading.Timer(5.0, self.connection).start()
        print(self._client.publish_call_back())


FM()
