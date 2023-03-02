from pygame import *
from pygame.locals import *
import pygame

class Player(pygame.sprite.Sprite):
   
    def __init__(self):
        super().__init__()
        self.image= image.load("images/Canon.png").convert()
        self.image= transform.scale(self.image,(70,70))
        self.image= transform.rotate(self.image,-90)
        self.image.set_colorkey((0,0,0))
        
        self.rect = self.image.get_rect()

        self.vel=3

        

        self.derecha=False
        self.izquierda=False
        self.arriba=False
        self.abajo=False

        

    def mover(self,altura,anchura):
        
        #comprobar izquierda
        if self.izquierda and not self.derecha and self.rect.x > 0:
            #sumar velocidad izquierda
            self.rect.x -= self.vel
        #comprobar derecha
        if self.derecha and not self.izquierda and self.rect.x < anchura-50:
            #sumar velocidad derecha
            self.rect.x += self.vel
        #comprobar arriba
        if self.arriba and not self.abajo and self.rect.y > 0:
            #sumar velocidad arriba
            self.rect.y -= self.vel
        #comprobar abajo
        if self.abajo and not self.arriba and self.rect.y < altura-50:
            #sumar velocidad abajo
            self.rect.y += self.vel
        