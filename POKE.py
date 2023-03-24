import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

Largura = 640
Altura = 480
x = Largura/2
y = Altura/2


tela = pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption('DEV - Pokemon')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20    
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
    
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))




    pygame.display.update()


