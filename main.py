import pygame, sys
from pygame.locals import QUIT
import random
import time

pygame.init()

DISPLAY = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Chrome Dino')
score = 0
score = "SCORE:", score

# colors
RED = (200, 0, 0)

class Cactus:

    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l
        self.cactus = pygame.draw.rect(DISPLAY,"green",(150,220,30,30))

cactus1 = Cactus(150,220,30)
cactus2 = Cactus(350,210,40)
cactus3 = Cactus(550,200,50)

cacti = [cactus1,cactus2,cactus3]

clock = pygame.time.Clock()

def shiftcactus():
    for cactus in cacti:
        cactus.x -= 1
        
        if cactus.x < 0:
            cactus.x = 600

while True:
    clock.tick(60)
    DISPLAY.fill(RED)
    pygame.draw.rect(DISPLAY,"white",(0,250,600,500))
    pygame.draw.rect(DISPLAY,"black",(30,185,30,65))
    
    pygame.draw.rect(DISPLAY,"green",(cactus1.x,cactus1.y,30,30))
    pygame.draw.rect(DISPLAY,"green",(cactus2.x,cactus2.y,30,40))
    pygame.draw.rect(DISPLAY,"green",(cactus3.x,cactus3.y,30,50))
    shiftcactus()
    pygame.display.update()