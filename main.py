#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from config import *
from objects import *
from startup import *


platform_spawn()
monster_spawn()

#main game loop
running = True
while running:
    game_clock.tick(FPS)

    #get the events
    events = pygame.event.get()
    for event in events:
        #print(event)
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
            elif event.key == K_p:
                pause()
        
    for monster in monsters:
        if not window.get_rect().inflate(150,100).contains(monster.rect):
            monster.kill()
            player.score += 1 
            score_text.text = "Score: " + str(player.score)
            monster_spawn()
    
            
    platform_leave()
    
    player_hit()

    if player.health == 0:
        gameover_text = Text("Game Over",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),all_sprites, ui_group)
        ui_group.draw(window)
        player.kill()
        pygame.display.update()
        pygame.time.delay(1000)
        running = False
            
    player_hits_platform(player, platforms)
    monster_hits_platform(monster, platforms)
    player_offscreen()

    
    window.fill(BACKGROUNDCOLOUR)
    back_ground.update()
    back_ground.render(window)
    all_sprites.update()
    
    for sprite in all_sprites:
        window.blit(sprite.image,sprite.rect)

    pygame.display.update()

pygame.quit()