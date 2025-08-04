
import pygame
from typing import TYPE_CHECKING
from arsenal import Arsenal # Corrected import

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'): 
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()


        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(self.image, 90)  # rotate to face right
        self.image = pygame.transform.scale(self.image, (self.settings.ship_h, self.settings.ship_w))  # flip width/height

        self.rect = self.image.get_rect()
        self.rect.midright = self.boundaries.midright
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def update(self)-> None:
        self._update_ship_movement() 
        self.arsenal.update_arsenal()
    
    def _update_ship_movement(self)-> None:
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def draw(self) -> None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self)-> bool:
        return self.arsenal.fire_bullet()

    def center_ship(self):
        self.rect.midright = self.boundaries.midright
        self.y = float(self.rect.y)



