#This is where all the classes will be kept to make easy changes to them and to keep them all in one place
from itertools import count
from config import *
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import scale, flip
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
        self.vel.x -= self.vel.x * FRIC
        self.position += self.vel
        self.rect.midbottom = self.position
        

class Player(Physics):
    def __init__(self, position, width, height, image="Assets/chara.png"):
        super().__init__(position, width, height, image)

        self.score = 0
        self.jumping = False #sets it up so can jump the first time
        self.jump_count = 0

    def move(self,direction):
        if direction == "left":
            self.vel.x -= MOVE_STRENGTH.x
        elif direction == "right":
            self.vel.x += MOVE_STRENGTH.x
        elif direction =="down":
            self.vel.y += MOVE_STRENGTH.y
    
    def jump(self):
        if self.jumping == False and self.jump_count < 2:
            self.jump_count = self.jump_count + 1
            self.vel += JUMP_STRENGTH
        elif self.jump_count == 2:
            self.jumping = True

    
        

class Monster(Physics):
    def __init__(self, position, width, height, image="Assets/monster.png"):
        super().__init__(position, width, height, image)
        self.image = flip(self.image,True,False)

    def update(self):
        self.position += self.vel
        self.rect.midbottom = self.position

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