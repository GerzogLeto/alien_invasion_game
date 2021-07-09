import sys
import pygame


def check_events():
    # Process button and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # Update display
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Show last display
    pygame.display.flip()