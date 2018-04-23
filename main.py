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

import sys

import pygame

def run_game():
    # Initialize game and create a screen object.
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Alien Invasion")

#mainloop for the game
while True:

    #Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT
        sys.exit()

        #Make screen visiable
        pygame.display.flip()

run_game()

#background color setup
bg_color = (0,0,255) 
#(0,0,225) is blue

#Redraw the screen during each pass through the loop
screen.fill(bg_color)

class Settings():
    """A class to store all settings for Space Invaders."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,255)

from settings import Settings

# Initialize pygame, settings, and screen object.

ai_settings = Settings()
screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))

    screen.fill(ai_settings.bg_color)

#SHIP CLASS

import pygame

class Ship():

    def__init__(self, screen):
    """Initialize the ship and set its starting position."""
    self.screen = screen

    # Load the ship image and get its rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    #Start each new ship at the bottom center of the screen
    self.rect.centerx = self

#this is not the completed project we are still moving the code into our project from the crashcourse and github. 




#weekly log
#week1: Oliver and I decided to work together to create a version of space invaders.
#week2: We found a template from github that we want to utilize 
#week2: We started to look at crash course as another resource for our game. Also, we began to code the start of the code

#day 1 code add more stuff