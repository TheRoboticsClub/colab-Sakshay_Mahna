import json
import cv2
import base64
import threading
import asyncio
import websockets

# Graphical User Interface Class
class GUI():
    # Initialization function
    # The actual initialization
    def __init__(self):
        t = threading.Thread(target=self.run_server)
        t.start()
        self.show = False
        self.payload = {'image': '', 'shape': []}

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

        self.show = True

    # Asynchronous function to keep sending the image to Javascript
    async def send_image(self, websocket, path):
        while True:
            if(self.show == True):
                encode = json.dumps(self.payload)
                await websocket.send(encode)
                self.show = False

    # Activate the server
    def run_server(self):
        # A seperate event loop to run two servers simultaneously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(self.send_image, "127.0.0.1", 2303)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        

