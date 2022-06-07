#This is where all the classes will be kept to make easy changes to them and to keep them all in one place

from config import *
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import scale
from pygame.font import Font

class Drawable(Sprite):
    pass

class Physics(Drawable):
    pass

class Player(Physics):
    pass

class Monster(Physics):
    pass

class Coin(Physics):
    pass

class Text(Sprite):
    pass

class Platform(Physics):
    pass

class Powerup(Physics):
    pass