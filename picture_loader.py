"""
Filename: picture_loader.py
Author: Amitai Ben Shalom (0559385905)
Description: Picture loader for the exhibit
"""

import os, pygame, time
from pygame.locals import *
from consts import MAX_PICTURES, IDLE_TIME, DEFAULT_PICTURE, CAMERA_ERROR


class PictureLoader:
    """
    Picture loader object for the exhibit
    """

    def __init__(self, screen, pictures_folder, picture_duration):
        """
        Initialize the picture loader object
        :param screen: the screen to display the pictures on
        :param pictures_folder: the folder where the pictures are saved
        :param picture_duration: the duration to display each picture (in idle mode)
        """
        self.screen = screen  # the screen to display the pictures on
        self.pictures_folder = pictures_folder  # the folder where the pictures are saved
        self.picture_duration = picture_duration  # the duration to display each picture (in idle mode)

        self.idle = False  # idle mode
        self.picture_index = 0  # current picture index
        self.last_picture_time = time.time()  # last time a picture was taken
        self.last_idle_picture_time = time.time()  # last time a picture was displayed in idle mode
        self.camera_error = False  # camera error flag

        os.makedirs(self.pictures_folder, exist_ok=True)  # create the pictures folder if it doesn't exist

        if not os.path.exists(DEFAULT_PICTURE):  # check if the default picture exists
            raise FileNotFoundError(f"Default picture not found: {DEFAULT_PICTURE}")
        
        if not os.path.exists(CAMERA_ERROR):  # check if the camera error picture exists
            raise FileNotFoundError(f"Camera error picture not found: {CAMERA_ERROR}")


    def load_latest_picture(self):
        """
        Load the latest picture from the pictures folder
        """
        if not self.check_pictures_folder():  # check if there are any pictures in the folder
            self.load_default_picture()  # load the default picture
            return
        
        pictures = os.listdir(self.pictures_folder)  # get all the pictures in the folder
        pictures.sort()  # sort the pictures by name
        picture_path = os.path.join(self.pictures_folder, pictures[-1])  # get the latest picture
        picture = pygame.image.load(picture_path)  # load the picture
        picture = pygame.transform.scale(picture, self.screen.get_size())  # scale the picture to the screen size
        self.screen.blit(picture, (0, 0))  # display the picture

    
    def load_camera_error(self):
        """
        Load the camera error picture
        """
        picture = pygame.image.load(CAMERA_ERROR)  # load the camera error picture
        picture = pygame.transform.scale(picture, self.screen.get_size())  # scale the picture to the screen size
        self.screen.blit(picture, (0, 0))  # display the camera error picture


    def load_default_picture(self):
        """
        Load the default picture
        """
        picture = pygame.image.load(DEFAULT_PICTURE)  # load the default picture
        picture = pygame.transform.scale(picture, self.screen.get_size())  # scale the picture to the screen size
        self.screen.blit(picture, (0, 0))  # display the default picture


    def display_picture(self):
        """
        Display the picture on the screen based on the current mode (idle or not)
        """
        if not self.check_pictures_folder():  # check if there are any pictures in the folder
            self.load_default_picture()  # load the default picture
            return

        if self.camera_error:  # check if there is a camera error
            self.load_camera_error()  # load the camera error picture
            return
        
        self.check_idle()  # check if the program is in idle mode

        if not self.idle:
            self.load_latest_picture()  # load the latest picture
            return
        
        # idle mode - cycle through pictures
        current_time = time.time()  # get the current time
        pictures = os.listdir(self.pictures_folder)  # get all the pictures in the folder
        pictures.sort()  # sort the pictures by name

        if current_time - self.last_idle_picture_time > self.picture_duration:  # check if it's time to move to the next picture
            self.picture_index += 1  # move to the next picture

            if self.picture_index >= MAX_PICTURES or self.picture_index >= len(pictures):
                self.picture_index = 0  # reset the picture index if needed

            self.last_idle_picture_time = current_time  # update the last idle picture time

        picture_path = os.path.join(self.pictures_folder, pictures[-(self.picture_index + 1)])  # get the picture path
        picture = pygame.image.load(picture_path)  # load the picture
        picture = pygame.transform.scale(picture, self.screen.get_size())  # scale the picture to the screen size
        self.screen.blit(picture, (0, 0))  # display the picture


    def check_idle(self):
        """
        Check if the program needs to be in idle mode and update the idle flag
        """
        current_time = time.time()  # get the current time

        if current_time - self.last_picture_time > IDLE_TIME:  # check if the program needs to go into idle mode
            self.idle = True  # turn on idle mode

        else:
            self.idle = False  # turn off idle mode


    def check_pictures_folder(self):
        """
        Check if there are any pictures in the pictures folder
        return: True if there are pictures, False otherwise
        """
        return len(os.listdir(self.pictures_folder)) > 0  # check if there are any pictures in the folder