from dotenv import load_dotenv
import os
import uuid

load_dotenv(".env")

broker_url = os.getenv('MQTT_BROKER_URL')
broker_port = int(os.getenv('MQTT_BROKER_PORT', 1883))
username = os.getenv('MQTT_USERNAME')
password = os.getenv('MQTT_PASSWORD')
topic = os.getenv('MQTT_TOPIC')


class Settings():
    def __init__(self):
        self.broker_url = broker_url
        self.broker_port = broker_port
        self.username = username
        self.password = password
        self.topic = topic
        self.client_id = str(uuid.uuid4())


    def all(self):
        return self.broker_url, self.broker_port, self.username, self.password, self.topic, self.client_id
