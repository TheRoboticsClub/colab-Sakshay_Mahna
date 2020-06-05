import rospy
import cv2
import threading
import time
from datetime import datetime

from interfaces.camera import ListenerCamera

# Hardware Abstraction Layer
class HAL:
    IMG_WIDTH = 320
    IMG_HEIGHT = 240
    
    def __init__(self):
    	rospy.init_node("HAL")
    
    	self.image = None
    	self.camera = ListenerCamera("/TurtlebotROS/cameraL/image_raw")
    	self.camera_lock = threading.Lock()
    	
    # Explicit initialization functions
    # Class method, so user can call it without instantiation
    @classmethod
    def initRobot(self):
        pass
    
    # Get Image from ROS Driver Camera
    def getImage(self):
        self.camera_lock.acquire()
        self.image = self.camera.getImage().data
        self.camera_lock.release()
        
        return self.image
