# Importing print function from Python3 to allow the overrride
from __future__ import print_function

# Class for psuedo cosnole functions
class Console:
	# Initialize the websocket and client
	def __init__(self):
		pass
		
	# Function to set the websocket data
	def set_websocket(self, websocket, client):
		self.server = websocket
		self.client = client
	
	# Function to send text to psuedo console
	def print(self, text):
		message = "#con" + str(text)
		print(text)
		self.server.send_message(self.client, message)

	# Function to read from psuedo console
	def read(self, text):
		pass
		
	
