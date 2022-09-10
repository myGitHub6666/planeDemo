#!/usr/bin/env python3
# coding: utf-8

import os
from configparser import ConfigParser
from pprint import pprint


class PlaneInfo:
    def __init__(self):
        self.plane_image_path = None
        self.bullet_image_path = None
        self.steps = 0
        self.init_x = 0
        self.init_y = 0
        self.left_border = 0
        self.right_border = 0


class BulletInfo:
    def __init__(self):
        self.attack_range = 0
        self.move_steps = 0
        self.border_top = 0
        self.border_bottom = 0


class GameInfo:
    def __init__(self):
        self.title = None
        self.background = None
        self.music = None
        self.width = 0
        self.height = 0
        self.depth = 0


class ConfigHdl:
    config_hdl = None

    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'configurations.ini')
        self._config = ConfigParser()
        self._config.read(config_path)
        self._game_info = self._init_game()
        self._hero_plane = self._init_hero_plane()
        self._enemy_plane = self._init_enemy_plant()
        self._bullet_info = self._init_bullet()

    @property
    def enemy_info(self):
        return self._enemy_plane

    @property
    def hero_info(self):
        return self._hero_plane

    @property
    def game_info(self):
        return self._game_info

    @property
    def bullet_info(self):
        return self._bullet_info

    def _init_game(self):
        game_info = GameInfo()
        game_info.title = self._config.get('game_info', 'title')
        game_info.background = self._config.get('game_info', 'background')
        game_info.music = self._config.get('game_info', 'music')
        game_info.width = self._config.getint('game_info', 'width')
        game_info.height = self._config.getint('game_info', 'height')
        game_info.depth = self._config.getint('game_info', 'depth')
        return game_info

    def _init_plane(self, plane_type: str = None):
        plane_info = PlaneInfo()
        plane_info.plane_image_path = self._config.get(plane_type, 'plane_image_path')
        plane_info.bullet_image_path = self._config.get(plane_type, 'bullet_image_path')
        plane_info.steps = self._config.getint(plane_type, 'steps', fallback=0)
        plane_info.init_x = self._config.getint(plane_type, 'init_x')
        plane_info.init_y = self._config.getint(plane_type, 'init_y')
        plane_info.left_border = self._config.getint(plane_type, 'left_border')
        plane_info.right_border = self._config.getint(plane_type, 'right_border')
        return plane_info

    def _init_hero_plane(self):
        return self._init_plane('hero')

    def _init_enemy_plant(self):
        return self._init_plane('enemy')

    def _init_bullet(self):
        bullet_info = BulletInfo()
        bullet_info.attack_range = self._config.getint('bullet', 'attack_range')
        bullet_info.move_steps = self._config.getint('bullet', 'move_steps')
        bullet_info.border_top = self._config.getint('bullet', 'border_top')
        bullet_info.border_bottom = self._config.getint('bullet', 'border_bottom')
        return bullet_info


ConfigHdl.config_hdl = ConfigHdl()


def get_config_info():
    return ConfigHdl.config_hdl


def get_enemy_info():
    return ConfigHdl.config_hdl.enemy_info


def get_hero_info():
    return ConfigHdl.config_hdl.hero_info


def get_game_info():
    return ConfigHdl.config_hdl.game_info


def get_bullet_info():
    return ConfigHdl.config_hdl.bullet_info


if __name__ == "__main__":
    config_info = get_config_info()
    enemy_info = get_enemy_info()
    pass
