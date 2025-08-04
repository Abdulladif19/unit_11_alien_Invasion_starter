
import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats


class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.clock = pygame.time.Clock()
        self.running = True

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.stats = GameStats(self)
        self.game_active = True

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

    def run_game(self) -> None:
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        self.ship.arsenal.update_arsenal()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal, self.alien_fleet.fleet, True, True)

        if not self.alien_fleet.fleet:
            self.ship.arsenal.arsenal.empty()
            self.alien_fleet.create_fleet()

    def _update_aliens(self):
        self.alien_fleet.update_fleet()

        if pygame.sprite.spritecollideany(self.ship, self.alien_fleet.fleet):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        for alien in self.alien_fleet.fleet.sprites():
            if alien.rect.bottom >= self.settings.screen_h:
                self._ship_hit()
                break

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.ship.arsenal.arsenal.empty()
            self.alien_fleet.fleet.empty()
            self.alien_fleet.create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
