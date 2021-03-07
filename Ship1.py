import pygame
from random import randint

img = pygame.image.load('images\\1x.png')
img.set_colorkey((0, 0, 0))

img1 = pygame.image.load('images\\555.png')
img1.set_colorkey((0, 0, 0))

rocketimg = pygame.image.load('images\\222.png')
rocketimg.set_colorkey((255,255,255))

#класс главного корабля противника 
class Ship:
    def __init__(self,x,y,surf):
        self.x = x
        self.y = y
        self.surf = surf
        self.image = img
        self.paddle = self.image.get_rect(center=(self.x,self.y))
        self.image1 = img1
        self.rocketimg = rocketimg
        self.rocketpaddle = self.rocketimg.get_rect(center=(self.x,self.y+90))
        self.rocketspeed = 5
        self.v = 0
        self.count = 0

    def draw(self,surf):
        self.surf.blit(self.image,self.paddle)
    def boom(self,surf):
        self.surf.blit(self.image1,self.paddle)
    def rocket(self,surf):
        self.count +=1
        self.surf.blit(self.rocketimg,self.rocketpaddle)
        self.rocketpaddle.y += self.rocketspeed
        self.rocketpaddle.x += self.v
              
        from ekran import H
        if self.rocketpaddle.y > H and self.count>360:
            self.rocketpaddle.center = self.x,self.y+90
            self.v = randint(-5,5)
            self.count = 0
            

