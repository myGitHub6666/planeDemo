import pygame
from config.configs import get_bullet_info


class Bullet:
    def __init__(self, x, y, screen, image_path):
        self._bullet_info = get_bullet_info()
        self._move_steps = self._bullet_info.move_steps
        self.x = x + self._move_steps
        self.y = y + self._move_steps
        self._border_top = self._bullet_info.border_top
        self._border_bottom = self._bullet_info.border_bottom
        self.screen = screen
        self.image = pygame.image.load(image_path)

    def is_out_of_boundary(self):
        # out of boundary
        return True if self.y > self._border_top or self.y < self._border_bottom else False

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        raise Exception("Please overload this method in inherited class.")


class EnemyBullet(Bullet):
    def __init__(self, x, y, screen, image_path):
        super().__init__(x, y, screen, image_path)
        self._attack_range = self._bullet_info.attack_range

    def is_hit_by_bullet(self, bullet):
        x, y = bullet.x, bullet.y
        return (x + self._attack_range) >= self.x >= (x - self._attack_range) and \
               (y + self._attack_range) >= self.y >= (y - self._attack_range)

    def move(self):
        self.y += self._move_steps


class HeroBullet(Bullet):
    def __init__(self, x, y, screen, image_path):
        super().__init__(x, y, screen, image_path)

    def move(self):
        self.y -= self._move_steps


if __name__ == "__main__":
    pass