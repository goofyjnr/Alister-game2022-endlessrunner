#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from sys import exit
from config import *
from objects import *
from startup import *

stop_the_game = False

def game():
    #runs the main game loop
    global menu
    pygame.display.set_caption("Pigeon Pedestrian")
    
    menu = False
    base_platform_spawn()
    platform_spawn()
    monster_spawn()
    text_spawn()
    
    

    #main game loop
    running = True
    while running:
        if stop_the_game:
            return

        game_clock.tick(FPS)

        #get the events
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()
                break
            elif event.type == KEYDOWN:
                #if ESC key gets pressed
                if event.key == K_ESCAPE:
                    running = False #if the escape key is pressed quit the game.
                    menu = False
                    pygame.quit()
                    exit()
                    break
                elif event.key == K_SPACE or event.key == K_w or event.key == K_UP:
                    player.jump()
                elif event.key == K_RIGHT or event.key == K_d:
                    player.move("right")
                elif event.key == K_LEFT or event.key == K_a:
                    player.move("left")
                elif event.key == K_DOWN or event.key == K_s:
                    player.move("down")
                elif event.key == K_p:
                    pause()
            
        monster_leave()
        platform_leave()
        player_hit()
         
        player.colision_with_platforms(platforms)
        player.player_offscreen()

        for monster in monsters:
            monster.colision_with_platforms(platforms)
        
        #hard mode
        #if player.score == 1:
          #  monster_spawn()

        window.fill(BACKGROUNDCOLOUR)
        back_ground.update()
        back_ground.render(window)
        all_sprites.update()
        
        for sprite in all_sprites:
            window.blit(sprite.image,sprite.rect)

        
        pygame.display.update()

        if player.health == 0:
            game_over()


def main_menu():
    #runs the main menu loop
    global game
    global running
    pygame.display.set_caption("Menu")
    running = False

    menu = True
    while menu:
        game_clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == QUIT:
                running = False
                menu = False
                pygame.quit()
                exit()
                break
                
                
            elif event.type == KEYDOWN:
                #if ESC key gets pressed
                if event.key == K_ESCAPE:
                    running = False
                    menu = False
                    pygame.quit()
                    exit()
                    break

                
        


        menu_text = Text("Menu",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100), menu_ui)

        window.fill((23,33,39))


        menu_ui.update()

        if start_button.draw(window) == True:
            game()
        
        

        for sprite in menu_ui:
            window.blit(sprite.image,sprite.rect)

        if end_button.draw(window) == True:
            stop_the_game = True
            running = False
            menu = False
            pygame.quit()
            exit()
            break
        pygame.display.update()

def game_over():
    
    global running
    global menu
    #checks to see if the game is over
    if player.health == 0:
            gameover_text = Text("Game Over",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),all_sprites, ui_group)
            ui_group.draw(window)
            health_ui.draw(window)
            score_ui.draw(window)

            pygame.display.update()
            pygame.time.delay(1000)
            gameover_text.kill()
            for monster in monsters:
                monster.kill()
            for platform in platforms:
                platform.kill()
            player.playeralive = False
            running = False
            menu = False
            reset()
            running = False
            main_menu()
    

main_menu()

pygame.quit()
