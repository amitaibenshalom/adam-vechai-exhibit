"""
Filename: camera.py
Author: Amitai Ben Shalom (0559385905)
Description: camera object for the exhibit
"""

import cv2
from consts import CAMERA_INDEX

class Camera:
    """
    Camera object for the exhibit
    """

    def __init__(self):
        """
        Initialize the camera object
        """
        self.cap = cv2.VideoCapture(CAMERA_INDEX)  # initialize the camera

        if not self.cap.isOpened():  # check if camera is found
            print("Camera not found")  # print error message if camera is not found
            self.cap = None

    def take_picture(self, path, save=False):
        """
        Take a picture using the camera and save it in the given path
        :param path: the path to save the picture in
        return: True if the picture was taken, False otherwise (camera not found)
        """
        if self.cap is None:  # check if camera is found
            return False  # camera not found

        ret, frame = self.cap.read()  # take a picture

        if ret and save:
            cv2.imwrite(path, frame)  # save the picture
            # time.sleep(0.1)  # wait for the picture to be saved

        return ret  # return True if the picture was taken, False otherwise
    
