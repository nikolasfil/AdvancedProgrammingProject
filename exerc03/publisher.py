from flask import Flask, request
import paho.mqtt.client as mqtt
import time


app = Flask(__name__)


@app.route("/receive", methods=["POST"])
def receive_message():
    messagePost = request.get_data(as_text=True)
    messagePost = messagePost.replace("text=", "")
    print(f"Received message: {messagePost}")

    client = SimpleMqttClient(messagePost)

    return "Message received"


class SimpleMqttClient:
    def __init__(self,messagePost):
        self.messagePost = messagePost
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.connected = False
        self.run_client()


    def on_connect(self, client, userdata, flags, rc):
        if rc ==0 :
            self.connected = True
            print("Connected with result code " + str(rc))
        else:
            print('error')

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def on_publish(self, client, userdata, mid):
        if self.connected:
            print("mid: " + str(mid))
            client.disconnect()

    def publish_message(self,topic,message):
        self.client.publish(topic, message)

    def connect(self,broker_url):
        self.client.connect(broker_url,1883,60)
        self.client.loop_start()


    def run_client(self):
        self.connect("test.mosquitto.org")
        topic = "grupatras/lab/engine/up1072754"
        self.publish_message(topic,self.messagePost)

        while self.connected:
            time.sleep(1)


if __name__ == "__main__":
    app.run()
