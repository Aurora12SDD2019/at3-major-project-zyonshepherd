""" Short, one line description of the project ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Zyon Shepherd"
__license__ = "GPL"
__version__ = "0.0.9"
__email__ = "zyon.shepherd@education.nsw.gov.au"
__status__ = "Alpha"


'''revision notes:
09 made score work and also added files for the scores to be saved to however didn't get to making the highscores arrange
08 fixed collision with pipe, it was not working as the code I got did not fit the code, also starting to work with the score which prints
out a sore but has an error and prints out a large number
07 made bird print to screen and fly, found the physics of the values of the bird, also applied collisions to the ground but pipe
collisions are not working for some reason
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
SCREENWIDTH  = 288 #sets screen width
SCREENHEIGHT = 512 #sets screen height
BASEY = SCREENHEIGHT * 0.79 #sets the value of where base is
PIPEGAPSIZE = 100 #sets gap size between pipe
BLACK = (0,0,0) #creates colour black
WHITE = (255,255,255) #creates colour white
font = pygame.font.Font(None,30) #creates font


P.display.set_caption("Flappy Bird Game") #creates display name
IMAGES, SOUNDS, HITMASKS = {}, {}, {} # creates dictionarys for different 


'''imports sprites'''
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

xrange = range #used for creating lists


def main():
    global clock, SCREEN #creates gloabal variables for clock and SCREEN
    
    
    clock = pygame.time.Clock()  # creates clock to limit frames per second
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) #displays screen
    pygame.display.set_caption('Flappy Bird') #sets caption equal to flappy bird
    
    '''loads and randomises sprites to choose different setups each time'''
    
    
    IMAGES['menu'] = pygame.image.load('media/menu.png').convert_alpha()
    IMAGES['base'] = pygame.image.load('media/base.png').convert_alpha()
    IMAGES['help'] = pygame.image.load('media/help.png').convert_alpha()
    
        

    
    while True:
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
            # hitmask for pipes
        HITMASKS['pipe'] = (
            getHitMask(IMAGES['pipe'][0]),
            getHitMask(IMAGES['pipe'][1])
        )

            # hitmask for player
        HITMASKS['player'] = (
            getHitMask(IMAGES['player'][0]),
            getHitMask(IMAGES['player'][1]),
            getHitMask(IMAGES['player'][2])
        )
        
        
             
            
        movementInfo = menuScreen()
        crashInfo = mainGame(movementInfo)
        gameOverScreen(crashInfo)
    
    
        
        
    

def menuScreen():

    
    playerIndex = 0 #sets the player index to 0
    playerIndexGen = cycle([0, 1, 2, 1])
    
    basex = 0 #sets value of basex to 0
    
    playerx = int(SCREENWIDTH * 0.2) #sets value of playerx to half of the Screen width
    playery = int((SCREENHEIGHT - IMAGES['player'][0].get_height()) /2) #sets playery to 
    
    
    
    
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

    
    playerIndex = 0
    loopIter = 0
    score = 0
    playerIndexGen = movementInfo['playerIndexGen']
    
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
    
    # player velocity, max velocity, downward accleration, accleration on flap
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerMaxVelY =  10   # max vel along Y, max descend speed
    playerMinVelY =  -8   # min vel along Y, max ascend speed
    playerAccY    =   1   # players downward accleration
    playerFlapAcc =  -9   # players speed on flapping
    playerFlapped = False # True when player flaps
    
    
    
        # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in pygame.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                pygame.quit()
                sys.exit()
            
            # your code starts here #
            if event.type == KEYDOWN and (event.key == K_SPACE): #includes touching screen
                if playery > -2 * IMAGES['player'][0].get_height():
                    playerVelY = playerFlapAcc
                    playerFlapped = True
                    
        crashCheckTest = crashCheck({'x': playerx, 'y':playery, 'index': playerIndex}, upperPipes, lowerPipes)

        if crashCheckTest[0]:
            return {
                'y': playery,
                'groundCrash': crashCheckTest[1],
                'basex': basex,
                'score': score,
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'playerVelY': playerVelY,
                
            }
        
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
        
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 100) % baseShift)
        
        
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped == True:
            playerFlapped = False
            
        playerHeight = IMAGES['player'][playerIndex].get_height()
        playery += min(playerVelY, BASEY - playery - playerHeight)
                
            
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
            
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (upperPipe['x'],upperPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lowerPipe['x'],lowerPipe['y']))
            
        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        
        showScore(score)
            
        SCREEN.blit(IMAGES['player'][playerIndex], (playerx, playery))
        
            
        P.display.update()
        clock.tick(loopRate)
    
def gameOverScreen(crashInfo):
    
    score = crashInfo['score']
    showScore(score)
    
    name = ''
    
    # game loop - runs loopRate times a second!
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                play = False  # causes exit of game loop
            
            # your code starts here #
        if name is not '': #includes touching screen
                
            highScoreScreen()
            return {
                'name': name
            }

        name = input("What is your name")
        
        writeInFile = open("media/HighScores/LeaderBoard-AllTime.txt","a+")
        writeInFile.write(name + " " + str(score) + "\r" + "\n")
        writeInFile.close()
        
        writeInFile = open("media/HighScores/LeaderBoard-Monthly.txt","a+")
        writeInFile.write(name + " " + str(score) + "\r" + "\n")
        writeInFile.close()
                
        writeInFile = open("media/HighScores/LeaderBoard-Yearly.txt","a+")
        writeInFile.write(name + " " + str(score) + "\r" + "\n")
        writeInFile.close()
            
        SCREEN.blit(IMAGES['background'], (0,0))
        
        P.display.update()
        clock.tick(loopRate)
        

        
    
            
def helpScreen():

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

    
    while True:  # game loop - note:  everything in this loop is indented one tab

        for event in P.event.get():  # get user interaction events
            if event.type == P.QUIT:  # tests if window's X (close) has been clicked
                pygame.quit()
                sys.exit()
            
            # your code starts here #
            if event.type == KEYDOWN and (event.key == K_b): #includes touching screen
                main()
                
        choice = input("What would you like to print out 'Monthly, Yearly or AllTime'? ")
        
        if choice == 'AllTime':
            readAllTime = open("media/HighScores/LeaderBoard-AllTime.txt", "r")
            printAllTimes = readAllTime.readlines()
            for line in printAllTimes:
                print("------------------\n" + line)
        
        elif choice == 'Monthly':
            readMonthly = open("media/HighScores/LeaderBoard-Monthly.txt", "r")
            printMonthly = readMonthly.readlines()
            for line in printMonthly:
                print("------------------\n" + line)
                
        elif choice == 'Yearly':
            readYearly = open("media/HighScores/LeaderBoard-Monthly.txt", "r")
            printYearly = readYearly.readlines()
            for line in printYearly:
                print("------------------\n" + line)
        
        
            
        menuScreen()
        SCREEN.blit(IMAGES['background'],(0,0))
        
        
        
        
        P.display.update()
        clock.tick(loopRate)
    
    
        
    
def getRandomPipe():

    
    gapY = rand.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
    gapY += int(BASEY * 0.2)
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return[
        { 'x': pipeX, 'y': gapY - pipeHeight }, #upper pipe
        { 'x': pipeX, 'y': gapY + PIPEGAPSIZE }, #lower pipe
    ]
def showScore(score):

    
    pipesPassed = 0
    
    scoreDigits = [int(x) for x in list(str(score))]
    
    
    scoreText = font.render('Score: {}'.format(score),1,WHITE,BLACK)
    SCREEN.blit(scoreText,[0,0])
    
    
    
    
    
    

def crashCheck(player, upperPipes, lowerPipes):
    '''hecks for possible crash in program'''
    playerIndex = player['index']
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()
    
    if player['y'] + player['h'] >= BASEY - 1:
        return [True, True]
    else:

        playerRect = pygame.Rect(player['x'], player['y'], player['w'], player['h'])
        pipeW = IMAGES['pipe'][0].get_width()
        pipeH = IMAGES['pipe'][0].get_height()

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            upperPipeRect = pygame.Rect(upperPipe['x'], upperPipe['y'], pipeW, pipeH)
            lowerPipeRect = pygame.Rect(lowerPipe['x'], lowerPipe['y'], pipeW, pipeH)

            # player and upper/lower pipe hitmasks
            pHitMask = HITMASKS['player'][playerIndex]
            uHitmask = HITMASKS['pipe'][0]
            lHitmask = HITMASKS['pipe'][1]

            # if bird collided with upipe or lpipe
            upperCollide = pixelCollision(playerRect, upperPipeRect, pHitMask, uHitmask)
            lowerCollide = pixelCollision(playerRect, lowerPipeRect, pHitMask, lHitmask)

            if upperCollide or lowerCollide:
                return [True, False]

    return [False, False]
    
def pixelCollision(rect1,rect2, hm1, hm2):
    """checks if two objects have collided using hitmasks"""
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hm1[x1+x][y1+y] and hm2[x2+x][y2+y]:
                return True
    return False


    
def getHitMask(image):
    print("Get Hit Mask Stub")
    mask = []
    
    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x, y))[3]))
    return mask
    

    



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
pygame.quit()   # stops the game engine
sys.exit()  # close operating system window