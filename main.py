#This is where the main loop and other things that interact with the main loop is kept 

import pygame 
from sys import exit
from config import *
from objects import *
from startup import *



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
                
            elif event.type == KEYDOWN:
                #if ESC key gets pressed
                if event.key == K_ESCAPE:
                    running = False #if the escape key is pressed quit the game.
                    menu = False
                    pygame.quit()
                    exit()
                    
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
        if hard_mode == True:
            if player.score == 0:
                monster_spawn()

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
    global hard_mode
    global infoing
    pygame.display.set_caption("Menu")
    running = False
    hard_mode = False

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
                
                
                
            elif event.type == KEYDOWN:
                #if ESC key gets pressed
                if event.key == K_ESCAPE:
                    running = False
                    menu = False
                    pygame.quit()
                    exit()
                    



        menu_text = Text("Pigeon Pedestrian",(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100), font= get_font(40))
        menu_text.add(menu_ui)

        window.fill(BACKGROUNDCOLOUR)
        
        back_ground.render(window)
        back_ground.update()


        menu_ui.update()

        if start_button.draw(window) == True:
            game()
        
        if hard_mode_button.draw(window) == True:
            hard_mode = True
            game()
        
        if info_button.draw(window) == True:
            infoing = True
            info()
        
        

        if end_button.draw(window) == True:
            stop_the_game = True
            running = False
            menu = False
            pygame.quit()
            exit()
            

        for sprite in menu_ui:
            window.blit(sprite.image,sprite.rect)
        
        
        pygame.display.update()

def game_over():
    #checks to see if the player has died
    
    global running
    global menu
    
    #checks to see if the game is over
    if player.health == 0:
            gameover_text = Text("Game Over",(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),font= get_font(50))
            gameover_text.add(all_sprites, ui_group)
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
            hard_mode = False
            reset()
            running = False
            main_menu()

def info():
    #runs the info loop where the player can find out how to play the game and what its about
    global infoing
    pygame.display.set_caption("Info")

    infoing = True
    if infoing == True:
        while infoing:
            game_clock.tick(FPS)
            events = pygame.event.get()
            window.fill(BACKGROUNDCOLOUR)
            for event in events:
                #print(event)
                if event.type == QUIT:
                    infoing = False
                    pygame.quit()
                    exit()
                    
                elif event.type == KEYDOWN:
                    #if ESC key gets pressed
                    if event.key == K_ESCAPE:
                        infoing = False
                        pygame.quit()
                        exit()
            info_text_1 = Text("Use WASD or Arrow keys to move the pigeon around the screen.",(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100), font= get_font(13))
            info_text_1.add(info_ui)
            info_text_2 = Text("Avoid getting hit by the cars by jumping over them.",(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100+20), font= get_font(13))
            info_text_2.add(info_ui)
            info_text_3 = Text("Every time the car leaves the screen you gain one point",(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100+40), font= get_font(13))
            info_text_3.add(info_ui)
            if back_button.draw(window) == True:
                main_menu()
            if end_button.draw(window) == True:
                        infoing = False
                        pygame.quit()
                        exit()
                        
            

            for sprite in info_ui:
                window.blit(sprite.image,sprite.rect)
            
            pygame.display.update()
            


    

main_menu()#Starts off the game at the Menu

pygame.quit()
