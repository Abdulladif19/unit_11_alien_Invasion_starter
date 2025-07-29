"""
Lab11_Abdulladif1.py
Author: Abdulladif
Purpose: Reposition spaceship on left or right edge of the screen. Ship moves up/down, fires horizontally toward center.
Date: 07/18/2025
"""

import pygame
import sys
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.clock = pygame.time.Clock()
        self.running = True

        self.ship = Ship(self, Arsenal(self))

    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self.ship.fire()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
