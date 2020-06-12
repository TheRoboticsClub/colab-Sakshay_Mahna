#!/usr/bin/env python

from websocket_server import WebsocketServer
import logging
import time
import threading
from datetime import datetime
import re
import traceback

import gui
import hal

class Template:
    # Initialize class variables
    # self.time_cycle to run an execution for atleast 1 second
    # self.process for the current running process
    def __init__(self):
        self.thread = None
        self.reload = False
        self.time_cycle = 80

        # Initialize the GUI and HAL behind the scenes
        self.gui = gui.GUI()
        self.hal = hal.HAL()

    # Function to parse the code
    # A few assumptions: 
    # 1. The user always passes sequential and iterative codes
    # 2. Only a single infinite loop
    def parse_code(self, source_code):
    	# Get the debug level and strip the debug part
    	debug_level = int(source_code[5])
    	source_code = source_code[5:]
    	
    	source_code = self.debug_parse(source_code, debug_level)
    	sequential_code, iterative_code = self.seperate_seq_iter(source_code)
        

        return iterative_code, sequential_code, debug_level
        
    # Function to parse code according to the debugging level
    def debug_parse(self, source_code, debug_level):
    	if(debug_level == 0):
    		# If debug level is 0, then all the GUI operations should not be called
    		source_code = re.sub(r'GUI\..*', '', source_code)
    		
    	return source_code
    
    # Function to seperate the iterative and sequential code
    def seperate_seq_iter(self, source_code):
    	if source_code == "":
            return "", ""

        # Search for an instance of while True
        infinite_loop = re.search(r'[^ \t]while\(True\):|[^ \t]while True:', source_code)

        # Seperate the content inside while True and the other
        # (Seperating the sequential and iterative part!)
        try:
            start_index = infinite_loop.start()
            iterative_code = source_code[start_index:]
            sequential_code = source_code[:start_index]

            # Remove while True: syntax from the code
            # And remove the the 4 spaces indentation before each command
            iterative_code = re.sub(r'[^ ]while\(True\):|[^ ]while True:', '', iterative_code)
            iterative_code = re.sub(r'^[ ]{4}', '', iterative_code, flags=re.M)

        except:
            sequential_code = source_code
            iterative_code = ""
            
        return sequential_code, iterative_code


    # The process function
    def process_code(self, source_code):
        # Reference Environment for the exec() function
        reference_environment = {'GUI': self.gui, 'HAL': self.hal}
        iterative_code, sequential_code, debug_level = self.parse_code(source_code)
        
        # print("The debug level is " + str(debug_level)
        # print(sequential_code)
        # print(iterative_code)
        
        # Whatever the code is, first step is to just stop!
        self.hal.motors.sendV(0)

        try:
            # The Python exec function
            # Run the sequential part
            exec(sequential_code, {"gui": gui, "hal": hal, "time": time}, reference_environment)

            # Run the iterative part inside template
            # and keep the check for flag
            while self.reload == False:
                start_time = datetime.now()
                
                # A few changes in the reference environment, to
                # allow usage of the initialized API
                reference_environment["GUI"] = self.gui
                reference_environment["HAL"] = self.hal
                # Execute the iterative portion
                exec(iterative_code, reference_environment)

                # Template specifics to run!
                finish_time = datetime.now()
                dt = start_time - finish_time
                ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0

                if(ms < self.time_cycle):
                    time.sleep((self.time_cycle - ms) / 1000.0)

            # self.thread.join()
            print("Current Thread Joined!")

        # To print the errors that the user submitted through the Javascript editor (ACE)
        except Exception:
            traceback.print_exc()
    
    # Function to maintain thread execution
    def execute_thread(self, source_code):
        # Keep checking until the thread is alive
        # The thread will die when the coming iteration reads the flag
        if(self.thread != None):
            while self.thread.is_alive():
                pass

        # Turn the flag down, the iteration has successfully stopped!
        self.reload = False
        # New thread execution
        self.thread = threading.Thread(target=self.process_code, args=[source_code])
        self.thread.start()
        print("New Thread Started!")

    # The websocket function
    # Gets called when there is an incoming message from the client
    def handle(self, client, server, message):
        try:
            # Once received turn the reload flag up and send it to execute_thread function
            code = message
            # print(repr(code))
            self.reload = True
            self.execute_thread(code)
        except:
            pass

    # Function that gets called when the server is connected
    def connected(self, client, server):
    	print(client, 'connected')
    	
    # Function that gets called when the connected closes
    def handle_close(self, client, server):
    	print(client, 'closed')
    	
    def run_server(self):
    	server = WebsocketServer(port=1905, host="127.0.0.1")
    	server.set_fn_new_client(self.connected)
    	server.set_fn_client_left(self.handle_close)
    	server.set_fn_message_received(self.handle)
    	server.run_forever()
    

# Execute!
if __name__ == "__main__":
    server = Template()
    server.run_server()
