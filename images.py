#---------------------------------------------------------------------------------------------------------------
# Name     : images.py
# Purpose  : images
# Author   : puviyarasu.p
# Created  : 28-05-2020
#---------------------------------------------------------------------------------------------------------------
import pygame,sys,os#images impoting work so etha sys add panniruku
pygame.init()

background = pygame.image.load(os.path.join('images','sea.png'))
outline = pygame.image.load(os.path.join('images','grass.png'))
inner = pygame.image.load(os.path.join('images','dirt.png'))
player = pygame.image.load(os.path.join('images','player.png'))
box1 = pygame.image.load(os.path.join('images','box1.png'))
box2 = pygame.image.load(os.path.join('images','box2.png'))
box3 = pygame.image.load(os.path.join('images','box3.png'))
box4 = pygame.image.load(os.path.join('images','box4.png'))
con_list=[pygame.image.load(os.path.join('images','c1.png')),pygame.image.load(os.path.join('images','c2.png')),pygame.image.load(os.path.join('images','c3.png')),pygame.image.load(os.path.join('images','c4.png')),pygame.image.load(os.path.join('images','c5.png')),pygame.image.load(os.path.join('images','c6.png'))]
door=[
pygame.image.load(os.path.join('images','d1.png')),pygame.image.load(os.path.join('images','d2.png')),pygame.image.load(os.path.join('images','d3.png')),pygame.image.load(os.path.join('images','d4.png')),
pygame.image.load(os.path.join('images','d5.png')),pygame.image.load(os.path.join('images','d6.png')),pygame.image.load(os.path.join('images','d7.png')),pygame.image.load(os.path.join('images','d8.png')),
pygame.image.load(os.path.join('images','d9.png')),pygame.image.load(os.path.join('images','d10.png')),pygame.image.load(os.path.join('images','d11.png')),pygame.image.load(os.path.join('images','d12.png')),
pygame.image.load(os.path.join('images','d13.png')),pygame.image.load(os.path.join('images','d14.png')),pygame.image.load(os.path.join('images','d15.png')),pygame.image.load(os.path.join('images','d16.png')),
pygame.image.load(os.path.join('images','d17.png')),pygame.image.load(os.path.join('images','d18.png')),pygame.image.load(os.path.join('images','d19.png')),pygame.image.load(os.path.join('images','d20.png'))]
win_back = pygame.image.load(os.path.join('images','win.png'))
