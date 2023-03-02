import random
import pygame
from pygame import *
import math
from pygame.locals import *
import sys
import player,enemy,bullet,musgo,boss

pygame.init()

ALTURA=1080
ANCHURA=1920

size= (ANCHURA,ALTURA)


#COLORES
BLANCO=(255,255,255)
GRIS= (240,240,240)
NEGRO= (0,0,0)


screen= pygame.display.set_mode(size)
pygame.display.set_caption("DIEP.IO")
#fondo

player= player.Player()
boss= boss.Boss()

enemies= pygame.sprite.Group()
bullets= pygame.sprite.Group()
musgos= pygame.sprite.Group()

def crearEnemigo():
    e= enemy.Enemy()
    e.rect.x=random.randint(0,ANCHURA-30)
    e.rect.y=random.randint(0,ALTURA-30)
    e.image= transform.rotate(e.image,random.randint(0,360))
    e.image.set_colorkey((0,0,0))
    
    enemies.add(e)
def crearMusgo():
    m= musgo.Musgo()
    m.rect.x=random.randint(0,ANCHURA-70)
    m.rect.y=random.randint(0,ALTURA-70)
    musgos.add(m)

for i in range(10):
    crearEnemigo()

for i in range(5):
    crearMusgo()

def draw_score(screen, score):
	font = pygame.font.SysFont("serif", 50)
	text_surface = font.render("Score: " + str(score), True, NEGRO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (500,0)
	screen.blit(text_surface, text_rect)

def draw_menu(screen,alpha):
    font = pygame.font.SysFont("serif", 40)
    text_surface = font.render(" WASD para moverse y MOUSE para disparar", True, (100,100,100))
    text_rect = text_surface.get_rect()
    text_rect = (200,200)
    screen.blit(text_surface, text_rect)

    text_surface = font.render("Pulsa 'ESPACIO' para empezar la partida", True, (100,100,100))
    text_surface.set_alpha(alpha)
    #print(text_surface.get_alpha())   
    text_rect = text_surface.get_rect()
    text_rect = (200,600)
    screen.blit(text_surface, text_rect)

def mostrarVida(vida):
    vida_rect_atras=pygame.draw.rect(screen,(255,0,0),(10,10,100,30))
    vida_rect=pygame.draw.rect(screen,(0,255,0),(10,10,vida,30))  

def resetPartida():
    player.derecha=False
    player.izquierda=False
    player.arriba=False
    player.abajo=False

    player.rect.x=500
    player.rect.y=350

    boss.rect.x=900
    boss.rect.y=100

    enemies.empty()
    musgos.empty()
    bullets.empty()

    for i in range(10):
        crearEnemigo()

    for i in range(5):
        crearMusgo()

    
terminado=False
while not terminado:
    #pygame.time.delay(20)
    # ---- Presentacion ----
    screen.fill( GRIS)
    # Nuevo 0.09
    
    alpha=20
    alpha_vel=15
    entrarAlJuego = False
    while not entrarAlJuego:
        pygame.time.wait(100)
        for event in pygame.event.get(KEYUP):
            if event.key == K_SPACE:
                entrarAlJuego = True

        if alpha >= 255 or alpha <= 15:
            alpha_vel *= -1
            #print("cambia")
        alpha += alpha_vel  
        screen.fill( GRIS)  
        draw_menu(screen,alpha)
        pygame.display.flip()


    # ---- PARTIDA ---- 
 
    gameOver = False
    score=0
    vida=100
    disparando=False
    ultimoDisparo= pygame.time.get_ticks()
    resetPartida()
    while not gameOver:
        for event in pygame.event.get():
            #print(event)
            
            if event.type== pygame.QUIT:
                sys.exit()

            # CON WASD
            if event.type == pygame.KEYDOWN:
                
                #derecha
                if event.key == pygame.K_d:
                    player.derecha= True
                #izquierda
                if event.key == pygame.K_a:
                    player.izquierda= True
                #arriba
                if event.key == pygame.K_w:
                    player.arriba= True
                #abajo
                if event.key == pygame.K_s:
                    player.abajo= True

            if event.type == pygame.KEYUP:
                
                #derecha
                if event.key == pygame.K_d:
                    player.derecha= False
                #izquierda
                if event.key == pygame.K_a:
                    player.izquierda= False
                #arriba
                if event.key == pygame.K_w:
                    player.arriba= False
                #abajo
                if event.key == pygame.K_s:
                    player.abajo= False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                disparando=True
            if event.type == pygame.MOUSEBUTTONUP:
                disparando=False

        
        #rotacion del cañon
        mx,my=pygame.mouse.get_pos()
        px=player.rect.x
        py=player.rect.y
        vectorPos= pygame.math.Vector2(mx-px,my-py)
        
        #print("vx: "+ str(vectorPos.x))
        #print("vy: "+ str(vectorPos.y))
    
        pendiente=vectorPos.y/(vectorPos.x+0.1)
        angulo= math.degrees(math.atan(pendiente))
        #print(angulo)
        
        if(vectorPos.x<0):
            if (vectorPos.y<0):
                angulo+=180
                #print("segundo cuadrante: " + str(angulo))
            else:
                angulo +=180
            
        else:
            angulo += 360
        #print("angulo: " + str(angulo))
        canon=pygame.transform.rotate(player.image,-angulo)
        #canon_rect = player.image.get_rect()
        #print(player.rect)


        if disparando:
            #controlar cadencia
            ahora= pygame.time.get_ticks()
            if ahora - ultimoDisparo > bullet.cadencia:
                mousePos=pygame.mouse.get_pos()
                mouseX=mousePos[0]
                mouseY=mousePos[1]

                #rectenadas del player
                px=player.rect.x
                py=player.rect.y
                #crear bullet
                bul=bullet.Bullet(px+30,py+30)

                #calculamos vector posicion
                vectorPos= pygame.math.Vector2(mouseX-px,mouseY-py)
                #print(vectorPos)
                vnor=vectorPos.normalize()
                #print(vnor)
                bul.vx=vnor.x
                bul.vy=vnor.y
                #print(bul.vx,bul.vy)

                bullets.add(bul)
                ultimoDisparo=ahora

        #dibujar las balas
        for bullet1 in bullets:
            #comprobar si estan fuera del limite, para eliminarlos
            if bullet1.rect.x <0 or bullet1.rect.x > ANCHURA+15 or bullet1.rect.y <0 or bullet1.rect.y > ALTURA+15:
                bullet1.kill()
            else:
                bullet1.mover()

        player.mover(ALTURA,ANCHURA)
        boss.mover(player.rect.x,player.rect.y)
        
        hits= pygame.sprite.groupcollide(bullets,enemies,True,True)
        if hits:
            score +=1
            print("Score: " + str(score))
            #añadir otro enemigo
            crearEnemigo()

        damage= pygame.sprite.spritecollide(player,musgos,False)
        if damage:
            vida -= 0.5
            print("VIDA: " + str(vida))
            if (vida<=0):
                gameOver=True
                print("GAME OVER...")        
        
        for e in enemies:
            e.flotar()


        # DIBUJAR OBJETOS
        screen.fill(GRIS)
        enemies.draw(screen)
        bullets.draw(screen)
        musgos.draw(screen)
        mostrarVida(vida)
        draw_score(screen,score)
        screen.blit(canon,player.rect)
        screen.blit(boss.image,boss.rect)


        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    print("PROGRAMA ACABADO !!")
    

   
    