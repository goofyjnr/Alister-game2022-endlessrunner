#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from pygame.locals import *
from config import *
from objects import *
from startup import *
from random import randint

pygame.init()

#player and platform colision
def hits_platform(player,platforms):
    hits_platforms = pygame.sprite.spritecollide(player,platforms,False)
    if len(hits_platforms) != 0 :
        if player.vel.y > 0:
            player.vel.y = 0 
            player.position.y = hits_platforms[0].rect.top+1

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
        
            
    hits_platform(player,platforms)

    all_sprites.update()
    window.fill(BACKGROUNDCOLOUR)
    for sprite in all_sprites:
        window.blit(sprite.image,sprite.rect)
    pygame.display.update()

pygame.quit()