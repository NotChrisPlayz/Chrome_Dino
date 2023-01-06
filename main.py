import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()

DISPLAY = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Chrome Dino')
score = 0
score = "SCORE:", score

# colors
RED = (200, 0, 0)

class Ground:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ground = pygame.draw.rect(DISPLAY,"white",(0,250,600,500))


#Ground.x = 0
#Ground.y = 250

#def shiftGround():
 #   for road in roads:
  #      road.y += 1
   #     if road.y > 400:
    #        road.y = -road.road.get_height()

while True:
    DISPLAY.fill(RED)
    DISPLAY.blit(ground.ground, (0, ground.y))
    pygame.draw.rect(DISPLAY,"black",(30,185,30,65))
    pygame.draw.rect(DISPLAY,"green",(150,220,30,30))
    pygame.draw.rect(DISPLAY,"green",(350,210,30,40))
    pygame.draw.rect(DISPLAY,"green",(550,200,30,50))
    pygame.display.update()