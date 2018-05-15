#I plan to create a modified version of pacman for my project. I was looking at templates but I have not chosen one to modify. 
#Project Proposal
#SPACE INVADERS
#Find a template that we can edit the:
#create weapon calss, colors, controlls
#We need to learn how to create different levels for enemies or a multiplayer online session
#We know how to do a lot of the simple things like style of the game with classes, move two battle ships at once

#break progress
#we found a template: https://github.com/leerob/Space_Invaders
#we need to find out what methods we want to use that we previously know and incorporate the template we found into our own version.
# we are gonna use what we found from python crasdh course

# Space Invaders
# We took code from Mr.Lee. His link is above in line 10.
# We are now taking blocks of code that we want to replace with our own. 


#OUR PROJECT

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

import game_functions as gf

def run_game():
    # Init pygame, settings and create screen object
    pygame.init();

    # loading settings variables from imported class
    ai_settings = Settings()

    # the screen object is called a surface which displays a game element
    # this surface will be redrawn every pass through the loop for animation
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Nation")

    # make the play button
    play_button = Button(ai_settings, screen, "Play")

    # create instance to store game stats
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # Make ship, reference the screen we created for coordinate matching
    ship = Ship(ai_settings, screen)

    # make a group to store bullets
    bullets = Group()

    # make a group to store aliens
    aliens = Group()

    # create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets)
            gf.check_collisions_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, aliens)
            gf.check_collisions_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.check_location_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

# kick off the run_game() function
run_game()


#weekly log
#week1: Oliver and I decided to work together to create a version of space invaders.
#week2: We found a template from github that we want to utilize 
#week2: We started to look at crash course as another resource for our game. Also, we began to code the start of the code

#day 1 code add more stuff