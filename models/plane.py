import random
import pygame
from enum import Enum
from models.bullet import HeroBullet, EnemyBullet
from config.configs import get_enemy_info, get_hero_info


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


class Plane:
    def __init__(self, screen, plane_info):
        # default position
        self._x = plane_info.init_x
        self._y = plane_info.init_y

        self._direction = Direction.RIGHT
        self._screen = screen
        self._image = pygame.image.load(plane_info.plane_image_path)
        self._bullet_image = plane_info.bullet_image_path
        self._bullets_list = []
        self._steps = plane_info.steps
        self._left_border = plane_info.left_border
        self._right_border = plane_info.right_border

    def move(self):
        raise Exception("Should initialized in inherited class")

    def fire(self):
        raise Exception("Should initialized in inherited class")

    def display(self):
        self._screen.blit(self._image, (self._x, self._y))
        for bullet in self._bullets_list:
            bullet.display()
            bullet.move()

    def update_status(self, *args):
        pass


class EnemyPlane(Plane):
    def __init__(self, screen):
        super().__init__(screen, get_enemy_info())
        self._hit_bullet_lists = []

    def fire(self):
        if random.randint(2, 4) == 3:
            bullet = EnemyBullet(self._x, self._y, self._screen, self._bullet_image)
            self._bullets_list.append(bullet)

    def move(self):
        if self._x > self._right_border:
            self._direction = Direction.LEFT
        elif self._x < self._left_border:
            self._direction = Direction.RIGHT
        self._x = self._x + (-self._steps if self._direction == Direction.LEFT else self._steps)

    def update_status(self, **kwargs):
        # 判断一下子弹是否越界，然后把越界的子弹保存在一个列表里面
        del_bullet_list = set()
        for item in self._bullets_list:
            if item.is_out_of_boundary():
                del_bullet_list.add(item)  # 把越界的子弹放入一个列表中
                pass

        # 判断子弹是否被击中
        hero_bullets_list = []
        if 'bullets_list' in kwargs.keys():
            hero_bullets_list = kwargs['bullets_list']
        self._hit_bullet_lists = []
        for item in self._bullets_list:
            for bullet in hero_bullets_list:
                if item.is_hit_by_bullet(bullet):
                    self._hit_bullet_lists.append(bullet)
                    del_bullet_list.add(item)

        for del_item in del_bullet_list:
            self._bullets_list.remove(del_item)
        pass

    def get_hit_bullets_list(self) -> list:
        return self._hit_bullet_lists


class HeroPlane(Plane):
    def __init__(self, screen):
        super().__init__(screen, get_hero_info())

    def fire(self):
        bullet = HeroBullet(self._x, self._y, self._screen, self._bullet_image)
        self._bullets_list.append(bullet)

    def move_left(self):
        self._x -= self._steps if self._x > self._left_border else 0

    def move_right(self):
        self._x += self._steps if self._x < self._right_border else 0

    def update_status(self, **kwargs):
        delete_bullet_list = set()
        for bullet in self._bullets_list:
            # check whether bullet is out of boundary
            if bullet.is_out_of_boundary():
                delete_bullet_list.add(bullet)

        hit_bullets_list = []
        if 'bullets_list' in kwargs.keys():
            hit_bullets_list = kwargs['bullets_list']
        for bullet in hit_bullets_list:
            delete_bullet_list.add(bullet)

        # remove bullets that is out of boundary
        for bullet in delete_bullet_list:
            self._bullets_list.remove(bullet)

    def get_bullet_ranges(self) -> list:
        return self._bullets_list


if __name__ == "__main__":
    pass