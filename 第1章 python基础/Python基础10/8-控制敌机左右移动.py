import pygame
import time
from pygame.locals import *
class HeroPlane(object):
    def __init__(self,screen):
        self.x = 210
        self.y = 700
        self.screen = screen
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []#用来储存发射出去的子弹对象引用
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
class EnemyPlane(object):
    """敌机的类"""
    def __init__(self,screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image = pygame.image.load("./feiji/enemy0.png")
        #self.bullet_list = []#用来储存发射出去的子弹对象引用
        self.direction = "right"
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        #for bullet in self.bullet_list:
        #    bullet.display()
        #    bullet.move()
    def move(self):
        if self.direction == "right":
            self.x+=5
        elif self.direction == "left":
            self.x-=5
        if self.x>480-50:
            self.direction= "left"
        elif self.x<0:
            self.direction = "right"
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
class Bullet(object):
    def __init__(self,screen,x,y):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=10
def key_control(hero):
     #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero.move_left()

            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.move_right()

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero.fire()

def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #2.创建一个和窗口一样大小的图片,用来充当背景
    background = pygame.image.load("./feiji/background.png")
    #3.创建一个飞机对象
    hero = HeroPlane(screen)
    #4.创建一个敌机对象
    enemy = EnemyPlane(screen)
    """把背景图片放到窗口中显示"""
    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
