

import pygame

from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    """Start the main loop for the game."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Ship creation.
    ship = Ship(screen)
    # Назначение цвета фона.
    bg_color = (0, 255, 230)
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
