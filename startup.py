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

#objects
#moving platforms
#baseplatform
platform = Platform((WINDOW_WITDTH/2,WINDOW_HEIGHT),WINDOW_WITDTH,60)
platform.add(all_sprites,platforms)

#player
player = Player((30,WINDOW_HEIGHT/2),40,40)
player.add(all_sprites, players)
player.vel = Vector2(0,0)
#monsters
#coins
#text
