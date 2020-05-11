#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
    while True:
        message = input("Enter your message: ")
        await websocket.send(message)

        async for message in websocket:
            print(message)
            break

start_server = websockets.serve(hello, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()