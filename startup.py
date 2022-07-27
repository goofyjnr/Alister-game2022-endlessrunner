#where everything that needs to be spawned is spawned in
import pygame
from pygame.locals import *

from config import *
from objects import *
from random import randint, random, choice

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
    monster = Monster((WINDOW_WITDTH,WINDOW_HEIGHT-65),randint(80,100),70,image= monster_colour )
    monster.add(all_sprites, monsters)
    monster.vel = Vector2(MONSTER_SPEED-randint(1,6),0)


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
end_button.add(menu_ui,info_ui)

hard_mode_button = Button((WINDOW_WITDTH/2+100,WINDOW_HEIGHT/2),150,70,image = "Assets/hard.png")
hard_mode_button.add(menu_ui)

info_button =  Button((WINDOW_WITDTH/2-100,WINDOW_HEIGHT/2+120),150,70,image = "Assets/info.png")
info_button.add(menu_ui)

back_button = Button((WINDOW_WITDTH/2-100,WINDOW_HEIGHT/2+120),150,70,image = "Assets/back.png")
back_button.add(info_ui)



#functions
#pauses the game
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



