import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(self.image, 270)  # rotate to face right
        self.image = pygame.transform.scale(self.image, (self.settings.ship_h, self.settings.ship_w))  # flip width/height

        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft  # stick to the left side
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

        self.arsenal = arsenal

    def update(self):
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y
        self.arsenal.update_arsenal()

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        return self.arsenal.fire_bullet(self.rect.centery)


