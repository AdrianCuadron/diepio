import pygame
from pygame.locals import *
from pygame import *

class Boss(pygame.sprite.Sprite):
   
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("images/boss.png")
        self.image= transform.scale(self.image,(100,100))
        
        self.rect = self.image.get_rect()
        self.rect.x=900
        self.rect.y=100

        self.vx=1
        self.vy=1
        self.vel=4

    def mover(self,px,py):
        vectorPos= pygame.math.Vector2(px-self.rect.x+0.1,py-self.rect.y)
        #print(vectorPos)
        vnor=vectorPos.normalize()
        print(vnor)
        self.vx=round(vnor.x)
        self.vy=round(vnor.y)


        self.rect.x += self.vx*self.vel
        self.rect.y += self.vy*self.vel