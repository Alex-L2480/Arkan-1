import pygame

  

W = 1500 # ширина игрового окна
H = 1000# высота игрового окна
fps = 60

pygame.init()#создаю окно игры
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

img1 = pygame.image.load('images/m1.png')
img2 = pygame.image.load('images/m2.png')
img11 = pygame.image.load('images/m3.png')
img22 = pygame.image.load('images/m4.png')

class Button:
    def __init__ (self, x, y, surf, image, image2):
        self.x = x
        self.y = y
        self.surf = surf
        self.image = image
        self.image2 = image2
        self.paddle = self.image.get_rect(topleft = (self.x,self.y))
        

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.paddle.left < mouse[0] < self.paddle.right and self.paddle.bottom > mouse[1] > self.paddle.top:
            self.surf.blit(self.image2,(self.paddle.x,self.paddle.y))
            if click[0] == 1 and self.paddle.top == 200:
                from main import run_game
                run_game()    
            if click[0] == 1 and self.paddle.top == 450:
                quit()                                     
        else:
            self.surf.blit(self.image,(self.paddle.x,self.paddle.y))
            
button1 = Button(445,200,sc,img1,img2,)
button2 = Button(445,450,sc,img11,img22)

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() #цикл игры до нажатия на крестик идет

        sc.fill('blue')
        button1.draw()
        button2.draw()

        
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps) 

menu()
