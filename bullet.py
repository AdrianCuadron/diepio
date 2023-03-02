import pygame
from pygame import *


cadencia=500
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load("images/Nave.png").convert()
        self.image= transform.scale(self.image,(25,25))
        self.image.set_colorkey((0,0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vel=10
        
        self.vx=1
        self.vy=1

    def mover(self):
        self.rect.x += self.vx*self.vel
        self.rect.y += self.vy*self.vel

        #self.rect.x += 1
        #self.rect.y += 9