import pygame


#Класс  Главного Героя  Динамический герой +jump

wr= [pygame.image.load('images\\pygame_right_1.png'), pygame.image.load('images\\pygame_right_2.png'), 
pygame.image.load('images\\pygame_right_3.png'), pygame.image.load('images\\pygame_right_4.png'),
pygame.image.load('images\\pygame_right_5.png'), pygame.image.load('images\\pygame_right_6.png')]

wl = [pygame.image.load('images\\pygame_left_1.png'), pygame.image.load('images\\pygame_left_2.png'),
pygame.image.load('images\\pygame_left_3.png'), pygame.image.load('images\\pygame_left_4.png'),
pygame.image.load('images\\pygame_left_5.png'), pygame.image.load('images\\pygame_left_6.png')]


img = pygame.image.load('images\\pygame_idle.png')
img.set_colorkey((0, 0, 0))

class Player:
    def __init__(self,x,y,surf,speed):
        self.x=x
        self.y=y
        self.surf = surf
        self.speed = speed
        self.image=img
        self.paddle = self.image.get_rect(center=(self.x,self.y))
        self.animcount = 0
        self.jump = False
        self.jumpcount = 10
    
    def move(self):
        from ekran import W
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.left>0:
            self.paddle.left-=self.speed
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and self.paddle.right<W: 
            self.paddle.right+=self.speed 
            right = True
            left = False     
        else:
            right = False
            left = False
            self.animcount = 0
            self.surf.blit(self.image,self.paddle)
        if self.animcount+1>30:
            self.animcount = 0
        if left:
            self.surf.blit(wl[self.animcount//5],(self.paddle.x,self.paddle.y))
            self.animcount+=1
        if right:
            self.surf.blit(wr[self.animcount//5],(self.paddle.x,self.paddle.y))
            self.animcount+=1

        if keys[pygame.K_SPACE]:
            self.jump=True
        
        if self.jump is True:
            if self.jumpcount >= -10:
                if self.jumpcount<0:
                    self.paddle.y+=(self.jumpcount**2)/2
                else:
                    self.paddle.y-=(self.jumpcount**2)/2
                self.jumpcount-=1
            
            else:
                self.jump=False
                self.jumpcount=10
                self.paddle.y = 880
     





