""" Short, one line description of the project ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Zyon Shepherd"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "zyon.shepherd@education.nsw.gov.au"
__status__ = "Alpha"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
import random
from mods import *


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 288, 512   # sets size of screen/window
SCREEN = P.display.set_mode(SCREENSIZE)  # creates window and game screen
P.display.set_caption("Flappy Bird Game") #creates display name
IMAGES, SOUNDS, HITMASKS = {}, {}, {}

# set variables for some colours if you wnat them RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

PLAYERS_LIST = (
    #red bird
    ('media/redbird-upflap.png',
     'media/redbird-midflap.png',
     'media/redbird-downflap.png',
    ),
    #blue bird
    ('media/bluebird-upflap.png',
     'media/bluebird-midflap.png',
     'media/bluebird-downflap.png',
    ),
    #yellow bird
    ('media/yellowbird-upflap.png',
     'media/yellowbird-midflap.png',
     'media/yellowbird-downflap.png',
    ),
)
     

def main():
    print("main Stub")

def menuSreen():
    print("Menu Screen Stub")
    
        # game loop - runs loopRate times a second!
    while play:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                play = False  # causes exit of game loop
            
            # your code starts here #
            if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
                # change this to do something if user clicks mouse
                # or touches screen
                pass 

def mainGame():
    print("Main Game Stub")
    
        # game loop - runs loopRate times a second!
    while play:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                play = False  # causes exit of game loop
            
            # your code starts here #
            if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
                # change this to do something if user clicks mouse
                # or touches screen
                pass 
    
def gameOverScreen():
    print("Game over Screen Stub")
    
        # game loop - runs loopRate times a second!
    while play:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                play = False  # causes exit of game loop
            
            # your code starts here #
            if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
                # change this to do something if user clicks mouse
                # or touches screen
                pass 
    
def getRandomPipe():
    print("Random Pipe Stub")
    
def showSore():
    print("SHow Score Stub")
    
def checkCrash():
    print("Check crash Stub")
    
def pixelCollision():
    print("pixel Collision Stub")
    
def getHitMask():
    print("Get Hit Mask Stub")
    

    

    

play = True  # controls whether to keep playing

# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here #
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            # change this to do something if user clicks mouse
            # or touches screen
            pass 
        


    # your code ends here #
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value
    
if __name__ == '__main__':
    main()


# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window