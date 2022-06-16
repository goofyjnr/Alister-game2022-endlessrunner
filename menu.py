from config import *
from objects import *
from startup import *

menu_ui = pygame.sprite.Group()

def main_menu():
    global game
    pygame.display.set_caption("Main menu")

    menu = True
    while menu:
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == QUIT:
                menu = False
            elif event.type == KEYDOWN:
                #if ESC key gets pressed
                if event.key == K_ESCAPE:
                    menu = False #if the escape key is pressed quit the game.
                elif event.key == K_g:
                    game()
                

        Menu_text = Text("Menu",80,(WINDOW_WITDTH/2,WINDOW_HEIGHT/2-100), menu_ui)

        window.fill((255,255,255))
        all_sprites.update()

        for sprite in menu_ui:
            window.blit(sprite.image,sprite.rect)

        pygame.display.update()



