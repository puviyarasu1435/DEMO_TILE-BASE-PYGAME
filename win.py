#---------------------------------------------------------------------------------------------------------------
# Name     : maping.py
# Purpose  : blit map
# Author   : puviyarasu.p
# Created  : 29-05-2020
#---------------------------------------------------------------------------------------------------------------
import pygame, sys,os #images impoting work so etha sys add panniruku
import pygame, sys,os #images impoting work so etha sys add panniruku
from pygame.locals import * #local events
import images as img
#---------------------------------------------------------------------------------------------------------------
pygame.init()#pygame starting
clock = pygame.time.Clock()#loop speed
pygame.display.set_caption('GAME')
large = pygame.font.Font("ALGER.TTF", 80)

winsize = (1000,600)#window size

screen = pygame.display.set_mode(winsize,0,32) #normal window

display = pygame.Surface((winsize)) #pygame surface

while True:
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display.blit(img.win_back,(0,0))
    scorebord = large.render("win!", True, (250,250,250))
    display.blit(scorebord,(400,200))
    screen.blit(pygame.transform.scale(display,winsize),(0,0))
    pygame.display.update()
    clock.tick(70)
