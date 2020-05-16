#!/usr/bin/env python

import asyncio
import websockets
import time
import multiprocessing
from datetime import datetime
import traceback

class Template:
    # Initialize class variables
    # self.time_cycle to run an execution for atleast 1 second
    # self.process for the current running process
    def __init__(self):
        self.time_cycle = 1000
        self.process = None
        
    # The process function
    def process_function(self, source_code):
        try:
            # The Python exec function
            execution = exec(source_code)
            if execution != None:
                print(execution)

        # To print the errors that the user submitted through the Javascript editor (ACE)
        except Exception:
            traceback.print_exc()


    # Function that handles the process dynamics
    def execute_process(self, source_code):
        # Terminate the process if we have one currently running!
        if(self.process != None):
            self.process.terminate()
            print("Current Process Terminated!")

        # Start a new process as daemon, is the daemon = true (commented)
        # required? It performs the same without that as well!
        self.process = multiprocessing.Process(target=self.process_function, args=(source_code,))
        # self.process.daemon = True
        self.process.start()
        print("New Process Started!")


    # The websocket function
    async def get_code(self, websocket, path):
        try:
            # Wait asynchronously for the message from browser
            # Once received send it to execute_process function
            async for message in websocket:
                code = message
                # print(repr(code))
                self.execute_process(code)
        except:
            pass

    # Function to run the server indefinitely!
    def run_server(self):
        start_server = websockets.serve(self.get_code, "127.0.0.1", 6789)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

# Execute!
if __name__ == "__main__":
    server = Template()
    server.run_server()