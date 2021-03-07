import pygame
import random as rnd

# класс маленького корабля

img1 = pygame.image.load('images\\21.png')
img1.set_colorkey((0, 0, 0))


img2 = pygame.image.load('images\\22.png')
img2.set_colorkey((0, 0, 0))

img3= pygame.image.load('images\\23.png')
img3.set_colorkey((0, 0, 0))


img4 = pygame.image.load('images\\555.png')
img4.set_colorkey((0, 0, 0))

class Ships:
    def __init__(self,x,y,surf):
        self.x=x
        self.y=y
        self.surf = surf
        self.image= rnd.choice([img1,img2,img3])
        self.paddle = self.image.get_rect(center=(self.x,self.y))
        self.img4 = img4
    def draw(self,surf):
        self.surf.blit(self.image,self.paddle)

    def boom(self,surf):
        self.surf.blit(self.img4,self.paddle)
