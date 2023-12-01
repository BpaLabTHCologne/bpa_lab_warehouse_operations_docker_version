import paho.mqtt.client as mqtt
import json
from domain import HighbayDomain
import sys

# Functions for MQTT
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Warehouse_Operations/start")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # Load the received message
    message = json.loads(msg.payload)

    # Perform the task based on the function parameter (Test version: robot action are commented for testing without robot)
    if message['function'] == 'fetch_bicycle_from_shelf': 
        print("Bicycle fetched from shelf!")

    elif message['function'] == 'move_bicycle_to_dock': 
        print ("Bicycle moved to dock!")

    elif message['function'] == 'pick_bicycle':
        print("Bicycle picked up!")

    elif message['function'] == 'store_bicycle_to_shelf':
        print("Bicycle stored to shelf!")

    # Response that is sent once the task is executed
    completed_message = {
    'function': message['function'],
    'place_id': message['place_id'],
    'task_type': 'completed'
    }

    # Send the response that the task is completed
    client.publish('Warehouse_Operations/ready', json.dumps(completed_message))


# MQTT client is started and waits for message from the workers
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if client.connect("mqtt-broker", 1883, 60) != 0:
    print("Could not establish connection with the MQTT broker!")
    sys.exit(-1)

# Block the network loop to keep the script running
client.loop_forever()
