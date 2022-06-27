#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from config import *
from objects import *
from startup import *


#runs the main game loop
def game():
    pygame.display.set_caption("Game")
    
    base_platform_spawn()
    platform_spawn()
    monster_spawn()
    text_spawn()
    
    

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
                elif event.key == K_r:
                    reset()
            
        monster_leave()
        platform_leave()
        player_hit()
        
        
              
        player_hits_platform(player, platforms)

        player_offscreen()

        for monster in monsters:
            monster_hits_platform(monster,platforms)


        
        window.fill(BACKGROUNDCOLOUR)
        back_ground.update()
        back_ground.render(window)
        all_sprites.update()
        
        for sprite in all_sprites:
            window.blit(sprite.image,sprite.rect)

        game_over()
        pygame.display.update()


def main_menu():
    #runs the main menu loop
    global game
    global running
    pygame.display.set_caption("Main menu")

    menu = True
    while menu:
        game_clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == QUIT:
                running = False
                menu = False
                
            elif event.type == KEYDOWN:
                #if ESC key gets pressed
                if event.key == K_ESCAPE:
                    menu = False #if the escape key is pressed quit the game.
                elif event.key == K_g:
                    game()
                
        


        menu_text = Text("Menu",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100), menu_ui)
        body_text= Text("press g to play",40,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2+150), menu_ui)

        window.fill((255,255,255))


        menu_ui.update()

        for sprite in menu_ui:
            window.blit(sprite.image,sprite.rect)

        pygame.display.update()

def game_over():
    global running
    #checks to see if the game is over
    if player.health == 0:
            gameover_text = Text("Game Over",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),all_sprites, ui_group)
            ui_group.draw(window)
            health_ui.draw(window)
            score_ui.draw(window)

            pygame.display.update()
            pygame.time.delay(1000)
            gameover_text.kill()
            player.playeralive = False
            reset()
            running = False
            main_menu()
main_menu()
pygame.quit()
