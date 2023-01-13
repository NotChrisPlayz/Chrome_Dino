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

class Dino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jumping = False
        self.coming_down = False
        self.float = False
        self.dino = pygame.draw.rect(DISPLAY,"black",(30,185,30,65))

    def jump(self):
        self.jumping = True

    def come_down(self):
        self.coming_down = True
        #self.y += 10
        
dino = Dino(30,185)

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

def controlDino():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump()

def collision():
    for cactus in cacti:
        if abs(dino.x - cactus.x) <= 10:
            print (dino.y +85, cactus.y)
            if dino.y + 85 > cactus.y:
                DISPLAY.fill("black")
    

float = 0

while True:
    clock.tick(60)
    DISPLAY.fill(RED)
    pygame.draw.rect(DISPLAY,"white",(0,250,600,500))
    pygame.draw.rect(DISPLAY,"black",(dino.x,dino.y,30,65))
    for cactus in cacti:
        pygame.draw.rect(DISPLAY,"green",(cactus.x,cactus.y,30,cactus.l))
    shiftcactus()
    controlDino()
    if dino.jumping:
        dino.y-=1
    if dino.y < 120:
        dino.jumping = False
        dino.float = True
    if dino.float:
        float += 1
        if float > 50:
            dino.float = False
            dino.come_down()
            float = 0
    if dino.coming_down:
        dino.y+=1
    if dino.y >= 185:
        dino.coming_down = False
    collision()
    pygame.display.update()