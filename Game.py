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
from itertools import cycle
import pygame  # accesses pygame files
from pygame.locals import *
import sys  # to communicate with windows
import random as rand
from mods import *


# pygame setup - only runs once


loopRate = 30  # sets max speed of main loop
P.init()
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BASEY = SCREENHEIGHT * 0.79


P.display.set_caption("Flappy Bird Game") #creates display name
IMAGES, SOUNDS, HITMASKS = {}, {}, {}

PLAYERS_LIST = (
    #red bird
    ('media/redbird-upflap.png',
     'media/redbird-midflap.png',
     'media/redbird-downflap.png'
    ),
    #blue bird
    ('media/bluebird-upflap.png',
     'media/bluebird-midflap.png',
     'media/bluebird-downflap.png'
    ),
    #yellow bird
    ('media/yellowbird-upflap.png',
     'media/yellowbird-midflap.png',
     'media/yellowbird-downflap.png'
    ),
)

BACKGROUNDS_LIST = (
    'media/background-day.png',
    'media/background-night.png',
)


PIPES_LIST = (
    'media/pipe-green.png',
    'media/pipe-red.png'
)
     

def main():
    print("main Stub")
    global clock, SCREEN
    
    
    clock = pygame.time.Clock()  # creates clock to limit frames per second
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    
    IMAGES['numbers'] = (
        P.image.load('media/0.png').convert_alpha(),
        P.image.load('media/1.png').convert_alpha(),
        P.image.load('media/2.png').convert_alpha(),
        P.image.load('media/3.png').convert_alpha(),
        P.image.load('media/4.png').convert_alpha(),
        P.image.load('media/5.png').convert_alpha(),
        P.image.load('media/6.png').convert_alpha(),
        P.image.load('media/7.png').convert_alpha(),
        P.image.load('media/8.png').convert_alpha(),
        P.image.load('media/9.png').convert_alpha()
    )
    
    IMAGES['message'] = pygame.image.load('media/message.png').convert_alpha()
    IMAGES['base'] = pygame.image.load('media/base.png').convert_alpha()
    IMAGES['gameover'] = pygame.image.load('media/gameover.png').convert_alpha()
        

    
    
    randBg = rand.randint(0, len(BACKGROUNDS_LIST)-1)
    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert_alpha()
        
    randPlayer = rand.randint(0, len(PLAYERS_LIST) - 1)
    IMAGES['player'] = (
        P.image.load(PLAYERS_LIST[randPlayer][0]).convert_alpha(),
        P.image.load(PLAYERS_LIST[randPlayer][1]).convert_alpha(),
        P.image.load(PLAYERS_LIST[randPlayer][2]).convert_alpha(),
    )
        
        
        
        
        
        
        
        
    movementInfo = menuScreen()
    
        
        
    

def menuScreen():
    print("Menu Screen Stub")

    # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                P.quit()
                sys.exit()# causes exit of game loop
            
            # your code starts here #
            if event.type == KEYDOWN and (event.key == K_SPACE): #includes touching screen
                return { }   
            
        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))
        
        
        P.display.update()
        clock.tick(loopRate)
        



def mainGame():
    print("Main Game Stub")
    
        # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                play = False  # causes exit of game loop
            
            # your code starts here #
            if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
                # change this to do something if user clicks mouse
                # or touches screen
                pass 
    
def gameOverScreen(crashInfo):
    print("Game over Screen Stub")
    
    # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

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


    

    



'''# game loop - runs loopRate times a second!
while True:  # game loop - note:  everything in this loop is indented one tab

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
    clock.tick(loopRate)  # limits game to frame per second, FPS value'''
    
if __name__ == '__main__':
    main()


# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window