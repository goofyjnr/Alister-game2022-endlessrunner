#where all the global constants are kept allowing me to easily change any of the values and have them change for the entire project
from pygame import Vector2

#game window
WINDOW_WITDTH = 800
WINDOW_HEIGHT = 400

#colours 
BACKGROUNDCOLOUR = (130, 202, 225)


#Frames per second
FPS = 30

#game world physics
GRAVITY = Vector2(0,0.4)
FRIC = 0.08 #Friction