import pygame
from pygame.locals import *
from pygame import *

class Musgo(pygame.sprite.Sprite):
   
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("images/musgo.png")
        self.image= transform.scale(self.image,(70,70))
        
        self.rect = self.image.get_rect()
        self.vel=3

    def mover(self):
        self.rect.x += self.vx*self.vel
        self.rect.y += self.vy*self.vel