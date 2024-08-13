from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from random import randrange, uniform
import paho.mqtt.client as mqtt

thread = None
thread_lock = Lock()

app = Flask(__name__)
app.secret_key = 'your secret here'
socketio = SocketIO(app, cors_allowed_origins='*')
mqtt_client = mqtt.Client()

myG=20

def get_current_datetime():      
    randNumber = randrange(10, 40)
    return randNumber


def background_thread():
    global myG
    print("Generating random sensor values")
    while True:        
        #socketio.emit('updateSensorData', { "date": get_current_datetime()})
        socketio.emit('updateSensorData', { "date": myG})
        socketio.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

@socketio.on('disconnect')
def handle_disconnect():
    socketio.emit('my_response_close', { 'data': 'close' })
    print('Client disconnected')

def on_connect(client, userdata, flags, rc):
    #print(rc)    
    client.subscribe("XXXXX")    
    
def on_message(client, userdata, msg):
    global myG
    myG=msg.payload.decode('utf8')      
    print("TEMPERATURE "+ str(myG))
    

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("XXX.XXX.XXX.XXX", 1883, 60)
mqtt_client.loop_start()
if __name__ == '__main__':
    socketio.run(app, debug=True) 