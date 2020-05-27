import cv2
import threading

# Hardware Abstraction Layer
# ROS Driver Control coming here soon!!
class HAL:
    # Explicit initialization functions
    # Class method, so user can call it without instantiation
    @classmethod
    def initRobot(self):
        pass

    # Get Image using OpenCV functions
    def getImage(self, index):
        if(index == 1):
            img = cv2.imread('terminator.jpg')
        else:
            img = cv2.imread('lamborghini.jpg')
        return img