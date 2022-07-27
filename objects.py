#This is where all the classes will be kept to make easy changes to them and to keep them all in one place

from config import *
from pygame.sprite import Sprite, spritecollide
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import scale, flip
from pygame.font import Font
from pygame.mouse import get_pos, get_pressed
from pygame.surface import Surface
from pygame.time import *
import pygame



class Drawable(Sprite):
    """Drawable class as a base for everything that needs to be drawn to the screen"""
    def __init__(self,position,width,height,image = "Assets/chara.png"):
        super().__init__()

        self.position = Vector2(position)
        self.image = scale(load(image),(width,height))
        self.image.set_colorkey((70,60,78))

        self.rect = self.image.get_rect(midbottom=position)

class Physics(Drawable):
    """Class for objects that require movment or any physics based things inherits from Drawable"""
    def __init__(self, position, width, height, image = "Assets/chara.png"):
        super().__init__(position, width, height, image)

        self.vel = Vector2((0,0))

    def update(self):
        #Basic update function for all things on the window
        self.vel += GRAVITY
        self.vel.x -= self.vel.x * FRIC
        self.position += self.vel
        self.rect.midbottom = self.position
        
class Text(Sprite):
    """Class for all the text based objects"""
    def __init__(self, text, position, font,  *groups) -> None:
        super().__init__(*groups)
        self.text = text
        self.position = Vector2(position)
        self.font = font
        self.image = self.font.render(self.text,True,TEXTCOLOUR)
        self.rect = self.image.get_rect(midbottom=position)

    def update(self):
        #different update for text
        self.image = self.font.render(self.text,True,TEXTCOLOUR)
        self.rect = self.image.get_rect(midbottom=self.position)

class SpriteSheet():
    """Class for handling the sprite sheets alowing for character animation"""
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        #gets the sprite sheet and puts the whole thing on to the screen
        image = Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), (((frame * width)), 0, width, height))
        image = pygame.transform.scale (image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
        

class Player(Physics):
    """Class to set up the player and all the things it needs to do i.e. movement inherits from Physics"""
    def __init__(self, position, width, height, image = "Assets/chara.png"):
        super().__init__(position, width, height, image,)
        self.jumping = False #sets it up so can jump the first time
        self.jump_count = 0
        self.score = 0
        self.health = PLAYER_HEALTH
        self.playeralive = True

        #sprite sheet and animation stuff
        
        self.sprite_sheet_image = pygame.image.load('Assets/sprite_sheet.png').convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)

        self.animation_list = []
        self.animation_steps = [5, 1]
        self.action = 0
        self.last_update = get_ticks()
        self.animation_cooldown = 125
        self.frame = 0
        self.step_counter = 0

        for animation in self.animation_steps:
            temp_image_list = []
            for _ in range(animation):
                temp_image_list.append(self.sprite_sheet.get_image(self.step_counter, 11, 8, 5, (0,0,0)))
                self.step_counter += 1
            self.animation_list.append(temp_image_list)

    def move(self,direction):
        #player movment
        if direction == "left":
            self.vel.x -= MOVE_STRENGTH.x
        elif direction == "right":
            self.vel.x += MOVE_STRENGTH.x
        elif direction =="down":
            self.vel.y += MOVE_STRENGTH.y
    
    def jump(self):
        #player jumping
        if self.jumping == False and self.jump_count < 2:
            self.vel.y =0
            self.jump_count = self.jump_count + 1
            self.vel += JUMP_STRENGTH
        elif self.jump_count == 2:
            self.jumping = True

    def colision_with_platforms(self,platforms):
        #player and platform colision
        player_hits_platforms = spritecollide(self,platforms,False)
        if len(player_hits_platforms) != 0:
            if self.vel.y > 0 and self.position.y < player_hits_platforms[0].rect.bottom:
                self.vel.y = 0 
                self.position.y = player_hits_platforms[0].rect.top 
                self.jumping = False #resets it so after you touch a platform you can jump again
                self.jump_count = 0

    def player_offscreen(self):
         #stops the player from going off screen
        if self.position.x < 0:
            self.vel = Vector2(0,0)
            self.position.x = self.position.x+3       
        if self.position.x > WINDOW_WITDTH-200:
            self.vel = Vector2(0,0)
            self.position.x = self.position.x-1
        if self.position.y < 0 :
            self.vel = Vector2(0,0)
            self.position.y = self.position.y+3

    def restart(self,position):
        #resets player to beginging position
        self.jumping = False
        self.jump_count = 0 
        self.score = 0
        self.health = PLAYER_HEALTH
        self.position = Vector2(position)
        self.playeralive= True

    def update(self):
        #Update function for the player
        self.vel += GRAVITY
        self.vel.x -= self.vel.x * FRIC
        self.position += self.vel
        self.rect.midbottom = self.position

        #sprite sheet and animation stuff
        #frame_0 = self.sprite_sheet.get_image(1, 100, 121, 1, (30,0,30))
        current_time = get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
                
        self.image = self.animation_list[self.action][self.frame]
        
    

    
        

class Monster(Physics):
    """Class to set up the monster inherits inherits from Physics"""
    def __init__(self, position, width, height, image = "Assets/monster/1.png"):
        super().__init__(position, width, height, image)
        
        self.vel = Vector2(-3,0)
    def update(self):
        #different update for monsters allows for movment and gravity
        self.vel += GRAVITY
        self.position += self.vel
        self.rect.midbottom = self.position

    def colision_with_platforms(self,platforms):
        #monster and platform colision
        monster_hits_platforms = spritecollide(self,platforms,False)
        if len(monster_hits_platforms) != 0 :
            if self.vel.y > 0:
                self.vel.y = 0
                self.position.y = monster_hits_platforms[0].rect.top 
    

    def restart(self,position):
        self.vel = Vector2(-3,0)
        self.position = Vector2(position)




class Platform(Physics):
    """Class for the setting up the platforms inherits from Physics"""
    def __init__(self, position, width, height, image = "Assets/platform.png"):
        super().__init__(position, width, height, image)
        self.vel = Vector2((0,0))
    def update(self):
        #different update for Platforms that allows for movment with out gravity
        self.position += self.vel
        self.rect.midbottom = self.position

class Background(Drawable):
    """Class to set up the background that moves across the screen in a loop inherits from Drawable"""
    def __init__(self, position, x, y, width, height, image="Assets/background.png"):
        super().__init__(position, width, height, image)
        self.bgimage = scale(load(image),(width,height))
        self.rectBGimg = self.bgimage.get_rect()
        

        self.bgY1 = y
        self.bgX1 = x

        self.bgY2 = y
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 1
    def update(self):
        #different update for the Moving background
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
    def render(self,window):
        window.blit(self.bgimage, (self.bgX1, self.bgY1))
        window.blit(self.bgimage, (self.bgX2, self.bgY2))

#button class
class Button(Drawable):
    """Class to set up Buttons on the screen and allow for mouse dection on them inherits from Drawable"""
    def __init__(self, position, width, height, image = "Assets/start.png"):
        super().__init__(position, width, height, image)

        self.clicked = False 


    def draw(self, window):
        #draws the buttons to the screen and checks for mouse imputs 
        action = False
        #get mouse position
        pos = get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if get_pressed()[0] == 0:
            self.clicked = False
        #draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))

        return action
