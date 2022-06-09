#where everything that needs to be spawned is spawned in
import pygame

from config import *
from objects import *

window = pygame.display.set_mode((WINDOW_WITDTH,WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

#sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()
monsters = pygame.sprite.Group()

#objects
#moving platforms
#baseplatform
#creates the base platform
platform = Platform((WINDOW_WITDTH/2,WINDOW_HEIGHT),WINDOW_WITDTH,60)
platform.add(all_sprites,platforms)


#player
#creates the player
player = Player((30,WINDOW_HEIGHT/2),40,40)
player.add(all_sprites, players)
player.vel = Vector2(0,0)

#monsters
#creates the monster
monster = Monster((WINDOW_WITDTH-30,WINDOW_HEIGHT/2),40,40)
monster.add(all_sprites, monsters)
monster.vel = Vector2(-3,0)

#coins
#text


#player and platform colision
def hits_platform(player,platforms):
    hits_platforms = pygame.sprite.spritecollide(player,platforms,False)
    if len(hits_platforms) != 0 :
        if player.vel.y > 0:
            player.vel.y = 0 
            player.position.y = hits_platforms[0].rect.top+1
            player.jumping = False #resets it so after you touch a platform you can jump again
            player.jump_count = 0