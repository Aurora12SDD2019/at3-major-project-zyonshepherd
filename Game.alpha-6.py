""" Short, one line description of the project ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Zyon Shepherd"
__license__ = "GPL"
__version__ = "0.0.6"
__email__ = "zyon.shepherd@education.nsw.gov.au"
__status__ = "Alpha"


'''revision notes:
06 fixed pipe error (caused by copying and pasting my code) making it now printing out pipes on the top and bottom, also made pipes delete
when they went off the screen allowing for more to be created, also made playerx and playery values so it could be printed to the screen
05 worked through creating the pipes blit to the screen (used some of the values from other code sourcces so it has the same flow as the
normal flappy bird)
04 created ways to access the help screen which shows how to play the game and high score screen which doesn't do much
03 created menu screen and also setup help screen stub and highscore stub which are called if speific numbers are pressed
02 worked through menuSCreen function and blitted the background to the screen
01 created all the functions and also imported most of the sprites
'''

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
PIPEGAPSIZE = 100


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
    
    IMAGES['menu'] = pygame.image.load('media/menu.png').convert_alpha()
    IMAGES['base'] = pygame.image.load('media/base.png').convert_alpha()
    IMAGES['help'] = pygame.image.load('media/help.png').convert_alpha()
    IMAGES['gameover'] = pygame.image.load('media/gameover.png').convert_alpha()
        

    
    
    randBg = rand.randint(0, len(BACKGROUNDS_LIST)-1)
    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert_alpha()
        
    randPlayer = rand.randint(0, len(PLAYERS_LIST) - 1)
    IMAGES['player'] = (
        P.image.load(PLAYERS_LIST[randPlayer][0]).convert_alpha(),
        P.image.load(PLAYERS_LIST[randPlayer][1]).convert_alpha(),
        P.image.load(PLAYERS_LIST[randPlayer][2]).convert_alpha(),
    )
    
    pipeIndex = rand.randint(0, len(PIPES_LIST) - 1)
    IMAGES['pipe'] = (
        pygame.transform.flip(
        pygame.image.load(PIPES_LIST[pipeIndex]).convert_alpha(), False, True),
        pygame.image.load(PIPES_LIST[pipeIndex]).convert_alpha(),
        )
        
        
        
    movementInfo = menuScreen()
    crashInfo = mainGame(movementInfo)
    
        
        
    

def menuScreen():
    print("Menu Screen Stub")
    
    playerIndex = 0
    playerIndexGen = cycle([0, 1, 2, 1])
    
    basex = 0
    
    playerx = int(SCREENWIDTH * 0.2)
    playery = int((SCREENHEIGHT - IMAGES['player'][0].get_height()) /2)
    
    
    
    
    # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in pygame.event.get():  # get user interaction events
            if event.type == P.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  # tests if window's X (close) has been clicked
                pygame.quit()
                sys.exit()# causes exit of game loop
                
            if event.type == KEYDOWN and (event.key == K_2):
                helpScreen()
            elif event.type == KEYDOWN and (event.key == K_3):
                highScoreScreen()
            
            # your code starts here #
            if event.type == KEYDOWN and (event.key == K_SPACE): #includes touching screen
                return {
                    'playerIndexGen': playerIndexGen,
                    'basex': basex,
                    'playery': playery,
                    }   
            
        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))
        SCREEN.blit(IMAGES['base'],(basex, BASEY))
        SCREEN.blit(IMAGES['menu'],(0,0))
        
        
        
        P.display.update()
        clock.tick(loopRate)
        



def mainGame(movementInfo):
    print("Main Game Stub")
    
    playerIndex = 0
    
    playerx = int(SCREENWIDTH * 0.2)
    playery = movementInfo['playery']
    
    basex = movementInfo['basex']
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()
    
    
    #calls getRandomPipe function and creates 2 random pipes
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[0]['y']}
    ]
    
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[1]['y']}
    ]
    
    pipeVelX = -4
    
    
    
        # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in pygame.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                pygame.quit()
                sys.exit()
            
            # your code starts here #
            if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
                # change this to do something if user clicks mouse
                # or touches screen
                pass
            
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
            
        if 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])
            
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
            
            
        SCREEN.blit(IMAGES['background'],(0,0))
        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        
            
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (upperPipe['x'],upperPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lowerPipe['x'],lowerPipe['y']))
            
        SCREEN.blit(IMAGES['player'][playerIndex], (playerx, playery))
            
        P.display.update()
        clock.tick(loopRate)
    
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
            
def helpScreen():
    print("helpScreen Stub")
    # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                pygame.quit()
                sys.exit()
            
            # your code starts here #
            if event.type == KEYDOWN and (event.key == K_b): #includes touching screen
                main()

        SCREEN.blit(IMAGES['background'],(0,0))
        SCREEN.blit(IMAGES['help'],(0,0))
        
        P.display.update()
        clock.tick(loopRate)
    
def highScoreScreen():
    print("highscorescreen stub")
    
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                pygame.quit()
                sys.exit()
            
            # your code starts here #
            if event.type == KEYDOWN and (event.key == K_b): #includes touching screen
                main()

        SCREEN.blit(IMAGES['background'],(0,0))
        
        P.display.update()
        clock.tick(loopRate)
    
def getRandomPipe():
    print("Random Pipe Stub")
    
    gapY = rand.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
    gapY += int(BASEY * 0.2)
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return[
        { 'x': pipeX, 'y': gapY - pipeHeight }, #upper pipe
        { 'x': pipeX, 'y': gapY + PIPEGAPSIZE }, #lower pipe
    ]
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