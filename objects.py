#This is where all the classes will be kept to make easy changes to them and to keep them all in one place

from config import *
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import scale
from pygame.font import Font

class Drawable(Sprite):
    def __init__(self,position,width,height,image="Assets/chara.png"):
        super().__init__()

        self.position = Vector2(position)
        self.image = scale(load(image),(width,height))
        self.image.set_colorkey((70,60,78))

        self.rect = self.image.get_rect(midbottom=position)

class Physics(Drawable):
    def __init__(self, position, width, height, image="Assets/chara.png"):
        super().__init__(position, width, height, image)

        self.vel = Vector2((0,0))

    def update(self):
        self.vel += GRAVITY
        self.vel -= self.vel * FRIC
        self.position += self.vel
        self.rect.midbottom = self.position
        

class Player(Physics):
    def __init__(self, position, width, height, image="Assets/chara.png"):
        super().__init__(position, width, height, image)

        self.score = 0
        

class Monster(Physics):
    pass

class Coin(Physics):
    pass

class Text(Sprite):
    pass

class Platform(Physics):
    def __init__(self, position, width, height, image="Assets/platform.png"):
        super().__init__(position, width, height, image)
        self.vel = Vector2((0,0))
    def update(self):
        self.position += self.vel
        self.rect.midbottom = self.position

class Powerup(Physics):
    pass