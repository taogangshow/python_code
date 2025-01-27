import pygame
import time
from pygame.locals import *
import random
class Base(object):
    def __init__(self,screen,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_name)

class BasePlane(Base):
    def __init__(self,screen,x,y,image_name):
        Base.__init__(self,screen,x,y,image_name)
        self.bullet_list = []#用来储存发射出去的子弹对象引用
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)


class HeroPlane(BasePlane):
    """飞机的类"""
    def __init__(self,screen):
        BasePlane.__init__(self,screen,210,700,"./feiji/hero1.png")

    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
class EnemyPlane(BasePlane):
    """敌机的类"""
    def __init__(self,screen):
        BasePlane.__init__(self,screen,0,0,"./feiji/enemy0.png")
        self.direction = "right"#用来存储敌机默认的方向
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)
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
        random_num = random.randint(1,100)
        if random_num==20 or random_num==30:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
class Bullet(BaseBullet):
    """飞机的子弹类"""
    def __init__(self,screen,x,y):
        BasePlane.__init__(self,screen,x+40,y-20,"./feiji/bullet.png")
    def move(self):
        self.y-=10
    def judge(self):
        if self.y<0:# if self.y<200测试当子弹在200的位置时候是否消失
            return True
        else:
            return False
class EnemyBullet(BasePlane):
    """敌机的子弹类"""
    def __init__(self,screen,x,y):
        BasePlane.__init__(self,screen,x+25,y+40,"./feiji/bullet1.png")
    def move(self):
        self.y+=5
    def judge(self):
        if self.y>852:# if self.y>400测试当子弹在200的位置时候是否消失
            return True
        else:
            return False
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
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
