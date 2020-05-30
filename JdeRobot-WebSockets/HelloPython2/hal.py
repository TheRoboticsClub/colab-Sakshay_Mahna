import cv2
import threading

from interfaces.camera import ListenerCamera

# Hardware Abstraction Layer
class HAL:
    IMG_WIDTH = 320
    IMG_HEIGHT = 240
    
    def __init__(self):
    	self.initiate_camera_thread() 
    	
    # Explicit initialization functions
    # Class method, so user can call it without instantiation
    @classmethod
    def initRobot(self):
        pass

    def initiate_camera_thread(self):
    	self.camera = ListenerCamera("/F1ROS/cameraL/image_raw")
    	self.camera_thread = threading.Thread(self.camera.start())
    	self.camera_thread.start()
    
    # Get Image from ROS Driver Camera
    def getImage(self):
        img = self.camera.getImage().data
        img = cv2.resize(img, (self.IMG_WIDTH, self.IMG_HEIGHT))
        return img
