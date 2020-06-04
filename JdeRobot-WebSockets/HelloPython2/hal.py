import cv2
import threading
import time
from datetime import datetime

from interfaces.camera import ListenerCamera

# Hardware Abstraction Layer
class HAL(threading.Thread):
    IMG_WIDTH = 320
    IMG_HEIGHT = 240
    
    def __init__(self):
    	super(HAL, self).__init__(name="HALThread")
    
    	self.time_cycle = 50
    	self.image = None
    	self.camera = ListenerCamera("/F1ROS/cameraL/image_raw")
    	
    # Explicit initialization functions
    # Class method, so user can call it without instantiation
    @classmethod
    def initRobot(self):
        pass

    def run(self):
    	while True:
    		start_time = datetime.now()
    		self.camera.start()
    		self.image = self.camera.getImage().data
    		
    		finish_time = datetime.now()
    		
    		dt = finish_time - start_time
    		ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    		
    		if ms < self.time_cycle:
    			time.sleep((self.time_cycle - ms) / 1000.0)  
    		
    
    # Get Image from ROS Driver Camera
    def getImage(self):
        return self.image
