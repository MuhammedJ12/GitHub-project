import sys

import pygame

from bullet import Bullet
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
def check_events(ship):
 """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        check_keydown_events(event, ship)
    elif event.type == pygame.KEYUP:
        check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    
def check_events(ship):

    elif event.type ==pygame.KEYDOWN:
        if event.type ==pygame.event.get():
        #moves ship to the right
        ship.rect.centerx += 1
def check_keydown_events(event, ship):
    """Respond to keypresses."""
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
def check_keyup_events(event, ship):
    """Respond to key releases."""
    elif event.type == pygame.KEYDOWN
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
