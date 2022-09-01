import pygame
from pygame.locals import *
# 创建飞机类
'''
1 : 
'''
class HeroPlane(object):
    def __init(self,screen):
        '''
        初始化函数，主窗体对象
        :return:
        '''
        # 飞机的默认位置
        self.x = 150
        self.y = 450
        self.screen = screen
        # 设置要显示内容的窗口
        # 生成飞机的图片对象
        self.imageName = './feiji/hero.png'
        self.image = pygame.image.load(self.imageName)
        pass
    def moveleft(self):
        '''
        飞机左移动
        :return:
        '''
        if self.x >0:
            self.x -=10
        pass
    def moveright(self):
        '''
        飞机右移动
        :return:
        '''
        if self.x < 600:
            self.x += 10
        pass
    def display(self):
        '''
        飞机在主屏幕的显示
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
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
                print('按下空格键')




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
    pygame.mixer.music.play(-1) # -1表示无限循环
    hero = HeroPlane(screen)
    # 载入玩家飞机图片
    while True:
        screen.blit(background,(0,0))
        # 显示玩家飞机图片
        hero.display()
        # 读取键盘数据
        key_control(hero)
        # 更新显示内容
        pygame.display.update()

if __name__ == "__main__":
   main()