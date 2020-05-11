#!/usr/bin/env python

import asyncio
import websockets
import math
import cv2
import time
import traceback

# Function that executes source_code using exec()
def execute_code(source_code):
    try:
        execution = exec(source_code, {'math': math, 'cv2':cv2, 'time':time})
        if execution != None:
            print(execution)
    except Exception:
        traceback.print_exc()

# The websocket function
async def get_code(websocket, path):
    try:
        async for message in websocket:
            code = message
            # print(code)
            execute_code(code)
    except:
        pass

start_server = websockets.serve(get_code, "127.0.0.1", 6789)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()