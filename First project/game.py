import pygame
from pygame.locals import *
import gameobject
import component

# initilize window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
component.SpriteRenderer.screen = screen

#loading assets
petr = pygame.image.load("First project/Assets/Sprites/Petr/PetrBase.png")
obj = gameobject.Gameobject("Petr")
obj.add_componenet(component.SpriteRenderer(petr))
petr_position = (100, 100)

#game loop
while True:
    #clear screen
    screen.fill(0)

    #render petr
    component.SpriteRenderer.render_all()

    #show render
    pygame.display.flip()
    
    #check for game window close
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)

        if event.type == pygame.KEYDOWN:
            pass    

