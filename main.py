import pygame, sys
from pygame.locals import QUIT

pygame.init()
pygame.mixer.init()

jumpSound = pygame.mixer.Sound("jump.mp3")

DISPLAY = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Chrome Dino')

game = "playing"

dino_img = pygame.transform.scale(pygame.image.load("dino.png"),(30,65))
cactus_img = pygame.image.load("Cactus.png")
cactus_img = pygame.transform.scale(cactus_img,(40,30))
cactus_img2 = pygame.transform.scale(cactus_img,(40,40))
cactus_img3 = pygame.transform.scale(cactus_img,(40,45))

cacti_img = [cactus_img,cactus_img2,cactus_img3]

font = pygame.font.SysFont("Times New Roman",25)
bigFont = pygame.font.SysFont("Times New Roman" , 40)

LosingText = bigFont.render("GAME OVER",False, "black")

# colors
RED = (200, 0, 0)

class Cactus: 
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l
        
class Dino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jumping = False
        self.coming_down = False
        self.float = False
        self.float_energy = 0
        self.condition = "alive"
        self.score = 0

    def jump(self):
        self.jumping = True

    def come_down(self):
        self.coming_down = True
        
dino = Dino(30,185)

cactus = Cactus(150,220,30)
cactus2 = Cactus(350,210,40)
cactus3 = Cactus(550,205,45)

cacti = [cactus,cactus2,cactus3]

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
                if not dino.coming_down:
                    pygame.mixer.Sound.play(jumpSound)
                    dino.jump()

def collision():
    for cactus in cacti:
        if abs(dino.x - cactus.x) <= 10:
            if dino.y + 85 > cactus.y:
                dino.condition = "dead"

def handle_dino():
    if dino.jumping:
        dino.y-=1
    if dino.y < 120:
        dino.jumping = False
        dino.float = True
    if dino.float:
        dino.float_energy += 1
        if dino.float_energy > 10 :
            dino.float = False
            dino.come_down()
            dino.float_energy = 0
    if dino.coming_down:
        dino.y+=1
    if dino.y >= 185:
        dino.coming_down = False
    
clock = pygame.time.Clock()

while True:
    clock.tick(150)
    DISPLAY.fill("white")
    pygame.draw.rect(DISPLAY,"black",(0,250,600,10))
    DISPLAY.blit(dino_img,(dino.x,dino.y))
    for index,cactus in enumerate(cacti):
        DISPLAY.blit(cacti_img[index],(cactus.x,cactus.y))

    shiftcactus()
    controlDino()
    handle_dino()
    collision()
    if dino.condition == "dead":
        DISPLAY.fill("white")
        ScoreText = font.render(f"Score:{dino.score}",False, "black")
        DISPLAY.blit(ScoreText,(10,65))
        DISPLAY.blit(LosingText,(10,20))
    else:
        dino.score += 1
    
    pygame.display.update()