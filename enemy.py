import random
from pygame import *
from pygame.locals import *
import pygame

class Enemy(pygame.sprite.Sprite):
   
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("images/enemySquare.png")
        self.image= transform.scale(self.image,(30,30))
        
        self.rect = self.image.get_rect()
    
    def flotar(self):
        self.rect.x +=random.randint(-1,1)
        self.rect.y +=random.randint(-1,1)
