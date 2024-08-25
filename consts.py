"""
Filename: consts.py
Author: Amitai Ben Shalom (0559385905)
Description: Constants file for the exhibit
"""

import pygame
from pygame.locals import *

# pictures related settings
MAX_PICTURES = 10  # number of pictures that will be displayed in idle mode
PICTURES_FOLDER = "/home/dell/pictures"  # folder where the pictures are saved
PICTURE_DURATION = 1  # seconds per picture in idle mode
CAMERA_INDEX = 0  # camera index to use (0 is the default camera) (if not working, try 0, 1, 2, 3)

# idle mode settings
IDLE_TIME = 4  # seconds until idle mode (cycle through pictures)

# screen settings
RUN_ON_FULLSCREEN = True  # run in fullscreen mode
SCREEN_SIZE = (1920, 1080)  # screen size - if run_on_fullscreen is True, THIS WILL BE IGNORED

# keys settings
TAKE_PICTURE_KEY = pygame.K_0  # key to take a picture (0) - DO NOT CHANGE
EXIT_KEY = pygame.K_ESCAPE  # key to exit the program (ESC)

# error settings
DEFAULT_PICTURE = "/home/dell/adam-vechai-exhibit/default/error.png"  # picture to display when no pictures are found
CAMERA_ERROR = "/home/dell/adam-vechai-exhibit/default/camera_error.png"  # picture to display when camera is not found
