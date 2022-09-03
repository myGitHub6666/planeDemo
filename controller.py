import sys
import pygame
from pygame.locals import *
from models.plane import EnemyPlane, HeroPlane
from config.configs import get_game_info


class Controller:
    def __init__(self):
        self._screen = None
        self._enemy_plane = None
        self._hero_plane = None
        self._background = None
        self._init_status()

    def _init_status(self):
        game_info = get_game_info()
        # create a windows to display all content.
        self._screen = pygame.display.set_mode((game_info.width, game_info.height),
                                               depth=game_info.depth)
        self._background = pygame.image.load(game_info.background)
        pygame.display.set_caption(game_info.title)

        # add background music
        pygame.mixer.init()
        pygame.mixer.music.load(game_info.music)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)  # -1表示无限循环

        # create plane objects.
        self._enemy_plane = EnemyPlane(self._screen)
        self._hero_plane = HeroPlane(self._screen)

    def run(self):
        while True:
            self._screen.blit(self._background, (0, 0))

            hero_bullet_ranges = self._hero_plane.get_bullet_ranges()
            self._enemy_plane.update_status(bullets_list=hero_bullet_ranges)

            hit_bullets_list = self._enemy_plane.get_hit_bullets_list()
            self._hero_plane.update_status(bullets_list=hit_bullets_list)

            self._enemy_plane.fire()
            self._enemy_plane.move()

            self._capture_keyboard_event()

            self._hero_plane.display()
            self._enemy_plane.display()

            pygame.display.update()

    def _capture_keyboard_event(self):
        pressed_keys_list = pygame.key.get_pressed()
        if pressed_keys_list[K_a] or pressed_keys_list[K_LEFT]:
            print('move left')
            self._hero_plane.move_left()
        if pressed_keys_list[K_d] or pressed_keys_list[K_RIGHT]:
            print("move right")
            self._hero_plane.move_right()

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == QUIT:
                print('exit')
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    print('press spacer and fire')
                    self._hero_plane.fire()


if __name__ == "__main__":
    ctrl_hdl = Controller()
    ctrl_hdl.run()
