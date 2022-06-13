#where everything that needs to be spawned is spawned in
import pygame

from config import *
from objects import *
from random import randint

window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()
monsters = pygame.sprite.Group()

#background
back_ground = Background((WINDOW_WITDTH/2,WINDOW_HEIGHT/2),WINDOW_WITDTH,WINDOW_HEIGHT)

#objects
#moving platforms
def platform_spawn():
    platform = Platform((WINDOW_WITDTH,WINDOW_HEIGHT-200),100,20)
    platform.add(all_sprites,platforms)
    platform.vel = Vector2(-randint(3,5),0)

#baseplatform
#creates the base platform
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
    monster = Monster((WINDOW_WITDTH-30,WINDOW_HEIGHT/2+70),randint(40,60),randint(40,60))
    monster.add(all_sprites, monsters)
    monster.vel = Vector2(-5,0)


#coins
#text


#player and platform colision
def player_hits_platform(player, platforms):
    player_hits_platforms = pygame.sprite.spritecollide(player,platforms,False)
    if len(player_hits_platforms) != 0 :
        if player.vel.y > 0:
            player.vel.y = 0 
            player.position.y = player_hits_platforms[0].rect.top 
            player.jumping = False #resets it so after you touch a platform you can jump again
            player.jump_count = 0

#monste and platform colision
def monster_hits_platform(monster, platforms):
    monster_hits_platforms = pygame.sprite.spritecollide(monster,platforms,False)
    if len(monster_hits_platforms) != 0 :
        if monster.vel.y > 0:
            monster.vel.y = 0
            monster.position.y = monster_hits_platforms[0].rect.top 