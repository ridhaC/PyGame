import pygame
from pygame.locals import *
import gameobject

# initilize window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#loading assets
petr = pygame.image.load("First project/Assets/Sprites/Petr/PetrBase.png")
petr = pygame.transform.scale(petr, (7*4, 16*4))
petrPosition = [100, 100]
velocity = [0, 0]
#game loop
while True:
    #clear screen
    screen.fill(0)

    #render petr
    screen.blit(petr, tuple(petrPosition))
    velocity[1] += 0.001
    petrPosition[0] += velocity[0]
    petrPosition[1] += velocity[1]

    #show render
    pygame.display.flip()
    
    #check for game window close
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                velocity[0] = -1
            if event.key == pygame.K_d:
                velocity[0] = 1

