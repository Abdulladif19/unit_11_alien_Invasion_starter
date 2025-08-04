
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_shift_speed = self.settings.fleet_shift_speed

        self.create_fleet()

    def create_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size_vertical(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets_vertical_fleet(alien_w, alien_h, screen_w, fleet_w, fleet_h)
        
        self._create_vertical_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_vertical_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for col in range(fleet_w):
            for row in range(fleet_h):
                if col % 2 == 0 or row % 2 == 0:
                   continue
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                self._create_alien(current_x, current_y)

    def calculate_offsets_vertical_fleet(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        half_screen_h = self.settings.screen_h // 2
        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_w
        
        x_offset = int((screen_w/4) - (fleet_horizontal_space/2))
        y_offset = int((half_screen_h) - (fleet_vertical_space/2))

        return x_offset, y_offset

    def calculate_fleet_size_vertical(self, alien_w, screen_w, alien_h, screen_h):
        fleet_h = (screen_h // alien_h)
        fleet_w = ((screen_w / 2) // alien_w)

        if fleet_w % 2 == 0:
            fleet_w -= 1 
        else:
            fleet_w -= 2

        if fleet_h  % 2 == 0:
            fleet_h -= 1 
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self) -> None:
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._shift_alien_fleet_horizontally()
                self.fleet_direction *= -1
                break

    def _shift_alien_fleet_horizontally(self) -> None:
        for alien in self.fleet:
            alien.x += self.fleet_shift_speed

    def update_fleet(self) -> None:
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

