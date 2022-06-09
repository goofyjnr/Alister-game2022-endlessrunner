#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from pygame.locals import *
from config import *
from objects import *
from startup import *
from random import randint

pygame.init()


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
        elif event.type == KEYDOWN:
            #if ESC key gets pressed
            if event.key == K_ESCAPE:
                running = False #if the escape key is pressed quit the game.
            elif event.key == K_SPACE:
                player.jump()
            elif event.key == K_RIGHT or event.key == K_d:
                player.move("right")
            elif event.key == K_LEFT or event.key == K_a:
                player.move("left")
            elif event.key == K_DOWN or event.key == K_s:
                player.move("down")
        
            
    hits_platform(player,platforms)

    all_sprites.update()
    window.fill(BACKGROUNDCOLOUR)
    for sprite in all_sprites:
        window.blit(sprite.image,sprite.rect)
    pygame.display.update()

pygame.quit()