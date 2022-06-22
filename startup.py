#where everything that needs to be spawned is spawned in
from platform import platform
import pygame
from pygame.locals import *

from config import *
from objects import *
from random import randint

pygame.init()

window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()
monsters = pygame.sprite.Group()
ui_group = pygame.sprite.Group()
score_ui = pygame.sprite.Group()
health_ui = pygame.sprite.Group()
menu_ui = pygame.sprite.Group()

#background
back_ground = Background((WINDOW_WITDTH/2,WINDOW_HEIGHT/2),WINDOW_WITDTH,WINDOW_HEIGHT)

#objects
#moving platforms
def platform_spawn():
    platform = Platform((WINDOW_WITDTH,WINDOW_HEIGHT-200),randint(100,200),20)
    platform.add(all_sprites,platforms)
    platform.vel = Vector2(-randint(4,8),0)



#baseplatform
#creates the base platform
def base_platform_spawn():
    base_platform = Platform((WINDOW_WITDTH/2,WINDOW_HEIGHT ),WINDOW_WITDTH,60)
    base_platform.add(all_sprites,platforms)
    base_platform.vel = Vector2(0,0)


#player
#creates the player

player = Player((30,WINDOW_HEIGHT/2),40,40)
player.add(all_sprites, players)
player.vel = Vector2(0,0)

#monsters
#creates the monster

def monster_spawn():
    monster = Monster((WINDOW_WITDTH,WINDOW_HEIGHT-65),randint(60,80),randint(60,90))
    monster.add(all_sprites, monsters)
    monster.vel = Vector2(MONSTER_SPEED-randint(1,6),0)


#coins/points


#text
def text_spawn():
    #player health 
    player_health_text = Text("Health: " + str(player.health),50,(WINDOW_WITDTH/2-200,WINDOW_HEIGHT/2+200),all_sprites, health_ui)
    #score text
    score_text = Text("Score: " + str(player.score),50,(WINDOW_WITDTH/2+200,WINDOW_HEIGHT/2+200),all_sprites, score_ui)


#player and platform colision
def player_hits_platform(player, platforms):
    player_hits_platforms = pygame.sprite.spritecollide(player,platforms,False)
    if len(player_hits_platforms) != 0:
        if player.vel.y > 0 and player.position.y < player_hits_platforms[0].rect.bottom:
            player.vel.y = 0 
            player.position.y = player_hits_platforms[0].rect.top 
            player.jumping = False #resets it so after you touch a platform you can jump again
            player.jump_count = 0

#monste and platform colision
def monster_hits_platform(monster,platforms):
    monster_hits_platforms = pygame.sprite.spritecollide(monster,platforms,False)
    if len(monster_hits_platforms) != 0 :
        if monster.vel.y > 0:
            monster.vel.y = 0
            monster.position.y = monster_hits_platforms[0].rect.top 


#pauses the game
def pause():
    paused = True
    pause_text = Text("Paused",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2),all_sprites, ui_group)
    ui_group.draw(window)
    health_ui.draw(window)
    score_ui.draw(window)
    pygame.display.update()
    
    while paused:
        event = pygame.event.wait()
        if event.type == QUIT:
                paused = False
        if event.type == KEYDOWN:
            if event.key == K_p:
                
                paused = False
                pause_text.kill()


#stops the player from going off screen
def player_offscreen():
    if player.position.x < 0:
        player.vel = Vector2(0,0)
        player.position.x = player.position.x+3       
    if player.position.x > WINDOW_WITDTH:
        player.vel = Vector2(0,0)
        player.position.x = player.position.x-3
    if player.position.y < 0 :
        player.vel = Vector2(0,0)
        player.position.y = player.position.y+3

def player_hit():
    hit_monster = pygame.sprite.spritecollide(player,monsters,True)
    if len(hit_monster) != 0:
        player.health -= 1
        update_health()
        monster_spawn()



def platform_leave():
    for platform in platforms:
        if not window.get_rect().inflate(400,200).contains(platform.rect):
            platform.kill()
            platform_spawn()

def monster_leave():
    for monster in monsters:
            if not window.get_rect().inflate(150,100).contains(monster.rect):
                monster.kill()
                player.score += 1 
                update_score()
                monster_spawn()

def update_health():
    for player_health_text in health_ui:
        player_health_text.text = "Health: " + str(player.health)

def update_score():
    for score_text in score_ui:
        score_text.text = "Score: " + str(player.score)

def reset():
    if player.playeralive == False:
        player.restart((30,WINDOW_HEIGHT/2))
        update_health()
        update_score()
        for monster in monsters:
            monster.kill()
        for platform in platforms:
            platform.kill()
        

