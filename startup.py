#where everything that needs to be spawned is spawned in
import pygame
from pygame.locals import *
from sys import exit
from config import *
from objects import *
from random import randint, choice

pygame.init()

#set up
window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#things that need to be set to False at the beging of the game
hard_mode = False
infoing = False
stop_the_game = False

#sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()
monsters = pygame.sprite.Group()
ui_group = pygame.sprite.Group()
score_ui = pygame.sprite.Group()
health_ui = pygame.sprite.Group()
menu_ui = pygame.sprite.Group()
info_ui = pygame.sprite.Group()
pause_ui = pygame.sprite.Group()

#background
back_ground = Background((WINDOW_WITDTH/2,WINDOW_HEIGHT/2),0,0,WINDOW_WITDTH,WINDOW_HEIGHT)
base_platform_moving = Background((WINDOW_WITDTH/2,WINDOW_HEIGHT),0,WINDOW_HEIGHT-60,WINDOW_WITDTH,60, image = "Assets/platform.png")
    




#objects
#moving platforms
def platform_spawn():
    #spawns the moving platforms
    platform = Platform((WINDOW_WITDTH,WINDOW_HEIGHT-200),randint(100,200),20, image = "Assets/flying_platforms.png")
    platform.add(all_sprites,platforms)
    platform.vel = Vector2(-randint(4,8),0)

#baseplatform
#creates the base platform
def base_platform_spawn():
    #spawns the non moving base platform
    base_platform = Platform((WINDOW_WITDTH/2,WINDOW_HEIGHT ),WINDOW_WITDTH,60)
    base_platform.add(all_sprites,platforms)
    base_platform_moving.add(all_sprites)
    base_platform.vel = Vector2(0,0)

#player
#creates the player
player = Player((30,WINDOW_HEIGHT/2),40,40)
player.add(all_sprites, players)
player.vel = Vector2(0,0)

#monsters
#creates the monster
def monster_spawn():
    #spawns the monsters
    monster_colours = ["Assets/monster/0.png", "Assets/monster/1.png", "Assets/monster/2.png", "Assets/monster/3.png", "Assets/monster/4.png" ]
    monster_colour = choice(monster_colours)
    monster = Monster((WINDOW_WITDTH+30,WINDOW_HEIGHT-60.01),randint(80,100),70,image= monster_colour )
    monster.add(all_sprites, monsters)
    monster.vel = Vector2(MONSTER_SPEED-randint(3,6),0)


#text
def get_font(size): 
    #changes the font to the font that I wanted to use
        return Font("Assets/font.ttf", size)
def text_spawn():
    #player health 
    player_health_text = Text("Health: " + str(player.health),(WINDOW_WITDTH/2-240,40), font = get_font(25))
    player_health_text.add(all_sprites, health_ui )
    #score text
    score_text = Text("Score: " + str(player.score),(WINDOW_WITDTH/2+240,40),font = get_font(25))
    score_text.add(all_sprites, score_ui)

#buttons
start_button = Button((WINDOW_WITDTH/2-100,WINDOW_HEIGHT/2),150,70)
start_button.add(menu_ui)

end_button = Button((WINDOW_WITDTH/2+100,WINDOW_HEIGHT/2+120),150,70,image = "Assets/end.png")
end_button.add(menu_ui,info_ui,pause_ui)

hard_mode_button = Button((WINDOW_WITDTH/2+100,WINDOW_HEIGHT/2),150,70,image = "Assets/hard.png")
hard_mode_button.add(menu_ui)

info_button =  Button((WINDOW_WITDTH/2-100,WINDOW_HEIGHT/2+120),150,70,image = "Assets/info.png")
info_button.add(menu_ui)

back_button = Button((WINDOW_WITDTH/2-100,WINDOW_HEIGHT/2+120),150,70,image = "Assets/back.png")
back_button.add(info_ui)

play_button = Button((WINDOW_WITDTH/2-100,WINDOW_HEIGHT/2+120),150,70,image = "Assets/play.png")
play_button.add(pause_ui)



#functions
def player_hit():
    #player and monster colision
    hit_monster = pygame.sprite.spritecollide(player,monsters,True)
    if len(hit_monster) != 0:
        player.health -= 1
        update_health()
        
        if player.action < len(player.animation_list) - 1:
            player.action += 1
            player.frame = 0
            pygame.time.wait(50)
        monster_spawn()

def player_running():
    #resets the animation to the player running code
    if player.action > 0:
        if player.action == 1:
            pygame.time.wait(50)
        player.action = 0
        player.frame = 0
            


def platform_leave():
    #platform leaves the screen
    for platform in platforms:
        if not window.get_rect().inflate(400,200).contains(platform.rect):
            platform.kill()
            platform_spawn()

def monster_leave():
    #monster leaves the screen
    for monster in monsters:
            if not window.get_rect().inflate(150,100).contains(monster.rect):
                monster.kill()
                player.score += 1 
                update_score()
                monster_spawn()

def update_health():
    #updates all of the health ui
    for player_health_text in health_ui:
        player_health_text.text = "Health: " + str(player.health)

def update_score():
    #updates all the score ui
    for score_text in score_ui:
        score_text.text = "Score: " + str(player.score)

def reset():
    #resets the positions of things in the game
    if player.playeralive == False:
        player.restart((30,WINDOW_HEIGHT/2))
        update_health()
        update_score()
        for monster in monsters:
            monster.kill()
        for platform in platforms:
            platform.kill()


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
                elif event.key == K_DOWN or event.key == K_s:
                    player.move("down") 
                elif event.key == K_p:
                    pause()
        #Constant movment to the left or the right
        move_ticker = 0
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            if move_ticker == 0:
                move_ticker = 3
                player.move("left")
        if keys[K_RIGHT] or keys[K_d]:
            if move_ticker == 0:   
                move_ticker = 3     
                player.move("right")
                
            
        monster_leave()
        platform_leave()
        player_running()
        player_hit()
         
        player.colision_with_platforms(platforms)
        player.player_offscreen()

        for monster in monsters:
            monster.colision_with_platforms(platforms)
        
        #hard mode
        if hard_mode == True:
            if player.score == 0 or player.score == 1 :
                monster_spawn()

        window.fill(BACKGROUNDCOLOUR)
        back_ground.update()
        back_ground.render(window)
        
        all_sprites.update()
        
        
        for sprite in all_sprites:
            window.blit(sprite.image,sprite.rect)
        base_platform_moving.update()
        base_platform_moving.render(window)

        
        pygame.display.update()

        if player.health == 0:
            game_over()
        if move_ticker > 0:
            move_ticker -= 1


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


def pause():
    #pauses the game
    black_background = pygame.Surface((WINDOW_WITDTH,WINDOW_HEIGHT))
    black_background.set_alpha(150)
    pygame.draw.rect(black_background,(0,0,0),black_background.get_rect(),10)
    window.blit(black_background,(0,0))
    paused = True
    pause_text = Text("Paused",(WINDOW_WITDTH/2,WINDOW_HEIGHT/2), font = get_font(50))
    pause_text.add(all_sprites, ui_group)
    ui_group.draw(window)
    health_ui.draw(window)
    score_ui.draw(window)
    pause_ui.draw(window)
    pygame.display.update()
    
    while paused:
        event = pygame.event.wait()
        if event.type == QUIT:
                paused = False
                pause_text.kill()
        if event.type == KEYDOWN:
            if event.key == K_p:
                paused = False
                pause_text.kill()
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

        
        if play_button.draw(window) == True:
            pause_text.kill()
            paused = False
        if end_button.draw(window) == True:
            pygame.quit()
            exit()
