import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion', y_pos: float):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.rotate(self.image, 90)  # rotate to match horizontal direction
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_h, self.settings.bullet_w))

        self.rect = self.image.get_rect()
        self.rect.centery = y_pos
        self.rect.left = game.ship.rect.right  # start at the front of the ship

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
