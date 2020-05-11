import asyncio
import websockets
import cv2
import json
import numpy as np
import base64

# Images to be shown
database = {
    1: cv2.imread('Images/iron_man.jpg'),
    2: cv2.imread('Images/terminator.jpg'),
    3: cv2.imread('Images/lamborghini.jpg'),
    4: cv2.imread('Images/atlas.jpg'),
    5: cv2.imread('Images/kinova.jpeg')
}

# JSON object to be sent
payload = {
    'image': "",
    'shape': []
}

# The function that will prepare the data and send it!
def state_event(frame):
    shape = frame.shape
    frame = cv2.imencode('.JPEG', frame)[1]
    encoded_image = base64.b64encode(frame)

    # Fill the object
    payload['image'] = encoded_image.decode('utf-8')
    payload['shape'] = shape

    return json.dumps(payload)

# Function to cv2.imread() image
def get_image(index):
    frame = database[index]
    return frame

# The overall function
async def send_image(websocket, path):
    while True:
        index = input('Enter image index: ')
        frame = get_image(int(index))

        await websocket.send(state_event(frame))

        async for message in websocket:
            print(message)
            break

start_server = websockets.serve(send_image, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


    








