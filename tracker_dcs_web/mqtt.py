import os
import paho.mqtt.client as mqtt
from tracker_dcs_web.utils.logger import logger


mqtt_host = os.environ["MQTT_HOST"]

def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    logger.info(f"connected to mqtt broker: {mqtt_host}")


client = mqtt.Client()
client.on_connect = on_connect
client.connect(mqtt_host, 1883, 60)

