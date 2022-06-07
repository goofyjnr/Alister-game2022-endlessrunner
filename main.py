#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from pygame.locals import *
from config import *
from objects import *
from startup import *
from random import randint

pygame.init()

window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#sprite groups

#objects
#platforms
#baseplatform
#player
#monsters
#coins
#text


#main game loop
running = True
while running:
    game_clock.tick(FPS)

    #get the events
    events = pygame.event.get()
    for event in events:
        print(event)
        if event.type == QUIT:
            running = False
            


    window.fill(BACKGROUNDCOLOUR)
    pygame.display.update()

pygame.quit()