import pygame
import os
import random
from component import *
from method import *

pygame.init()
#H+W Screen
Width = 1920
Height = 1080

#Color
Pink = (255,153,204)
RED = (255,0,0)
White = (255,255,255)
Black = (0,0,0)
Darkslateblue = (72,61,139)
Indigo = (75,0,130)
Rebeccapurple = (102,51,153)
game_folder = os.path.dirname(__file__)
img_folder = "./src/GAME/seeker"
direction = 0
FPS = 30
clock = pygame.time.Clock()
background_pic = os.path.join(img_folder,'MC','2x','x2.jpeg')
all_sprites = pygame.sprite.Group()
enemy = pygame.sprite.Group()
hps = pygame.sprite.Group
attack_effects = pygame.sprite.Group()

class Seeker(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Seeker_idle = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        self.image = pygame.image.load(Seeker_idle).convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = Width / 2
        self.rect.bottom = Height / 2

    def update(self):
        Seeker_left = os.path.join(img_folder,'MC','x3','ไฟล์_001.png')
        Seeker_right = os.path.join(img_folder,'MC','x3','ไฟล์_000.png')
        Seeker_up = os.path.join(img_folder,'MC','x3','ไฟล์_003.png')
        Seeker_down = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        self.speedx =0
        self.speedy =0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.image = pygame.image.load(Seeker_left).convert()
            self.image.set_colorkey(Black)
            self.speedx = -5
        
        if keystate[pygame.K_d]:
            self.image = pygame.image.load(Seeker_right).convert()
            self.image.set_colorkey(Black)
            self.speedx = 5
            
        if keystate[pygame.K_s]:
            self.image = pygame.image.load(Seeker_down).convert()
            self.image.set_colorkey(Black)
            self.speedy = 5
            
        if keystate[pygame.K_w]:
            self.image = pygame.image.load(Seeker_up).convert()
            self.image.set_colorkey(Black)
            self.speedy = -5

        
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > Width + 10:
            self.rect.right = Width + 10
        
        if self.rect.left < -10:
            self.rect.left = -10
        
        if self.rect.top < 4:
            self.rect.top = 4
        
        if self.rect.bottom > Height:
            self.rect.bottom = Height

    def attack(self):
        attack =Attack_effect(self.rect.centerx,self.rect.top)
        all_sprites.add(attack)
        attack_effects.add(attack)



        
class Leaderboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill(Indigo)
        self.rect = self.image.get_rect()
        self.rect.right = 180
        self.rect.top = 260
class HP1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 300
        self.rect.bottom = 200

class HP2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 360
        self.rect.bottom = 200

class HP3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 420
        self.rect.bottom = 200

def lose_hp(char_hit_count , hp1 , hp2 , hp3):
    if char_hit_count == 1:
        hp1.image.fill(Black)
    elif char_hit_count == 2:
        hp2.image.fill(Black)
    elif char_hit_count == 3:
        hp3.image.fill(Black)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50,90))
        #self.image.fill(RED)
        Enemy_idle = os.path.join(img_folder,'SLIME_IDLE.png')
        self.image = pygame.image.load(Enemy_idle).convert()
        self.image.set_colorkey(Black)
        self.rect =self.image.get_rect()
        self.rect.top = random.randrange(169,900)
        self.rect.centerx = random.randrange(267,1500) 
    
    

class Attack_effect(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((90,20))
        self.image.fill(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -5

    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill

#font = pygame.font.SysFont("comicsansms", 20)
#Score_p1 = font.render("Hello, World", True, (0, 128, 0))


def main(argument) :
    
    background = Object(pygame.image.load(background_pic) , CENTER_X , CENTER_Y)
    
    char_hit_status = False
    char_hit_count = 0

    wave = 1
    score_p1 = 0

    seeker = Seeker()
    all_sprites.add(seeker)
    leaderboard = Leaderboard()
    all_sprites.add(leaderboard)

    hp1 = HP1()
    all_sprites.add(hp1)
    hps.add(hp1)
    hp2 = HP2()
    all_sprites.add(hp2)
    hps.add(hp2)
    hp3 = HP3()
    all_sprites.add(hp3)
    hps.add(hp3)


    Game_running = True
    em_count = 0


    for i in range(5):
        em = Enemy()
        all_sprites.add(em)
        enemy.add(em)
        em_count += 1
    while Game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    seeker.attack()
                if event.key == pygame.K_t:
                    print("mic on")


        
        
        all_sprites.update()
        hits_em = pygame.sprite.groupcollide(enemy,attack_effects,True,True)
        if hits_em:
            if hits_em:
                em_count -= 1
                score_p1 += 50
            if em_count <= 0:
                wave += 1
                for i in range(5*wave):
                    em = Enemy()
                    all_sprites.add(em)
                    enemy.add(em)
                    em_count += 1

       

        #check HP if HP run out,seeker will die
        
        if pygame.sprite.spritecollide(seeker,enemy,False):
            if not char_hit_status :
                char_hit_status = True
                char_hit_count += 1
                lose_hp(char_hit_count , hp1 , hp2 , hp3)
                score_p1 -= 100
        else :
            char_hit_status = False
        
        if char_hit_count >= 3:
            link_to('menu')
            Game_running=False
            
           
        clock.tick(FPS)
        
        background.draw()
        #screen.blit(Score_p1,250,250)

        all_sprites.draw(screen)
        pygame.display.update()