
from pathlib import Path

class Settings:

    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w = 1000
        self.screen_h = 400
        self.fps = 60
        self.bg_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60