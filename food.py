""" File to create food """

import random
import pygame
import colors

__author__ = 'Preston Fawcett'
__email__ = 'ptfawcett@csu.fullerton.edu'
__maintainer__ = 'PrestonFawcett'

class Food():
    """ Structure for food item """
    def __init__(self, screen):
        self._screen = screen
        self._dimension = (32, 32)
        self._x = 32 * random.randint(0, 23) + 16
        self._y = 32 * random.randint(0, 23) + 16
        self._grape = (self._x, self._y)
        self._respawn = False

    def draw(self):
        """ Draws food """
        if self._respawn:
            self._x = 32 * random.randint(0, 23) + 16
            self._y = 32 * random.randint(0, 23) + 16
            self._respawn = False
        grape = pygame.Rect(self._x, self._y, 32, 32)
        pygame.draw.rect(self._screen, colors.purple, grape)

    def update(self):
        """ Updates to respawn food """
        self._respawn = True
