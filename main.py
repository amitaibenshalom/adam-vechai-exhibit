"""
Filename: main.py
Author: Amitai Ben Shalom (0559385905)
Description: main file for the exhibit - run this
"""

import os, pygame, time
from consts import *
import datetime as dt
from camera import Camera
from picture_loader import PictureLoader

def main():
    
    pygame.init()  # initialize pygame
    clock = pygame.time.Clock()  # create a clock object

    if RUN_ON_FULLSCREEN:  # check if fullscreen mode is enabled
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # run in fullscreen mode

    else:
        print(SCREEN_SIZE)
        screen = pygame.display.set_mode(SCREEN_SIZE)  # use the screen size from the consts file

    pygame.display.set_caption("Exhibit")  # set the caption

    camera = Camera()  # create the camera object
    pictureLoader = PictureLoader(screen, PICTURES_FOLDER, PICTURE_DURATION)  # create the picture loader object

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:  # if the user pressed the exit button (X on the window)
                print("Exiting...")
                pygame.quit()
                return  # exit the program

            if event.type == KEYDOWN:
                if event.key == EXIT_KEY:  # if the user pressed the exit key (ESC)
                    print("Exiting...")
                    pygame.quit()
                    return  # exit the program
                
                if event.key == TAKE_PICTURE_KEY:  # if the user pressed the take picture key (0), this is equivalent to the button press
                    time_stamp = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # get the current time stamp (year-month-day-hour-minute-second)
                    picture_path = os.path.join(PICTURES_FOLDER, f"{time_stamp}.png")  # create the picture path
                    ret = camera.take_picture(picture_path, save=True)  # take the picture and save it

                    if not ret:  # check if the picture was taken
                        print("Error taking picture")
                        pictureLoader.camera_error = True  # set the camera error flag - picture was not taken
                    
                    pictureLoader.last_picture_time = time.time()  # update the last picture time
                    pictureLoader.picture_index = 0  # reset the picture index if needed

        camera.take_picture(PICTURES_FOLDER, save=False)  # take a picture but do not save it (must do this to clear the buffer of the camera)
        pictureLoader.display_picture()  # display the picture on the screen based on the current mode (idle or not)
        pygame.display.update()  # actually update the display
        clock.tick(60)  # limit the frame rate to 60 FPS


if __name__ == "__main__":
    main()  # run the main function