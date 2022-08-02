#where all the global constants are kept allowing me to easily change any of the values and have them change for the entire project
from pygame import Vector2



#game window
WINDOW_WITDTH = 800
WINDOW_HEIGHT = 400

#colours 
BACKGROUNDCOLOUR = (40,53,59)
TEXTCOLOUR = (0,0,0)
BLACK = (0,0,0)


#Frames per second
FPS = 30

#game world physics
GRAVITY = Vector2(0,1)
FRIC = 0.14 #Friction

#player stuff
JUMP_STRENGTH = Vector2(0,-15)
MOVE_STRENGTH =  Vector2(1.5,5)
PLAYER_HEALTH = 3

#monster stuff
MONSTER_SPEED = -5


