import pygame

#класс движущегося силового поля

img = pygame.image.load('images\\251.png')
img.set_colorkey((0, 0, 0))
img1 = pygame.image.load('images\\2511.png')
img1.set_colorkey((0, 0, 0))

class Sp_1:
    def __init__(self,x,y,surf,speed):
        self.x=x
        self.y=y
        self.surf = surf
        self.speed = speed
        self.image = img
        self.image1 = img1
        self.paddle = self.image.get_rect(topleft=(self.x,self.y))
        self.dx=1

    def draw(self,surf):
        self.surf.blit(self.image,self.paddle)
    def green(self,surf):
         self.surf.blit(self.image1,self.paddle)       

    def move(self):
        from ekran import W
        if  self.paddle.right < W and self.paddle.x >0:
            self.paddle.x += self.speed * self.dx 
        else:
            self.dx = -self.dx
            self.paddle.x += self.speed * self.dx


