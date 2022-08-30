import pygame
from pygame.locals import *


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

    # 载入晚间飞机图片
    hero = pygame.image.load('./feiji/hero.png')
    # 初始化玩家位置
    x,y = 0,965


    # 设定要显示的内容
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机图片
        screen.blit(hero,(x,y))
        # 获取键盘事件
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == QUIT:
                print("退出")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    if x >0:
                        x -= 5
                    print("left")
                elif event.key == K_d or event.key == K_RIGHT:
                    if x<670:
                        x += 5
                    print("right")
                elif event.key == K_SPACE:
                    print('K_space')
        # 更新显示的内容
        pygame.display.update()


if __name__ == "__main__":
    main()
