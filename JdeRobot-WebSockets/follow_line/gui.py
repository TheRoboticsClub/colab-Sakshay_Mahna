import json
import cv2
import base64
import threading
from websocket_server import WebsocketServer
import logging

# Graphical User Interface Class
class GUI:
    # Initialization function
    # The actual initialization
    def __init__(self, console):
        t = threading.Thread(target=self.run_server)
        self.payload = {'image': '', 'shape': []}
        self.server = None
        self.client = None
        
        # Take the console object to set the same websocket and client
        self.console = console
        t.start()

    # Explicit initialization function
    # Class method, so user can call it without instantiation
    @classmethod
    def initGUI(self):
        # self.payload = {'image': '', 'shape': []}
        pass

    # Function for student to call
    # Encodes the image as a JSON string and sends through the WS
    def showImage(self, image):
        shape = image.shape
        frame = cv2.imencode('.JPEG', image)[1]
        encoded_image = base64.b64encode(frame)

        self.payload['image'] = encoded_image.decode('utf-8')
        self.payload['shape'] = shape
        
        message = "#img" + json.dumps(self.payload) 

        self.server.send_message(self.client, message)

    # Function to get the client
    # Called when a new client is received
    def get_client(self, client, server):
    	self.client = client
        self.console.set_websocket(self.server, self.client)
    
    # Activate the server
    def run_server(self):
        self.server = WebsocketServer(port=2303, host="127.0.0.1")
        self.server.set_fn_new_client(self.get_client)
        self.server.set_fn_message_received(self.console.prompt)
        self.server.run_forever()
        

