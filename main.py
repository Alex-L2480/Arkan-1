import pygame
from random import randrange as rnd
from pygame.locals import *
from Shar4 import Shar
from Player3 import Player
from ekran import W,H
from Ship1 import Ship
from collision import collision
from Ships2 import Ships
from Silovoe_pole1 import Sp_1
from buttons import menu
import os
print(os.getcwd())

fps = 60
pygame.init()
sc = pygame.display.set_mode((W,H)) #создаю окно игры
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

a= Shar(670,800,sc,4)# объект щар

b = Player(700,915,sc,12)# объект игрок

c = Ship(700,70,sc) # главный корабль

t=0 # отсчет повреждений главного корабля

e = Sp_1(400,450,sc,6) #силовое поле

bg = pygame.image.load('images\\ee.jpg') #фон

u=0 # переменные для регулировки расстояний между малыми кораблями
g=0
block_list=[]
for i in range(3):
    for n in range(5):
        d = Ships(120+u, H//5+g,sc) # список мелких кораблей и их координаты
        block_list.append(d)
        u=u+300      
    u=0
    g=g+100

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE : #цикл игры до нажатия на крестик идет или нажатия ESC
                menu()          
        sc.blit(bg,(0, 0))# фон
        a.move() #создание шара 
        b.move() # создание игрока
        e.draw(sc)# создание силового поля
        e.move()

        for h in range(len(block_list)): # рисую мелкие корабли
            block_list[h].draw(sc)      
        if a.paddle.colliderect(b.paddle) and a.dy >= 0: # взаимодействие шара и игрока
            a.dy=-a.dy  

        if a.paddle.colliderect(e.paddle) and a.dy <= 0: # отскоки от силового поля
            a.dy=-a.dy 
        if a.paddle.colliderect(e.paddle) and a.dy >= 0: # отображение силового поля зеленым цветом при попадании шара сверху - проход насквозь
            e.green(sc)               
        global t       
        if t<4: # 4 - предел повреждений главного корабля
            c.draw(sc) # создание главного корабля
            c.rocket(sc) #создание ракеты
            if a.paddle.colliderect(c.paddle):
                clock.tick(fps) 
                a.dx, a.dy = collision(a.dx,a.dy,a.paddle,c.paddle)
                t+=1
                c.boom(sc)# эффект взрыва
                clock.tick(fps)     
        if c.rocketpaddle.colliderect(b.paddle): #выход после попадания ракеты
            quit()

        for f in range(-1,len(block_list)-1):
            if a.paddle.colliderect(block_list[f].paddle):
                pygame.display.update()# обновление экрана
                a.dx, a.dy = collision(a.dx,a.dy,a.paddle,block_list[f].paddle) #отскоки от маленьких кораблей и удаление их после попаданий мяча
                clock.tick(fps)
                block_list[f].boom(sc)# эффект взрыва  
                block_list.pop(f) # удаление подбитого корабля с экрана
                a.speed+=0.5                      
        if a.paddle.y>H: # выход из системы после упущения мяча
            quit()               
        pygame.display.update()
        pygame.display.flip()   # покадровое обновление экрана
        clock.tick(fps)            
run_game()
   