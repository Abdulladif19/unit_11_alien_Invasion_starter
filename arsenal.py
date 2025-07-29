import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.settings.screen_w:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self, y_pos: float) -> bool:
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game, y_pos)
            self.arsenal.add(new_bullet)
            return True
        return False
