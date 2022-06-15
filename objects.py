#This is where all the classes will be kept to make easy changes to them and to keep them all in one place

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
        
class Text(Sprite):
    def __init__(self, text, size, position, *groups) -> None:
        super().__init__(*groups)
        self.text = text
        self.position = Vector2(position)
        self.font = Font(None,size)
        self.image = self.font.render(self.text,True,TEXTCOLOUR)
        self.rect = self.image.get_rect(midbottom=position)

    def update(self):
        self.image = self.font.render(self.text,True,TEXTCOLOUR)
        self.rect = self.image.get_rect(midbottom=self.position)

class Player(Physics):
    def __init__(self, position, width, height, image="Assets/chara.png"):
        super().__init__(position, width, height, image)
        self.jumping = False #sets it up so can jump the first time
        self.jump_count = 0
        self.score = 0
        self.health = PLAYER_HEALTH

    def move(self,direction):
        if direction == "left":
            self.vel.x -= MOVE_STRENGTH.x
        elif direction == "right":
            self.vel.x += MOVE_STRENGTH.x
        elif direction =="down":
            self.vel.y += MOVE_STRENGTH.y
    
    def jump(self):
        if self.jumping == False and self.jump_count < 2:
            self.vel.y =0
            self.jump_count = self.jump_count + 1
            self.vel += JUMP_STRENGTH
        elif self.jump_count == 2:
            self.jumping = True

    
        

class Monster(Physics):
    def __init__(self, position, width, height, image="Assets/monster.png"):
        super().__init__(position, width, height, image)
        self.image = flip(self.image,True,False)
        self.vel = Vector2(-3,0)
    def update(self):
        self.vel += GRAVITY
        self.position += self.vel
        self.rect.midbottom = self.position



class Platform(Physics):
    def __init__(self, position, width, height, image="Assets/platform.png"):
        super().__init__(position, width, height, image)
        self.vel = Vector2((0,0))
    def update(self):
        self.position += self.vel
        self.rect.midbottom = self.position

class Background(Drawable):
      def __init__(self, position, width, height, image="Assets/background.png"):
        super().__init__(position, width, height, image)
        self.bgimage = scale(load(image),(width,height))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 1
         
      def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
             
      def render(self,window):
         window.blit(self.bgimage, (self.bgX1, self.bgY1))
         window.blit(self.bgimage, (self.bgX2, self.bgY2))

class Coin(Physics):
    pass

class Powerup(Physics):
    pass