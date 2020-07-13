import pygame
import random

import PIL

from pygame.locals import *
import sys
pygame.init()
font=pygame.font.Font('Candarab.ttf', 32)
clock = pygame.time.Clock()
crashed = False
carImgs = pygame.image.load('E.png')
display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Echart')
black = (0, 0, 0)
white = (255, 255, 255)

def draw_text(text,font,color,surface,x,y):
    textobj=font.render(text,20,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def main_menu():
    y=0
    gameDisplay.fill(white)
    draw_text('main_menu',font,black,gameDisplay,10,0)
    boutton1=pygame.Rect(100,100,100,20)
    pygame.draw.rect(gameDisplay,(250,00,00),boutton1)
    pygame.display.update()
    runing=True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    runing = False
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_0:
                    runing = False
                if event.key == pygame.K_1:
                    E()
                if event.key == pygame.K_2:
                    E2()
                if event.key == pygame.K_3:
                    y=y+1
                    if(y==4):
                        y=1
                        lineE(y)
                    lineE(y)
                if event.key == pygame.K_4:
                    y=y+1
                    if(y==4):
                        y=1
                        lineEBW(y)
                    lineEBW(y)
                if event.key==pygame.K_5:
                    redgreen()
def lineEBW(y):
    print(y)
    s=4
    s=s-y
    E=[]
    list=[]
    gameDisplay.fill(black)
    while len(list)!=4:
        r = random.randrange(0, 360, 90)
        if r not in list:
            list.append(r)
            Eimag = pygame.transform.scale(carImgs,(s*90, s*90))
            Eimag_c=Eimag.get_rect().center
            Eimag = pygame.transform.rotate(Eimag, r)
            print(Eimag_c)




            E.append(Eimag)
    t=random.randrange(0, 4, 1)
    print(t)
    boutton1 = pygame.Rect(t* 2 * 149, y * 97, s * 100, s * 100)
    pygame.draw.rect(gameDisplay, white, boutton1)

    for x in range(0,4):

        gameDisplay.blit(E[x],(x*2*150,y*100))
    pygame.display.update()

def redgreen():
    gameDisplay.fill((255,0,0))
    green = pygame.Rect(0,0,600,600)
    pygame.draw.rect(gameDisplay,(0,255,0),green)
    carImg = pygame.transform.scale(carImgs, (300, 300))
    carImg1 = pygame.transform.rotate(carImg, random.randrange(0, 360, 90))
    carImg2 = pygame.transform.rotate(carImg, random.randrange(0, 360, 90))
    # carImg1= pygame.transform.flip(carImg,1,0)
    gameDisplay.blit(carImg1, (200, 150))
    gameDisplay.blit(carImg2, (750, 150))

    pygame.display.update()




def lineE(y):
    print(y)
    s=4
    s=s-y
    E=[]
    list=[]
    gameDisplay.fill(white)
    while len(list)!=4:
        r = random.randrange(0, 360, 90)
        if r not in list:
            list.append(r)
            Eimag = pygame.transform.scale(carImgs,(s*90, s*90))
            Eimag_c=Eimag.get_rect().center
            Eimag = pygame.transform.rotate(Eimag, r)
            print(Eimag_c)




            E.append(Eimag)

    for x in range(0,4):
        gameDisplay.blit(E[x],(x*2*150,y*100))
    pygame.display.update()

def E():

    gameDisplay.fill(white)

    carImg = pygame.transform.scale(carImgs, (300, 300))

    cen=carImg.get_rect().center
    carImg1= pygame.transform.rotate(carImg,random.randrange(0, 360, 90))
    # carImg1=ncarImg1.get_rect(center=cen)

    # carImg1= pygame.transform.flip(carImg,1,0)

    gameDisplay.blit(carImg1, (100, 30))
    x = (0)
    y = (0)
    pygame.display.update()
def E2():
    gameDisplay.fill(white)
    carImg = pygame.transform.scale(carImgs, (300, 300))
    carImg1= pygame.transform.rotate(carImg,random.randrange(0, 360, 90))
    carImg2= pygame.transform.rotate(carImg,random.randrange(0, 360, 90))
    # carImg1= pygame.transform.flip(carImg,1,0)
    gameDisplay.blit(carImg1, (100, 150))
    gameDisplay.blit(carImg2, (400, 150))
    x = (0)
    y = (0)
    pygame.display.update()

if __name__ == '__main__':
    main_menu()
    gameDisplay.fill(white)
    while not crashed:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    E()
                    pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()