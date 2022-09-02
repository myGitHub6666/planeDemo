import random

import pygame
from pygame.locals import *


# 创建敌机的子弹类
class EnemyBullet(object):
    # 敌军子弹初始化
    def __init__(self, x, y, screen):
        self.x = x + 5
        self.y = y + 5
        self.screen = screen
        self.image = pygame.image.load('./feiji/bullet1.png')
        pass

    # 敌军子弹显示
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    # 敌军子弹移动
    def move(self):
        self.y += 5
        pass

    # 判断敌军子弹是否越界
    def judge(self):
        # 判断子弹是否越界
        if self.y > 965:
            return True
        else:
            return False
        pass


# 创建敌机类
class EnemyPlane(object):
    # 初始化敌军飞机
    def __init__(self, screen):
        '''
        初始化敌人的飞机，和我方飞机的类类似
        '''
        # 默认敌军可以向有右边移动
        self.direction = 'right'
        # 飞机的默认位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片
        self.imageName = './feiji/enemy0.png'
        self.image = pygame.image.load(self.imageName)
        # 用来存放敌人飞机子弹的列表
        self.enemyBulletList = []
        pass

    # 敌军发射子弹
    def sheBullet(self):
        # 创建一个新的敌机子弹对象
        num = random.randint(1, 80)
        if num == 3:
            newEnemyBullet = EnemyBullet(self.x, self.y, self.screen)
            # 把子弹对象添加到飞机类的enemyBulleList列表里面。
            self.enemyBulletList.append(newEnemyBullet)

    # 敌军的飞机可以左右自动
    def move(self):
        # 敌机可以左右移动,并且随机移动
        if self.x > 730:
            self.direction = 'left'
        elif self.x<0:
            self.direction = 'right'

        if self.direction == 'right':
            self.x +=2
        elif self.direction =="left":
            self.x -=2

    # 敌军子弹和飞机的显示
    def display(self):
        '''
        子弹显示和判断是否越界
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))
        # 判断一下子弹是否越界，然后把越界的子弹保存在一个列表里面
        delBulletList = []
        for item in self.enemyBulletList:
            if item.judge():
                delBulletList.append(item)  # 把越界的子弹放入一个列表中
                pass
        # 在敌机子弹的列表中删除越界的子弹
        for delItem in delBulletList:
            self.enemyBulletList.remove(delItem)
        # 遍历剩余的子弹，并显示
        for bullet in self.enemyBulletList:
            bullet.display()  # 循环显示子弹的位置，
            bullet.move()  # 循环显示子弹移动
        pass


# 创建飞机类
class HeroPlane(object):
    def __init__(self, screen):
        '''
        初始化函数，主窗体对象
        :return:
        '''
        # 飞机的默认位置
        self.x = 0
        self.y = 965
        self.screen = screen
        # 设置要显示内容的窗口
        # 生成飞机的图片对象
        self.imageName = './feiji/hero.png'
        self.image = pygame.image.load(self.imageName)
        # 用来存放子弹的列表
        self.bulletlist = []
        pass

    def sheBullet(self):
        # 创建一个新的子弹对象
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletlist.append(newBullet)

    def moveleft(self):
        '''
        飞机左移动
        :return:
        '''
        if self.x > 0:
            self.x -= 10
        pass

    def moveright(self):
        '''
        飞机右移动
        :return:
        '''
        if self.x < 730:
            self.x += 10
        pass

    def display(self):
        '''
        飞机在主屏幕的显示
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))
        needDelItermList = []
        for item in self.bulletlist:
            # 判断子弹是否越界
            if item.judge():
                needDelItermList.append(item)
                pass
        #
        for i in needDelItermList:
            # 删除越界的子弹
            self.bulletlist.remove(i)
            pass
        for bullet in self.bulletlist:
            # 遍历剩余的子弹并显示
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动，下次再看到子弹的时候就会看到子弹再修改后的位置

        pass


# 创建子弹类
class Bullet(object):
    def __init__(self, x, y, screen):
        '''

        :param screen:
        '''
        self.x = x + 15
        self.y = y - 5
        self.screen = screen
        self.imgage = pygame.image.load('./feiji/bullet.png')

        pass

    def display(self):
        self.screen.blit(self.imgage, (self.x, self.y))
        pass

    def move(self):
        self.y -= 5
        pass

    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y < 0:
            return True
        else:
            return False
        pass


# HeroObj是函数的普通参数，不是继承的类，HeroObj应该是一个实例化对象。
def key_control(HeroObj):
    '''
    检测键盘的操作
    :param HeroObj:该参数是一个飞机的实例化对象
    :return:
    '''
    # 获取键盘事件
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == QUIT:
            print("退出")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                HeroObj.moveleft()
                print('left')
            elif event.key == K_d or event.key == K_RIGHT:
                HeroObj.moveright()
                print("right")
            elif event.key == K_SPACE:
                HeroObj.sheBullet()
                print('按下空格键，发射子弹')


def main():
    # 首先创建有一个窗口，来显示内容
    screen = pygame.display.set_mode((796, 1024), depth=32)
    # 设定一个背景图片
    background = pygame.image.load('./feiji/background.png')
    # 设置一个title
    pygame.display.set_caption('飞机大战小游戏')
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # -1表示无限循环
    # 创建敌人飞机实例
    enemyplane = EnemyPlane(screen)
    hero = HeroPlane(screen)
    # 载入玩家飞机图片
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机图片
        hero.display()
        # 显示敌人飞机,调用显示敌机的方法
        enemyplane.display()
        # 敌机移动
        enemyplane.sheBullet()
        # 敌机发射子弹
        enemyplane.move()
        # 读取键盘数据
        key_control(hero)
        # 判断子弹打中飞机后，输出赢一局
        # 更新显示内容
        pygame.display.update()


if __name__ == "__main__":
    main()
