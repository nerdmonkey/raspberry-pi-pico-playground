import paho.mqtt.client as mqtt
import time
from config.settings import Settings
import json

class Relay():
    def __init__(self):
        self.broker_url, self.broker_port, self.username, self.password, self.topic, self.client_id = Settings().all()
        self.client = mqtt.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.connect(self.broker_url, self.broker_port, keepalive=60)


    def send(self, message):
        result = self.client.publish(self.topic, message, qos=0)
        time.sleep(0.5)

        return result


    def turn(self, state, value):
        pin = str(value)
        switches = {
            "8": 14,
            "7": 15,
            "6": 16,
            "5": 17,
            "4": 18,
            "3": 19,
            "2": 20,
            "1": 21,
        }

        message = {
            "pin": switches[pin],
            "value": state
        }

        payload = json.dumps(message)

        return self.send(payload)


    def on(self, value):
        return self.turn("on", value)

    def off(self, value):
        return self.turn("off", value)
