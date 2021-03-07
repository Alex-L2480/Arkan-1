import pygame

#Класс  Мяча - меняющийся мяч 2 вида списком, по времени меняется

img = pygame.image.load('images\\46.png')
img.set_colorkey((0, 0, 0))
img2 = pygame.image.load('images\\47.png')
img2.set_colorkey((0, 0, 0))

R=[img,img2]

class Shar:
    def __init__(self,x,y,surf,speed):
        self.x=x
        self.y=y
        self.surf = surf
        self.speed = speed
        self.image = img
        self.paddle = self.image.get_rect(center=(self.x,self.y))
        self.dx=1
        self.dy=-1
        self.animcount = 0
    def draw(self,surf):
        self.surf.blit(self.image,self.paddle)
    def move(self):
        from ekran import W
        self.paddle.x += self.speed * self.dx
        self.animcount+=1
        if self.animcount +1 >120:
            self.animcount = 0
        self.surf.blit(R[self.animcount//60],(self.paddle.x,self.paddle.y))

        self.paddle.y += self.speed * self.dy 
        
        if self.paddle.left < 1 or self.paddle.right > W - 1: 
            self.dx = -self.dx
        if self.paddle.top <1:
            self.dy = -self.dy